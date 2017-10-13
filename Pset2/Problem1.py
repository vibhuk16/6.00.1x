"""
Paying Debt off in a Year
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
The following variables contain values as described below:
1)  balance - the outstanding balance on the credit card
2)  annualInterestRate - annual interest rate as a decimal
3)  monthlyPaymentRate - minimum monthly payment rate as a decimal
For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print
Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of the year in the format:
Remaining balance: 4784.0
"""

count = 12
monthIntRate = annualInterestRate/12   
while count > 0:
    unpayedBalance = balance - (balance*monthlyPaymentRate)
    balance= unpayedBalance+monthIntRate * (unpayedBalance)
    count -= 1
print("Remaining balance:", round(balance,2))
