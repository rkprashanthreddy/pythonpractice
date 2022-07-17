print("Argparse 6: increasing verbosity levels")
print("---------------------------------------")
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("fullname",help="enter full name")
parser.add_argument("-level",help="add levels",choices=[0,1,2],type=int) #choices to choose only from.
args=parser.parse_args()
if args.level==1:
    print(f"You have entered your full name as {args.fullname}, thank you for the details.")
elif args.level==2:
    print(f"Your Full Name is {args.fullname}, thank you for the details, hope {args.fullname} you will have nice day.")
else:
    print(f"Fullname={args.fullname}")