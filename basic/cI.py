# Python3 program to find compound 
# interest for given values. 

# Compound Interest = P(1 + R/100)r

def compound_interest(principle, rate, time):
    # Calculates compound interest  
    CI = principle * (pow((1 + rate / 100), time))
    print('Compound interest', CI)


compound_interest(10000, 10.25, 5)


