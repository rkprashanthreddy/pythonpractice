print("Argparse 4")
print("----------")
print("action to store true value, by default its false.")
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--echo")  #for this if we say --echo error rises , we need to say --echo <argument>
parser.add_argument("--echo2",action="store_true") #for this --echo2 also works as true.
args=parser.parse_args()
if args.echo:
    print("Argument Provided.")
else:
    print("Argument Not Provided.")

if args.echo2:
    print("Argument Provided.")
else:
    print("Argument Not Provided.")