import math

fact = math.factorial #just an alias to make the formulas shorter & sweeter

def generate_outcomes(numBushes):
    '''
    Return a humongous list of all possible outcomes
    for breaking numBushes bushes, formatted as:
    [# of 0 rupees, # of 1 rupee, # of 2 rupees, # of 3 rupees]
    '''
    alloutcomes = []
    for i in range(numBushes+1):
        for j in range(numBushes-i+1):
            for k in range(numBushes-i-j+1):
                alloutcomes.append([i,j,k,numBushes-i-j-k])
    return alloutcomes

def total_rupees(outcome):
    '''
    For a given outcome, return the total number of rupees collected.
    '''
    return 0*outcome[0] + 1*outcome[1] + 3*outcome[2] + 5*outcome[3]

def odds(outcome):
    '''
    For a given outcome, return the odds of that outcome using the probability
    density function for a multinomial distribution.
    '''
    numBushes = outcome[0]+outcome[1]+outcome[2]+outcome[3]
    numerator = fact(numBushes) * (9/16)**outcome[0] * (5/16)**outcome[1] * (1/16)**outcome[2] * (1/16)**outcome[3]
    denominator = fact(outcome[0]) * fact(outcome[1]) * fact(outcome[2]) * fact(outcome[3])
    return numerator/denominator

def odds_at_least(rupeeCount, allOutcomes):
    '''
    Given a desired minimum rupeeCount and a list of allOutcomes possible,
    return the odds of collecting at least that many rupees.
    '''
    ret = 0
    for outcome in allOutcomes:
        if total_rupees(outcome) >= rupeeCount:
            ret += odds(outcome)
    return ret

def odds_to_90(rupees, bushesLeft):
    '''
    Given a current number of rupees and the number of bushesLeft,
    return the odds of having >=90 rupees after breaking the remaining bushes.
    '''
    outcomes = generate_outcomes(bushesLeft)
    return odds_at_least(90-rupees, outcomes)

print("The odds of getting at least 90 rupees in 84 bushes is " + str(odds_to_90(0,84)*100) + "%.")