''' Script for counting n-grams in a corpus & saving it in json format.

I may later add another, custom text format to cut down the file size
as much as possible, for better serving over the web.

This is in Python rather than JS simply because I prefer Python for
string/text handling stuff like this.  This is a bit unusual for a mostly
JS project, I guess, but I've at least kept it dependency-free
so you don't have to worry about installing npm dependencies AND 
pip dependencies.'''

from collections import Counter
import json
import sys

def n_grams(corpus,n=4,backoff=True):
    ''' Return n-gram counts for n=4.  

    If backoff=True (as is the case by default), also count all
    n-grams for smaller n, down to n=1, for possible use with backoff 
    and/or linear interpolation and/or something else.'''
    counts = Counter([corpus[i:i+n] for i in range(len(corpus)-n+1)])
    if backoff:
        for N in range(1,n):
            counts.update([corpus[i:i+N] for i in range(len(corpus)-N+1)])
    return counts

def create_data(file_in,n=4):
    with open(file_in,"r") as f:
        contents = f.read()
    counts = n_grams(contents,n)
    return json.dumps(dict(counts))

if __name__=="__main__":
    try:
        print(create_data(sys.argv[1],n=int(sys.argv[2])))
    except:
        print("Usage: python3 count_grams.py file_in n > file_out")
        print("Example:\n  python3 count_grams.py some_corpus.txt 4 > ngram_counts.json")
        sys.exit()
