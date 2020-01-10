# js-ngram-lm

A library for n-gram character-level language models in JavaScript (with
associated Python script for some reason).

The most relevant existing npm packages I can find are:

markovian-nlp: Is word-level and mostly focused on text generation.
languagemodel: Also word-level.
kn: Uses Kneser-Ney smoothing, but doesn't look super convenient to use.
natural: General NLP stuff, including n-grams, but no n-gram language models.

None of these does quite what I want, so I'm making my own library.
