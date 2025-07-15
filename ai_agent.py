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

#openai_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0, api_key=OPENAI_API_KEY)
groq_llm = ChatGroq(model ="llama3-70b-8192", temperature=0.0, api_key=GROQ_API_KEY)
search_tool = TavilySearchResults(max_results=3, TAVILY_API_KEY=TAVILY_API_KEY)
#from langgraph.prebuilt import create_react_agent
from langchain.agents import AgentExecutor
tools = [search_tool]
from langchain import hub
#from langchain_community.llms import OpenAI
from langchain.agents import AgentExecutor, create_react_agent
os.environ["LANGCHAIN_TRACING_V2"] = "false"

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(groq_llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

respose = agent_executor.invoke({"input": "Tell me about the crypto currency market?"})
print(respose["output"])
