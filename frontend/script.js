// Test case
const code = "49002010987"
const amount = 2000
const period = 12

fetch("http://localhost:8000/decisions" , {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        personalCode: code,
        loanAmount: amount,
        loanPeriod: period
    })
})
.then(respone => respone.json())
.then(json => {
    console.log("Loan decision: ", json);
    // TODO Modifiy HTML based on the loan assessment
})
.catch(error => console.error("Error: ", error))

console.log("Hello")