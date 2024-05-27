import arrr
from pyscript import document
#from langchain_community.llms import Ollama

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

    #llm = Ollama(model="llama3")
    #print(llm.invoke("Tell me a joke"))
    #output_div.innerText = llm.invoke("Tell me a joke")

