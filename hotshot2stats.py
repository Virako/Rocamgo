from hotshot import stats
import argparse


parser = argparse.ArgumentParser(description='Transform hotshot to pstat.')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

if args.input and args.output:
    try:
        st = stats.load(args.input)
        st.dump_stats(args.output)
        print "Done. "
    except IOError:
        print "File not exist. "
