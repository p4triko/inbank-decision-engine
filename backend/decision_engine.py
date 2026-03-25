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

    if personalCode == "49002010965":
        debt = True
    elif personalCode == "49002010976":
        segment = 1
    elif personalCode == "49002010987":
        segment = 2
    elif personalCode == "49002010998":
        segment = 3

    if not debt:
        creditScore = calculate_credit_score(loanAmount, loanPeriod, modifiers[segment])
        if creditScore >= 1:
            result["decision"] = "positive"
            result["amount"] = loanAmount
            result["period"] = loanPeriod
            
            return result
        else:
            newDecision = calculate_new_decision_and_sum(loanAmount, loanPeriod, modifiers[segment])
            result["decision"] = newDecision["newDecision"]
            result["amount"] = newDecision["newAmount"]
            result["period"] = newDecision["newPeriod"]

            return result

    result["decision"] = "negative"
    result["amount"] = 0
    result["period"] = loanPeriod

    return result

def calculate_new_decision_and_sum(amount: int, period: int, creditModifier: int):
    newResult = dict()

    newResult.setdefault("newDecision", "negative")
    newResult.setdefault("newAmount", amount)
    newResult.setdefault("newPeriod", period)

    for p in range(period, maximumPeriod + 1, 1):
        creditScore = calculate_credit_score(amount, p, creditModifier)
        if creditScore >= 1:
            newResult["newDecision"] = "positive"
            newResult["newAmount"] = amount
            newResult["newPeriod"] = p
            return newResult
    
    for a in range(amount, minimumSum - 1, -1):
        creditScore = calculate_credit_score(a, period, creditModifier)
        if creditScore >= 1:
            newResult["newDecision"] = "positive"
            newResult["newAmount"] = a
            newResult["newPeriod"] = period
            return newResult
    
    return newResult

def calculate_credit_score(amount: int, period: int, creditModifier: int):
    return (creditModifier / amount) * period