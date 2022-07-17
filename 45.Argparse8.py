print("Argparse 8: print output in desired language")
print("--------------------------------------------")
import argparse
parser=argparse.ArgumentParser(description="give arguments first manditory language is optional.",epilog="Thank You.")
parser.add_argument("name",help="enter full name")
parser.add_argument("-e","--english",help="output in english.",action="store_true")
parser.add_argument("-s","--spanish",help="output in spanish.",action="store_true")
args=parser.parse_args()
if args.english:
    print(f"Full Name Is={args.name}")
elif args.spanish:
    print(f"nombre completo es={args.name}")
else:
    print(args.name)