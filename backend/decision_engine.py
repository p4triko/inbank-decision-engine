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
        
        creditScore = calculate_credit_score(loanAmount, loanPeriod, segment, modifiers[segment])
        if creditScore >= 1:
            result["decision"] = "positive"
            result["amount"] = loanAmount
            
            return result
        else:
            newDecision = calculate_new_decision_and_sum(loanAmount, loanPeriod, modifiers[segment])

            return result

    result["decision"] = "negative"
    result["amount"] = 0
    return result

def calculate_new_decision_and_sum(amount: int, period: int, creditModifier: int):
    newResult = dict()

    newResult.setdefault("newDecision", "")
    newResult.setdefault("newAmount", 0)

    return newResult

def calculate_credit_score(amount: int, period: int, segment: int, creditModifier: int):
    return (creditModifier / amount) * period