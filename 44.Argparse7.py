print("Argparse 7: action=count, defualt, and current file name print used")
print("-------------------------------------------------------------------")
#prints based on number of occurances of specific option like -v, -vv for 2, -vvv etc
#also like --verbose --verbose for 2 in comand argument.
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("n1",help="enter number 1",type=int)
parser.add_argument("n2",help="enter number 2",type=int)
parser.add_argument("-l","--level",action="count",help="increase level of output.",default=0)
args=parser.parse_args()
answer=args.n1**args.n2
if args.level>=2:
    print(f"File Name='{__file__}'")
    print("{} when squared with {}={}".format(args.n1,args.n2,answer))
elif args.level>=1:
    print(f"square of {args.n1} with {args.n2} is {answer}")
else:
    print("Sqaure=",answer)

