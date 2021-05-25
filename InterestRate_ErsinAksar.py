loanAmount = float(input("Loan Amount: "))
years = float(input("Number of Years: "))
interestRate = float(5.0)
print("\nInterest Rate\t" + "Monthly Payment\t" + "Total Payment")
while interestRate <= 8.0:
    MonRate = float(interestRate / 12 / 100)
    MonthlyPayment = float(loanAmount * MonRate / (1 - 1 / pow(1 + MonRate, years * 12)))
    TotalPayment = format(MonthlyPayment * years * 12, ".2f")
    print(format(interestRate, ".3f"), end="%\t\t\t")
    print(format(MonthlyPayment, ".2f"), end="\t\t\t")
    print(TotalPayment, end="\n")
    interestRate += 1 / 8
