import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import AgentExecutor
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

def get_response(model_name, model_provider, system_prompt, messages, allow_search):
    """
    Function to get a response from the agent.
    """
    try:
        #model Used: llama3-70b-8192
        groq_llm = ChatGroq(model =model_name, temperature=0.0, api_key=GROQ_API_KEY)
        search_tool = TavilySearchResults(max_results=3, TAVILY_API_KEY=TAVILY_API_KEY)
        tools = [search_tool]
       #os.environ["LANGCHAIN_TRACING_V2"] = "false"


        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(groq_llm, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools)

        respose = agent_executor.invoke({"input": "Tell me about the crypto currency market?"})
        return respose["output"]
    except Exception as e:
        return str(e)

#openai_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0, api_key=OPENAI_API_KEY)
"""groq_llm = ChatGroq(model ="llama3-70b-8192", temperature=0.0, api_key=GROQ_API_KEY)
search_tool = TavilySearchResults(max_results=3, TAVILY_API_KEY=TAVILY_API_KEY)
tools = [search_tool]
os.environ["LANGCHAIN_TRACING_V2"] = "false"


prompt = hub.pull("hwchase17/react")
agent = create_react_agent(groq_llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

respose = agent_executor.invoke({"input": "Tell me about the crypto currency market?"})
print(respose["output"])"""
