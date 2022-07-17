#recomended module for command line parsing in python

print("Command line arguments with argparse")
print("------------------------------------")
print("positional arguments are manditory to provide, if we dont provide rises error.")
print("single argument")
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("arg1",help="prints the value entered in command line.")
args=parser.parse_args()
print(args.arg1)

