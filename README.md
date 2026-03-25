# Inbank Product Engineer Intern Test Task
## Technology used
Frontend - HTML, CSS and JS <br>
Backend - Python and FastAPI for building the API endpoint

## Prerequisites
1. pip (package installer for python) needs to installed.
2. In the terminal run the following commands:
   ```
   pip install fastapi
   ```
   ```
   pip install uvicorn
   ```
## Instructions
1. Clone the repository.
2. Open the folder in a code editor.
3. Navigate to the backend folder.
4. In the terminal run the command
   ```
   uvicorn main:app --reload
   ```
5. Open the index.html file in a browser, comfortable way is to use Live Server in VsCode.

## API endpoint
System provides just one main endpoint.
### Assess loan eligibility
* **URL:** `/decisions`
* **Method:** `POST`
* **Content-Type:** `application/json`

**An example of a request body**
```json
{
   "personalCode":  "49002010976"
   "loanAmount": 2000,
   "loanPeriod": 12
}
```

**Positive decision**
```json
{
   "decision":  "positive"
   "amount": 2000,
   "period": 20
}
```
Here the amount is adjusted, because approved amount didn't suffice.

**Negative decision**
```json
{
   "personalCode":  "negative"
   "loanAmount": 0,
   "loanPeriod": 12
}
```

## What is one thing you would improve about the take home assignment and how would you improve it?
Possibly add more parameters to mix which in turn would make the algorhitm for assessing the right for loans more interesting possibly. Maybe introduce loan types, for example student loans mortgages/etc and assess how these factor in. <br>
<br>
If I were to improve one thing about my own assignment, it would be the input side of things. Right now the only form of input is a slider, which does make precise inputs more difficult. In terms of implementing it there definitely needs to be some form of input validation, because
we are dealing with min and max for both the required values. The user would enter a value and then it would be ran through a filter basically to sort out all the bad.
