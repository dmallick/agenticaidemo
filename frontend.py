import streamlit as st

st.set_page_config(page_title="Frontend Agentic AI", page_icon=":guardsman:", layout="wide")
st.title("Agentica AI Demo")
st.write("This is a demo of the Agentica AI API. You can interact with the AI model here.")

system_prompt = st.text_area("System Prompt", "Define you AI Agent.")

provider=st.radio("Select Provider:", ("Groq", "OpenAI"))

MODEL_NAMES_GROQ = ["llama3-70b-8192", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")
user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")
API_URL="http://127.0.0.1:8090/chat"
if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")