# WAP to calculate gross salary and net salary of an employee
# da = Dearness Allowance
# hra = House Rent Allowance
# Pf = Provident Fund Income Tax

def da(basic):
    da = basic*80/100
    return da
def hra(basic):
    hra = basic*15/100
    return hra
def pf(basic):
    pf = basic*12/100
    return pf
def intax(gross):
    tax = gross*0.1
    return tax
basic = float(input("Enter basic salary: "))
gross = basic + da(basic) + hra(basic)
print("your gross salary: {:10.2f}".format(gross))
net = gross - pf(basic) - intax(gross)
print("your net Salary : {:10.2f}".format(net))
