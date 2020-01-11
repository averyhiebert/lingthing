# lingthing

A library for n-gram-based character-level language modeling in JavaScript,
intended for use in the browser.

A json file containing counts of n-grams in some training corpus can be
created using the script `scripts/count_grams.py`.  This can then be
used, along with the `lingthing.log_prob` function, to estimate
the (log) probability of a string (with Laplace smoothing applied, and
possibly other smoothing options in the future).

This package is a work-in-progress.

## Related packages / alternatives
The most relevant existing npm packages I can find are:

`markovian-nlp`: Word-level language modeling, apparently mostly focused on text generation.

`languagemodel`: Unigram-based cross-lingual language model.

`kn`: Word-level model using Kneser-Ney smoothing, which is probably the closest to what I'm looking for, but it doesn't look very convenient to use.

`natural`: Lots of general NLP stuff, including counting word n-grams, but no character-level n-gram language modeling specifically.

None of these packages does quite what I want (probably for a good
reason).
