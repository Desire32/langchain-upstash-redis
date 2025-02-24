from flask import Flask, request
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import UpstashRedisChatMessageHistory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from dotenv import load_dotenv
import os
import random


from langsmith import Client

app = Flask(__name__)

load_dotenv()

# session generate key, global to generate once for session
global session_hash
session_hash = str(random.randint(1000000, 9999999))


# for individual history
history = UpstashRedisChatMessageHistory(
    url=os.getenv("URL"), token=os.getenv("TOKEN"), ttl=10000, session_id=(f"{session_hash}")
)

# for general history
# history = UpstashRedisChatMessageHistory(
#     url=os.getenv("URL"), token=os.getenv("TOKEN"), ttl=1000000000, session_id=("session")
# )

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

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
#model = OllamaLLM(model="deepseek-r1:8b")
model = OllamaLLM(model="mistral:7b")
specific_chunks_model = OllamaLLM(model="llama3.2", callbacks=callback_manager)
chain = prompt_template | model
chat_history = history.messages

# TODO chunks (optional)

@app.route('/', methods=['POST'])
def start_up():
    query = request.get_data(as_text=True) # plain text use
    response = chain.invoke({"input": query, "chat_history": chat_history})

# save locally
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response))

# save also on a server
    history.add_message(HumanMessage(content=query))
    history.add_message(AIMessage(content=response))

# return to the user in console
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)