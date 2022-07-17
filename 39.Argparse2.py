#by default command line arguments are string , its required to type cast or provide type for entering.add_argument

print("Argparse2")
print("---------")
print("multiple arguments")
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("n1",help="enter first number",type=int)
parser.add_argument("n2",help="enter second number",type=int)
args=parser.parse_args()
sum=args.n1+args.n2
print("Sum=",sum)