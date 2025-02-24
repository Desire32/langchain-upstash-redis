## What does it do?

Flask server for the custom LLM chatbot. The bot works with Ollama LLM (e.g. Mistral 7B or whatever you decided to use) and uses Upstash Redis to store chat history.

## How does it work?

Session_hash is needed for random session key generation, every time we launch llm, we would have different sessions
```bash
global session_hash
session_hash = str(random.randint(1000000, 9999999))
```

This is how we make a connection between llm and upstash redis, where we need to initialize our url-env and token-env
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
            "You are helpful assistant from UCLan VR Museum, UCLan is the british university, abbreviature is University of Central Lancashire of Cyprus, your name is Martin"
        ),
        MessagesPlaceholder(variable_name="chat_history"), # template
        ("human", "{input}"),
        
    ]
)
```

Choose the model you have installed and attach it to the chain
```bash
model = OllamaLLM(model="mistral:7b")
chain = prompt_template | model
chat_history = history.messages
```

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

3. Clone the repo:
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

or simply use the requirements.txt:

``
pip install -r requirements.txt
``

## Stack
- Upstash Redis
- python-langchain
- ollama engine


## Screenshots

This is how it looks like in Upstash Redis, our dialog is being saved with custom ttl, in json format, and random session key:

![Screenshot 2025-02-24 at 22 11 28](https://github.com/user-attachments/assets/be9b2028-f747-40b8-90dc-dfa0ddce7b41)

Response speed depends on hardware specs, for example for RTX 30x series "hello" prompt would take 2 seconds max, but tests have been made on MacOS:

![Screenshot 2025-02-24 at 22 10 15](https://github.com/user-attachments/assets/d029624d-3bd7-4cf9-ad61-d9d13bd3a55d)

## License

The project is protected by MIT License.
