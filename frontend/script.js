fetch("http://localhost:8000/decisions" , {
    method: "Post",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        personalCode: code,
        loanAmount: amount,
        loanPerioud: period
    })
})
.then(respone => respone.json())
.then(json => {
    console.log("Loan data: ", json);
    // TODO Modifiy HTML based on the loan assessment
})
.catch(error => console.error("Error: ", error))