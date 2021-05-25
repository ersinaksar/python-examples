name = str(input("Enter employee's name: "))
hoursWork = int(input("Enter number of hours worked in a week: "))
hourlyPayRate = float(input("Enter hourly pay rate: "))
federalWitholding = float(input("Enter federal tax withoulding rate: "))
stateWitholding = float(input("Enter state tax withoulding rate: "))

print("Employee Name: " ,name)
print("Hours worked: " , hoursWork)
print("Pay rate: $" , hourlyPayRate)

grossPay = hoursWork * hourlyPayRate;
print("Gross pay: $" ,grossPay)

federalWitholding = federalWitholding * 100
stateWitholding = stateWitholding * 100

federalTax = (federalWitholding * grossPay) / 100

stateTax = (stateWitholding * grossPay) / 100

deduction = federalTax + stateTax
netPay = grossPay - deduction

print("Deductions : ")
print("    Federal Witholding (" ,federalWitholding , "%): $" , federalTax)
print("    State Witholding (" ,stateWitholding , "%): $" ,stateTax)
print("    Total Deduction: $" ,deduction)
print("Net Pay: $" , netPay)
