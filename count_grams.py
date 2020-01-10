''' Script for counting n-grams in a corpus & saving it in json format.

I may later add another, weirder format to cut down the file size
as much as possible.  It depends.

Why is this in Python and not JS if the rest of the project is going
to be JS?  I don't know, I guess I'm just a creature of habit.'''
from collections import Counter
import json

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


def create_data(file_in,file_out="ngrams.json",n=4):
    with open(file_in,"r") as f:
        contents = f.read()
    counts = n_grams(contents,n)
    with open(file_out,"w") as f:
        json.dump(dict(counts),f)
    return counts

# TODO: Replace main with a good user-friendly script with params etc.
if __name__=="__main__":
    counts = create_data("texts/LOB_nomarkup.txt")

