from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decision_engine import assess_loan_request

app = FastAPI()

class Loan(BaseModel):
    personalCode: str
    loanAmount: int
    loanPeriod: int

@app.post("/decisions")
def decide_loan(loan: Loan):
    code = loan.personalCode
    amount = loan.loanAmount
    period = loan.loanPeriod

    decision = "TEST"

    return decision
