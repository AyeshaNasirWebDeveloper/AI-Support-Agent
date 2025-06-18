from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import re
import logging
from typing import Dict, Optional
from dotenv import load_dotenv
import google.generativeai as genai

# Configuration
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ai-support-agent.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Gemini with correct model name
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash') 

class Message(BaseModel):
    message: str
    session_id: Optional[str] = "default"

# Enhanced Store Knowledge Base
STORE_KNOWLEDGE = """
## About Ayesha's Shopping Store
We're a premium online retailer specializing in:
- Fashion apparel (women's, men's, kids)
- Handmade jewelry and accessories
- Organic beauty products
- Home decor items

## Policies
- Shipping: Free on orders over $50 (3-5 business days)
- Returns: 30 days with original packaging
- Contact: support@ayeshastore.com or (555) 123-4567

## Current Promotions
1. Summer Sale - 20% off all dresses
2. New customer discount - 15% off first order
"""

# Order Database
ORDER_DB = {
    "ORD123": {
        "status": "Shipped", 
        "delivery": "June 20, 2025",
        "items": ["Silk Maxi Dress (Size M)", "Gold Hoop Earrings"],
        "total": "$89.98"
    },
    "ORD456": {
        "status": "Processing", 
        "delivery": "Est. June 25, 2025",
        "items": ["Organic Face Cream", "Bamboo Hairbrush"],
        "total": "$42.50"
    }
}

# Conversation Memory
conversations: Dict[str, Dict] = {}

def build_context(session_id: str) -> str:
    """Build dynamic conversation context"""
    context = [STORE_KNOWLEDGE]
    
    if session_id in conversations:
        conv = conversations[session_id]
        
        if 'order_id' in conv:
            order = ORDER_DB.get(conv['order_id'])
            if order:
                context.append(
                    f"Current Order: {conv['order_id']}\n"
                    f"Status: {order['status']}\n"
                    f"Items: {', '.join(order['items'])}\n"
                    f"Total: {order['total']}"
                )
        
        if 'history' in conv:
            context.append("Recent Messages:")
            for msg in conv['history'][-3:]:
                context.append(f"Customer: {msg['user']}")
                context.append(f"Assistant: {msg['response']}")
    
    return "\n\n".join(context)

@app.post("/ask")
async def ask_agent(data: Message):
    try:
        # Initialize session
        session_id = data.session_id
        if session_id not in conversations:
            conversations[session_id] = {'history': []}
        
        conv = conversations[session_id]
        user_message = data.message.strip()
        
        # Auto-detect order numbers
        if order_match := re.search(r"(ORD\d+)", user_message.upper()):
            conv['order_id'] = order_match.group(1)
        
        # Build intelligent prompt
        prompt = f"""
ROLE: You are Ayesha, the AI assistant for Ayesha's Shopping Store. Your personality:
- Friendly and approachable
- Knowledgeable about all store products and policies
- Professional but warm tone

CONTEXT:
{build_context(session_id)}

CUSTOMER MESSAGE: {user_message}

INSTRUCTIONS:
1. First check if this relates to an existing order
2. For order questions, verify details before responding
3. Answer general questions using the store knowledge
4. Keep responses concise but helpful (1-2 paragraphs max)
5. End with a relevant follow-up question when appropriate
6. Manage delays in order processing with empathy
"""
        # Get AI response
        response = model.generate_content(prompt)
        reply = response.text.strip()
        
        # Update conversation history
        conv['history'].append({
            'user': user_message,
            'response': reply
        })
        
        return {"reply": reply}
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            "reply": "I'm having some technical difficulties. Please email support@ayeshastore.com for immediate assistance.",
            "error": str(e)
        }

@app.get("/health")
async def health_check():
    return {"status": "active", "service": "Ayesha's Shopping Assistant"}

@app.get("/")
async def welcome():
    return {"message": "Welcome to Ayesha's Shopping Store API"}