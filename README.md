# AI Workflow Assistant (React + LangGraph)

This project is an AI-powered workflow assistant that automates multi-step tasks. Given a high-level goal, the AI can perform web research, summarize its findings, and draft content like a blog post.

This application demonstrates the power of `LangGraph` to create reliable, stateful AI agents and a `React.js` frontend to provide a rich user experience.

## 🌟 Features

-   **Multi-Step Workflows**: Defines a clear `search` → `summarize` → `write` flow using LangGraph.
-   **Real-Time Information**: Uses the DuckDuckGo Search tool to access up-to-date information from the web.
-   **Gemini-Powered Intelligence**: Leverages Google's Gemini 1.5 Flash model for summarization and content generation.
-   **Interactive UI**: A simple and clean React.js interface to input tasks and view step-by-step outputs.
-   **Separation of Concerns**: A distinct Python/Flask backend for AI logic and a React frontend for the user interface.

## 🛠️ Prerequisites

-   Python 3.10+
-   Node.js and npm (or yarn)

## 🚀 Installation & Setup

### 1. Backend Setup

First, navigate to the `backend` directory and set up the Python environment.

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

#### Get Your Free API Key

This project uses a free API key from **Google AI Studio**.

1.  Go to the [Google AI Studio website](https://aistudio.google.com/).
2.  Sign in and click "**Get API Key**".
3.  Create a new file named `.env` in the `backend` directory.

Now, add your new API key to the `.env` file:

```
# backend/.env
GEMINI_API_KEY="YOUR_NEW_AI_STUDIO_API_KEY"
```

### 2. Frontend Setup

In a separate terminal, navigate to the `frontend` directory and install the Node.js dependencies.

```bash
# Navigate to the frontend directory
cd ../frontend

# Install npm packages
npm install
```

## ▶️ Running the Application

You need to run both the backend server and the frontend application simultaneously.

### 1. Start the Backend Server

In your first terminal (in the `backend` directory):

```bash
# Ensure your virtual environment is active
# Then, start the Flask server
flask run --port=5000
```

The backend API will now be running at `http://localhost:5000`.

### 2. Start the Frontend Application

In your second terminal (in the `frontend` directory):

```bash
# Start the React development server
npm start
```

The application will automatically open in your browser at `http://localhost:3000`.
