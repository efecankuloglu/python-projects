import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--interest")
parser.add_argument("--periods")
parser.add_argument("--payment")

args = parser.parse_args()

parameters = [args.type, args.principal, args.interest, args.periods]

if len(parameters) < 4:
    print("Incorrect parameters")

if args.type == "diff":
    if args.payment != None:
        print("Incorrect parameters")
    elif args.interest == None:
        print("Incorrect parameters")
    else:
        total = 0
        for i in range(1, int(args.periods) + 1):
            monthly = (int(args.principal) / int(args.periods)) + (float(args.interest) / (12 * 100)) * (int(args.principal) - (int(args.principal) * (i - 1) / int(args.periods)))
            print(f"Month {i}: payment is {math.ceil(monthly)}")
            total += math.ceil(monthly)
        print(f"\nOverpayment = {total - int(args.principal)}")
elif args.type == "annuity":
    if args.interest == None:
        print("Incorrect parameters")
    elif args.payment == None:
        interest = float(args.interest) / (12 * 100)
        payment = int(args.principal) * (interest * ((1 + interest) ** int(args.periods))) / (((1 + interest) ** int(args.periods)) - 1)
        print(f"Your annuity payment = {math.ceil(payment)}!")
        print(f"Overpayment = {math.ceil(math.ceil(payment) * int(args.periods) - int(args.principal))}")
    elif args.principal == None:
        interest = float(args.interest) / (12 * 100)
        principal = int(args.payment) * (((1 + interest) ** int(args.periods)) - 1) / (interest * ((1 + interest) ** int(args.periods)))
        print(f"Your loan principal = {int(principal)}!")
        print(f"Overpayment = {math.ceil(int(args.periods) * int(args.payment) - principal)}")
    elif args.periods == None:
        interest = float(args.interest) / (12 * 100)
        periods = math.ceil(math.log(int(args.payment) / (int(args.payment) - interest * int(args.principal)), (1 + interest)))
        if periods < 12:
            print(f"It will take {periods} months to repay this loan!")
            print(f"Overpayment = {periods * int(args.payment) - int(args.principal)}")
        elif periods % 12 == 0:
            print(f"It will take {periods // 12} years to repay this loan!")
            print(f"Overpayment = {periods * int(args.payment) - int(args.principal)}")
        else:
            print(f"It will take {periods // 12} years and {periods % 12} months to repay this loan!")
            print(f"Overpayment = {periods * int(args.payment) - int(args.principal)}")
else:
    print("Incorrect parameters")
