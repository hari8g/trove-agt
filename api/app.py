from fastapi import FastAPI
from models.agents.financial_agent import FinancialAgent

app = FastAPI()

@app.get("/financial/")
def analyze(query: str):
    agent = FinancialAgent()
    return {"response": agent.analyze_financial_query(query)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
