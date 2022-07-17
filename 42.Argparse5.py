print("Argparse 5")
print("----------")
print("increase level of output with verbosity")
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("square",help="prints square of the number.",type=int)
parser.add_argument("-v",help="provide detaild output",action="store_true")
args=parser.parse_args()
answer=args.square**2
if args.v:
    print(f"The Square of the {args.square} is equals to {answer}")
else:
    print("Square=",answer)