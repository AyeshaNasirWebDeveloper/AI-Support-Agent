# Ayesha's Shopping Store - AI Customer Support Agent

## Overview

This project provides an AI-powered customer support interface for Ayesha's Shopping Store, featuring:

- Natural language conversation with customers
- Order tracking functionality
- Product and policy information
- Beautiful, animated UI with Tailwind CSS
- Fully responsive design

## Features

✨ **Elegant Chat Interface**  
🎨 **Tailwind CSS Styling**  
🌐 **Responsive Design**  
🤖 **AI-Powered Responses**  
📦 **Order Tracking Integration**  
⏱️ **Real-time Message Timestamps**  
🌀 **Smooth Animations**  
🚀 **FastAPI Backend Integration**

## Installation

### Prerequisites

- Node.js (v16 or later)
- Python (3.8 or later)
- npm or yarn

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Create a `.env.local` file with:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Create a `.env` file with:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

1. Access the frontend at `http://localhost:3000`
2. Interact with the AI customer support agent
3. Ask about orders, products, or store policies

## Project Structure

```
/ayesha-shopping-support
├── /frontend               # Next.js application
│   ├── /pages              # Application pages
│   ├── /public             # Static files
│   └── package.json        # Frontend dependencies
│
├── /backend                # FastAPI application
│   ├── main.py             # API endpoints
│   └── .env                # Environment variables
│
├── README.md               # This file
├── .gitignore              # Git ignore rules
```

## Customization

### Backend Customization

Modify the AI responses in:
- `backend/main.py`

## Troubleshooting

**Hydration Errors**:
- Ensure all dynamic content is client-side rendered
- Verify consistent timestamp formatting

**API Connection Issues**:
- Check CORS settings in backend

**Missing Environment Variables**:
- Ensure both `.env` (backend)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact:
- Email: ayeshanasir07000@gmail.com
- Linkedln: `https://www.linkedin.com/in/ayeshanasirwin/`

---

**Enjoy your enhanced customer support experience!** 🛍️💬