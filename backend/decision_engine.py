minimumSum = 2000
maximumSum = 10000

minimumPeriod = 12
maximumPeriod = 60

def assess_loan_request(personalCode: str, loanAmount: int, loanPeriod: int):
    # Takes in personal code, loan amount, loan period in
    # months and returns a decision
    # Returns -> (negative or positive) and the amount.

    result = dict()
    result.setdefault("decision", "")
    result.setdefault("amount", 0)
    result.setdefault("period", 0)

    modifiers = {
        1: 100,
        2: 200,
        3: 1000 
    }

    debt = False 
    segment = -1

    # Define which segments we need to apply when calculating credit score.
    if personalCode == "49002010965":
        debt = True
    elif personalCode == "49002010976":
        segment = 1
    elif personalCode == "49002010987":
        segment = 2
    elif personalCode == "49002010998":
        segment = 3

    # Proceed with credit score and amount calculations if the person has no debt.
    if not debt:
        # Let's check for how much is the person actually eligible for in terms of sum, while keeping it
        # constrained.
        maxApprovedAmount =  min(10000, modifiers[segment] * loanPeriod)

        if maxApprovedAmount >= loanAmount and maxApprovedAmount >= minimumSum:
            result["decision"] = "positive"
            result["amount"] = maxApprovedAmount
            result["period"] = loanPeriod
            return result
        else: # Let's see if we can offer an alternative.
            newDecision = calculate_new_decision_and_sum(loanAmount, loanPeriod, modifiers[segment])
            result["decision"] = newDecision["newDecision"]
            result["amount"] = newDecision["newAmount"]
            result["period"] = newDecision["newPeriod"]

            return result
    
    # Scenario has gone through all required checks, didn't pass them so we only really to return a negative decision.
    result["decision"] = "negative"
    result["amount"] = 0
    result["period"] = loanPeriod

    return result

def calculate_new_decision_and_sum(amount: int, period: int, creditModifier: int):
    # Takes in amount, period and credit modifier and based on that we calculate a new eligible decision and
    # amount basically.
    # Returns -> new decision along with the sum.

    newResult = dict()
 
    newResult.setdefault("newDecision", "negative")
    newResult.setdefault("newAmount", amount)
    newResult.setdefault("newPeriod", period)

    # For both of these checks it's importnant to note that we need to stay within our min and max boundraries.
    # First let's check if we can extend the period, basically extending the time it takes to pay.
    for p in range(period, maximumPeriod + 1, 1):
        creditScore = calculate_credit_score(amount, p, creditModifier)
        if creditScore >= 1:
            newResult["newDecision"] = "positive"
            newResult["newAmount"] = amount
            newResult["newPeriod"] = p
            return newResult
    
    # Extending the period didn't help, so let's see if we can the drop the requested amount.
    for a in range(amount, minimumSum - 1, -1):
        creditScore = calculate_credit_score(a, period, creditModifier)
        if creditScore >= 1:
            newResult["newDecision"] = "positive"
            newResult["newAmount"] = a
            newResult["newPeriod"] = period
            return newResult
    
    return newResult

def calculate_credit_score(amount: int, period: int, creditModifier: int):
    # Takes in amount, period and credit modifier and based on that we calculate the credit score.
    # Returns -> credit score.
    return (creditModifier / amount) * period