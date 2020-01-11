# lingthing ⚡

A library for n-gram-based character-level language modeling in JavaScript,
intended for use in the browser.  Also an anagram for "lightning".

A json file containing counts of n-grams in some training corpus can be
created using the script `scripts/count_grams.py` (or you can use the
example based on the Lancaster-Oslo-Bergen corpus, in 
`scripts/LOB_ngrams.json`).  This can then be
used, along with the `lingthing.log_prob` function, to estimate
the (log) probability of a string (with Laplace smoothing applied, and
possibly other smoothing options in the future).

This package is a work-in-progress.

## Usage
In node:
```javascript
const lt = require('lingthing');
const fs = require('fs');

let counts = JSON.parse(fs.readFileSync('scripts/LOB_ngrams.json'));

test_sentence = "Test sentence."
info = lt.corpus_info(counts)
log_probability = lt.log_prob(test_sentence,counts,"laplace",
    info.n,info.d,info.N);

console.log("Probability of sentence '" + test_sentence + "' is " 
    + Math.exp(log_probability));
```

## Building
To build the browser-friendly distribution, run `npm install` to
install dev-dependencies, and then run `npm run-script browser` to build
the actual file (which will appear in the `dist` directory).

## Related packages / alternatives
The most relevant existing npm packages I can find are:

`markovian-nlp`: Word-level language modeling, apparently mostly focused on text generation.

`languagemodel`: Unigram-based cross-lingual language model.

`kn`: Word-level model using Kneser-Ney smoothing, which is probably the closest to what I'm looking for, but it doesn't look very convenient to use.

`natural`: Lots of general NLP stuff, including counting word n-grams, but no character-level n-gram language modeling specifically.

None of these packages does quite what I want (probably for a good
reason).
