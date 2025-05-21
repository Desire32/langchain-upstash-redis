<p align="center">
  <img src="https://github.com/user-attachments/assets/8fe8b0b6-b66b-4649-bbae-2fa9b537af5f" alt="Frame 3" />
</p>

# LangChain Chat with Upstash Redis and Ollama

A powerful chat application that combines LangChain, Upstash Redis for message history storage, and Ollama for local LLM inference. This project demonstrates how to build a chat application with persistent memory using Redis and local LLM capabilities.

## Features

- 🤖 Local LLM inference using Ollama
- 💾 Persistent chat history with Upstash Redis
- 🔄 Streaming response support
- 🔒 Session-based chat history management
- 🌐 Flask-based REST API
- 🚀 Easy to deploy and scale

## Prerequisites

### 1. Ollama Installation

#### macOS
```bash
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows
Download the Ollama from the official website: https://ollama.com/download

Start Ollama and pull your preferred model:
```bash
ollama start # in separate console
ollama pull <model_name> # e.g., mistral:7b, llama2, etc.
```

### 2. Upstash Redis Setup

1. Create an account at [Upstash Console](https://console.upstash.com/)
2. Create a new Redis database
3. Copy your credentials:
   - UPSTASH_REDIS_REST_URL (URL)
   - UPSTASH_REDIS_REST_TOKEN (TOKEN)

### 3. Environment Setup

Create a `.env` file in the project root with:
```
URL=your_upstash_redis_url
TOKEN=your_upstash_redis_token
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python ai_mode.py
```

2. The server will run on `http://localhost:8080`
3. Send POST requests to the root endpoint with your message in the request body

## Technical Stack

- **Backend Framework**: Flask
- **LLM Integration**: 
  - LangChain
  - Ollama (local LLM)
- **Database**: Upstash Redis
- **Message History**: LangChain Chat Message History
- **Environment Management**: python-dotenv

## Configuration Options

The application supports two modes of chat history storage:
1. Session-based (default): Each session gets a unique ID
2. Persistent: Uses a fixed session ID for continuous conversation

To switch modes, modify the chat history configuration in `ai_mode.py`.

## License

This project is licensed under the MIT License.
