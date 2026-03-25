let amountSlider = document.getElementById("amountSlider");
let valueAmount = document.querySelector(".amountDisplay");

let periodSlider = document.getElementById("periodSlider");
let valuePeriod = document.querySelector(".periodDisplay");


valueAmount.innerHTML = amountSlider.value;
valuePeriod.innerHTML = periodSlider.value;

sendRequest();

amountSlider.addEventListener("input", function () {
    valueAmount.textContent = this.value;
});

// Send request only when the sliders are set put, otherwise we will be shooting out requests non-stop everytime
// the sliders moves for each number. Same applies to the other slider.
amountSlider.addEventListener("change", sendRequest);

periodSlider.addEventListener("input", function () {
    valuePeriod.textContent = this.value;
});

periodSlider.addEventListener("change", sendRequest);

// Update the decision when we change the scenarios for better comparison.
document.querySelectorAll('input[name="scenario"]').forEach(element => {
    element.addEventListener("change", sendRequest);
});

// This will act as our main request, we will use it to basically refresh the page constantly throughout
// slider and scenario changes, also we call it first when loading the page.
function sendRequest(){
    let selectedScenario = document.querySelector("input[name=scenario]:checked");
    fetch("http://localhost:8000/decisions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            personalCode: selectedScenario.value,
            loanAmount: parseInt(amountSlider.value),
            loanPeriod: parseInt(periodSlider.value),
        }),
    })
    .then((respone) => respone.json())
    .then((json) => {
        console.log("Loan decision: ", json);
        let result = document.querySelector(".eligibilityReport");
        
        if (json.decision == "positive") {
            result.innerHTML = `Decision: Positive | Amount: ${json.amount}`;
        }else{
            result.innerHTML = "Decision: Negative";
        }
    })
    .catch((error) => console.error("Error: ", error));
}