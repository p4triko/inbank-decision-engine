from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decision_engine import assess_loan_request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Since the frontend and backend side run on different addresses, we need to configure
# Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'], # List of origins that should be permitted to make cross-origin requests
                           # Should be more specific, but for the sake of this task we allow any origin
    allow_credentials = False, # Not required, since we don't need any form of logging in for this task
    allow_methods = ['POST'], # We only need to send data
)

# This will be our request body.
class Loan(BaseModel):
    personalCode: str
    loanAmount: int
    loanPeriod: int

@app.post("/decisions")
def decide_loan(loan: Loan):
    code = loan.personalCode
    amount = loan.loanAmount
    period = loan.loanPeriod

    decision = assess_loan_request(code, amount, period)

    return decision