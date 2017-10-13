"""
Paying Debt Off in a Year 
Write a program that calculates the minimum fixed monthly payment needed 
in order to pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
1)   balance - the outstanding balance on the credit card
2)   annualInterestRate - annual interest rate as a decimal
The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month 
(after the payment for that month is made). The monthly payment must be a multiple of $10 
and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, 
which is okay.
"""

monthlyPayment = 0
monthlyIntRate = annualInterestRate/12
while balance > 0:
    months = 12
    monthlyPayment += 10
    tempBalance = balance
    while months > 0 :
        unpaidBalance=tempBalance-monthlyPayment       
        tempBalance=unpaidBalance + monthlyIntRate* (unpaidBalance)
        months -= 1
        if tempBalance <= 0:
            balance = tempBalance
print("Lowest Payment:",monthlyPayment)
