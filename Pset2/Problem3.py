"""
Paying Debt Off in a Year Using Bisection Search
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. 
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without 
running into the problem of slow code? 
We can make this program run faster using a technique introduced in lecture - bisection search!
The following variables contain values as described below:
1)   balance - the outstanding balance on the credit card
2)   annualInterestRate - annual interest rate as a decimal
 
To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance 
within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, 
but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth 
of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.
What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. 
What we ultimately pay must be greater than what we would've paid in monthly installments, 
because the interest was compounded on the balance we didn't pay off each month. 
So a good upper bound for the monthly payment would be one-twelfth of the balance, 
after having its interest compounded monthly for an entire year.
"""

increment = 0.01
lower = balance / 12
upper = balance * ((1 + annualInterestRate / 12.0) ** 12) / 12.0
monthlyPayment = (lower + upper) / 2.0
tempBalance = balance
while abs(tempBalance) >= 0.01:
    month = 12
    tempBalance = balance
    while month > 0:
        tempBalance = tempBalance - monthlyPayment + (annualInterestRate / 12.0) * (tempBalance - monthlyPayment)
        month -= 1
    if abs(tempBalance) < 0.01:
        print("Lowest Payment:",round(monthlyPayment,2))
    else:
        if tempBalance < 0:
            upper = monthlyPayment
        else:
            lower = monthlyPayment
monthlyPayment = (lower + upper) / 2.0
