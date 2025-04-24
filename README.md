<p align="center">
  <img src="https://github.com/user-attachments/assets/8fe8b0b6-b66b-4649-bbae-2fa9b537af5f" alt="Frame 3" />
</p>

## How to use

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

Download the Ollama from the official website: https://ollama.com/download

Follow the link to select a model:

https://ollama.com/search

```bash
ollama start # in separate console

ollama pull <model_name>
```

2. Upstash Redis configuration
   
Login into Upstash: https://console.upstash.com/

Choose details and look for REST_API and copy next parameters:
- UPSTASH_REDIS_REST_URL ( our "URL")
- UPSTASH_REDIS_REST_TOKEN ( our "TOKEN")

## Stack
- Upstash Redis
- python-langchain
- ollama

## License

The project is protected by MIT License.
