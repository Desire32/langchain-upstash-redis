## What does it do?

Flask server for the custom LLM chatbot. The bot works with Ollama LLM (e.g. Mistral 7B or Llama3) and uses Upstash Redis to store chat history.

## How does it work?

## How do i use it?

1. Ollama installation:

macos

``
brew install ollama
``

linux

``
curl -fsSL https://ollama.com/install.sh | sh
``

windows

Download the installer from the official website: https://ollama.com/download
Install Ollama by following the instructions.

Follow the link to select a model:

https://ollama.com/search

```bash
ollama start # in separate console

ollama pull <model_name>

ollama serve
```


2. Clone the repo:
```bash
   git clone https://github.com/Desire32/langchain-llm-research-paper.git

   cd langchain-llm-research-paper/
```

MacOS:
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip3 install flask langchain langchain-core langchain-ollama langchain-community langsmith python-dotenv upstash-redis
```
Windows/Linux:
```bash
   python -m venv venv
   venv\Scripts\activate
   pip install flask langchain langchain-core langchain-ollama langchain-community langsmith python-dotenv upstash-redis
```

## Stack
- Upstash Redis
- python-langchain
- ollama engine
