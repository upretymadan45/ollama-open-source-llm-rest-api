import requests
import json
import streamlit as st

request = {
    "url":"http://localhost:11434/api/generate",
    "headers":{
        "Content-Type":"application/json"
    },
    "data":{
        "model": "llama2",
        "stream": False
    }
}

def getAPIResponse(url, headers, data):
    response = requests.post(url, headers=headers, data = json.dumps(data))

    if response.status_code == 200:
        return response.json().get("response")
    else:
        return "Error getting data"
    
def processUI():
    st.title("Welcome to running LLAMA2 using OLLAMA locally")
    textInput = st.text_input("Enter your question")
    submit = st.button("Submit")

    if submit:
        request["data"]["prompt"] = textInput
        url = request["url"]
        headers = request["headers"]
        data = request["data"]
        result = getAPIResponse(url, headers,data)
        print(result)
        st.write(result)

if __name__ == "__main__":
    processUI()