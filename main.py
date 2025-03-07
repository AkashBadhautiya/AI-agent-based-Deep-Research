from fastapi import FastAPI
from agents import research_agent, answer_drafter
from vector_store import store_research_data

app = FastAPI()

@app.get("/search")
def search(query: str):
    """Handles user query, fetches research data, stores it, and returns drafted response."""
    research_results = research_agent(query)
    store_research_data(research_results)
    state = {"research_results": research_results}
    result = answer_drafter(state)
    return {"response": result["final_answer"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
