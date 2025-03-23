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


##############
# Two ways of storing information into Upstash Redis
# Hint: if you want to increase TTL (time-to-leave), change the value "ttl=value"
##############

# Option 1:
# We use a random generate key, which means every session is going to be different, if you reload the model, it won't remember you
history = UpstashRedisChatMessageHistory(
    url=os.getenv("URL"), token=os.getenv("TOKEN"), ttl=10000, session_id=(f"{session_hash}")
)

# Option 2:
# You can ignore key generation and send it directly into pre-setup key, for example "session", it is going to remember you, even though you relaunched it.
#
# history = UpstashRedisChatMessageHistory(
#     url=os.getenv("URL"), token=os.getenv("TOKEN"), ttl=1000000000, session_id=("session")
# )

# Model behaviour
prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            "You are helpful assistant, your name is Mike, you are an AI located on the moon"
        ),
        MessagesPlaceholder(variable_name="chat_history"), # template
        ("human", "{input}"),
        
    ]
)

########
#callback_manager is a chunk mode, its going to be showing response dinamically, not in json format
########

#callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
#model = OllamaLLM(model="deepseek-r1:8b")
#specific_chunks_model = OllamaLLM(model="llama3.2", callbacks=callback_manager)

# choose the model and chain it
model = OllamaLLM(model="mistral:7b")
chain = prompt_template | model
chat_history = history.messages

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
