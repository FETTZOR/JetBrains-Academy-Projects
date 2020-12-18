import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", default=False)
parser.add_argument("-p", "--principal", type=float)
parser.add_argument("-per", "--periods", type=float)
parser.add_argument("-i", "--interest", type=float)
parser.add_argument("-pay", "--payment", type=float)
args = parser.parse_args()


if args.type == 'annuity' and len(sys.argv) == 5 and not args.payment:
    loan_principal = args.principal
    number_of_periods = args.periods
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    a = loan_principal * (i * ((1 + i) ** number_of_periods) / (((1 + i) ** number_of_periods) - 1))
    a_converted = math.ceil(a)
    print(f'Your monthly payment = {a_converted}!')
    overpayment = a_converted * number_of_periods - loan_principal
    print(f'Overpayment = {math.ceil(overpayment)}')

elif args.type == 'annuity' and len(sys.argv) == 5 and not args.principal:
    annuity_payment = args.payment
    number_of_periods = args.periods
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    p = annuity_payment / (i * ((1 + i) ** number_of_periods) / (((1 + i) ** number_of_periods) - 1))
    p_converted = math.floor(p)
    print(f'Your loan principal = {p_converted}!')
    overpayment = math.ceil(annuity_payment * number_of_periods) - p_converted
    print(f'Overpayment = {math.ceil(overpayment)}')

elif args.type == 'annuity' and len(sys.argv) == 5 and not args.periods:
    loan_principal = args.principal
    monthly_payment = args.payment
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    log = monthly_payment / (monthly_payment - i * loan_principal)
    n = math.log(log, (1 + i))
    overpayment = math.ceil(n) * monthly_payment - loan_principal
    n_converted = divmod(n, 12) [0]
    n_converted2 = divmod(n, 12) [1]
    n_converted_year = math.ceil(n_converted)
    n_converted_month = math.ceil(n_converted2)

    if n_converted_year > 1 and n_converted_month == 0:
        print(f'It will take {n_converted_year} years to repay this loan!')
    elif n_converted_month == 12:
        n_converted_year = n_converted_year + 1
        print(f'It will take {n_converted_year} years to repay this loan!')
    else:
        print(f'It will take {n_converted_year} years and {n_converted_month} months to repay this loan!')
    print('Overpayment =', math.ceil(overpayment))
elif args.type == 'diff' and len(sys.argv) == 5 and not args.payment:
    loan_principal = args.principal
    P = loan_principal
    periods = args.periods
    n = int(periods)
    interest = args.interest
    m = args.periods
    i = interest / (12 * 100)
    listik = []
    a = 0
    overpayment = loan_principal
    for f in range(n):
        d = P / n + i * (P - (P * (m - 1) / n))
        listik.append(math.ceil(d))
        overpayment = math.floor(overpayment - d)
        m = m - 1
    listik.reverse()
    for char in listik:
        a = a + 1
        print(f'Month {a}: payment is {char}')
    overpayment_converted = abs(overpayment)
    print()
    print('Overpayment = ', overpayment_converted)

else:
    print('Incorrect parameters.')
