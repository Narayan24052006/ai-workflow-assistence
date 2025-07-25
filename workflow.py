# backend/workflow.py
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, END
from prompts import summarize_prompt, write_post_prompt

# Load environment variables from .env file
load_dotenv()

# Initialize the AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ.get("GEMINI_API_KEY")
)


# Initialize the Search tool
search_tool = DuckDuckGoSearchRun()

# Define the state for the workflow
class WorkflowState(TypedDict):
    task: str
    search_results: Annotated[str, "The results from the web search"]
    summary: Annotated[str, "The summary of the search results"]
    blog_post: Annotated[str, "The final generated blog post"]

# Define the nodes (functions) for the workflow
def search_node(state: WorkflowState):
    """Node to perform a web search based on the user's task."""
    print("Executing Search Node...")
    task = state["task"]
    results = search_tool.run(f"research for: {task}")
    return {"search_results": results}

def summarize_node(state: WorkflowState):
    """Node to summarize the search results."""
    print("Executing Summarize Node...")
    task = state["task"]
    search_results = state["search_results"]
    prompt = summarize_prompt.format(task=task, search_results=search_results)
    summary = llm.invoke(prompt).content
    return {"summary": summary}

def write_post_node(state: WorkflowState):
    """Node to write the blog post."""
    print("Executing Write Post Node...")
    task = state["task"]
    summary = state["summary"]
    prompt = write_post_prompt.format(task=task, summary=summary)
    blog_post = llm.invoke(prompt).content
    return {"blog_post": blog_post}

# Create the graph and add the nodes and edges
def build_graph():
    graph = StateGraph(WorkflowState)
    graph.add_node("search", search_node)
    graph.add_node("summarize", summarize_node)
    graph.add_node("write_post", write_post_node)

    # Define the flow of the graph
    graph.set_entry_point("search")
    graph.add_edge("search", "summarize")
    graph.add_edge("summarize", "write_post")
    graph.add_edge("write_post", END)

    return graph.compile()

# Instantiate the compiled graph
app_graph = build_graph()