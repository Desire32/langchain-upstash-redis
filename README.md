<p align="center">
  <img src="https://github.com/user-attachments/assets/8fe8b0b6-b66b-4649-bbae-2fa9b537af5f" alt="Frame 3" />
</p>

Python-langchain based LLM chatbot. Works with Ollama LLM (e.g. Mistral 7B or whatever you decided to use) and uses Upstash Redis to store chat history.

## Initialization

Session_hash is needed for random session key generation, every time we launch llm, we would have different sessions:
```bash
global session_hash
session_hash = str(random.randint(1000000, 9999999))
```

This is how we make a connection between llm and upstash redis, where we need to initialize our url-env and token-env:
```bash
history = UpstashRedisChatMessageHistory(
    url=os.getenv("URL"), token=os.getenv("TOKEN"), ttl=10000, session_id=(f"{session_hash}")
)
```

ChatPromptTemplate allows us to create an individual llm behavior, depends on your fantasy :)
```bash
prompt_template = ChatPromptTemplate(
    [ # choose the system's attitude
        (
            "system",
            "You are helpful assistant"
        ),
        MessagesPlaceholder(variable_name="chat_history"), # template
        ("human", "{input}"),
        
    ]
)
```

Choose the model you have installed and attach it to the chain:
```bash
model = OllamaLLM(model="mistral:7b")
chain = prompt_template | model
chat_history = history.messages
```

## Use

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

or simply use the requirements.txt:

``
pip install -r requirements.txt
``

Start the bot:

``
python3 ai_mode.py
``
LLM bot is using simple flask server, if you want to change the port and host:

```
app.run(host="your-host", port="your-port", debug="True/False, if you want to use debug stuff")
```

In order to communicate with LLM, open the console (there supposed to be one window for ollama engine and one for communication) and use:

``
curl -X POST http://<your-address>/<your-port> -d "<your-message>"
``

## Stack
- Upstash Redis
- python-langchain
- ollama

## License

The project is protected by MIT License.
