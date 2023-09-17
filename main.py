# performing tax rate calculations
def calcTaxRates(temp, salary, taxRateLists, highestBrack):
    counter = 0
    tax_subs = []
    while (temp > 0):
        tax_amt = 0
        if counter == (len(taxRateLists)-1): 
            highestBrack =  True
            break
        lower_bound = taxRateLists[counter][0]

        # upperbound will either be the next highest bracket OR the rest of the income
        upper_bound = taxRateLists[counter+1][0]
        if salary < upper_bound:
            upper_bound = salary

        tax_amt = (upper_bound-lower_bound)*(taxRateLists[counter][1])

        counter += 1
        tax_subs.append(tax_amt)
        temp -= (upper_bound-lower_bound)

    # no upper bound if highestBrack is true
    if highestBrack==True:
        temp*=taxRateLists[len(taxRateLists) - 1][1]
        tax_subs.append(temp)

    # return tax_subs = list of tax deducations for each bracket
    return tax_subs

# list of state and federal tax rates
# [[lower_bound, tax_rate]]
stateTaxRates = [[0, 0.014], [20000, 0.0175], [35000, 0.035], [40000, 0.05525], [75000, 0.0637], [500000, 0.0897], [1000000, 0.1075]]
fedTaxRates = [[0, 0.1], [11000, 0.12], [44725, 0.22], [95375, 0.24], [182100, 0.32], [231250, 0.35], [578125, 0.37]]

# retrieve total money
x = input('Enter your salary (pre-tax): ').replace(",", "").replace("$", "")
print()

contributionLimit = 0.1 * float(x)            # assuming a person donates 10% of their income
temp = salary = float(x) - contributionLimit
highestBrack = False

stateTaxSubs = calcTaxRates(temp, salary, stateTaxRates, highestBrack=False)
fedTaxSubs = calcTaxRates(temp, salary, fedTaxRates, highestBrack=False)
ficaAmt = 0.0765 * salary

fedTax = sum(fedTaxSubs)
stateTax = sum(stateTaxSubs)
postTax = salary - fedTax - stateTax - ficaAmt
monthlySalary = postTax/12.0
print(f"Your federal income taxes are approximately ${fedTax:,.2f}")
print(f"Your state income taxes are approximately ${stateTax:,.2f}")
print(f"Your FICA taxes are approximately ${ficaAmt:,.2f}")

print(f"\nYour estimated take-home pay is ${postTax:,.2f}")
print(f"Therefore, your estimated take-home pay each month is ${monthlySalary:,.2f}")

needs = postTax*(0.5)
wants = postTax*(0.3)
savings = postTax*(0.2)

print(f'\nYou should be spending ${needs:,.2f} on your needs, ${wants:,.2f} on your wants, and ${savings:,.2f} on your savings')

mNeeds = needs/12.0
mWants = wants/12.0
mSavings = savings/12.0

print(f'\nOn a montly basis, you should be spending ${mNeeds:,.2f} on your needs, ${mWants:,.2f} on your wants, and ${mSavings:,.2f} on your savings')
