from langchain.tools import TavilySearchResults
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Set up Tavily Search Tool
os.environ["TAVILY_API_KEY"] = "your_api_key"
tavily_tool = TavilySearchResults()

# Initialize OpenAI model
llm = ChatOpenAI(model="gpt-4", temperature=0)

def research_agent(query):
    """Fetch online research results for a given query."""
    results = tavily_tool.run(query)
    return results

def answer_drafter(state):
    """Processes research results and generates a structured response."""
    research_data = state["research_results"]
    prompt = f"Based on the following research, draft a structured answer:\n\n{research_data}"
    response = llm([HumanMessage(content=prompt)]).content
    return {"final_answer": response}
