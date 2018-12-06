https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction: "tokenizing strings and giving an integer id for each possible token, for instance by using white-spaces and punctuation as token separators."


The default regexp selects tokens of 2 or more alphanumeric characters (punctuation is completely ignored and always treated as a token separator).


SVM classifier can act as a validation signal on the preprocessing. we will try the best preprocessing pipeline with the NN later.





Results:

tfidf only, 100 feats, svm: Accuracy:  0.8212461695607763

tfidf + 23 grammar, svm: Accuracy:  0.54902962206333

just 23 grammar: Accuracy:  0.4034729315628192
Accuracy:  0.5648621041879469


23 grammar + 7ary sequences:
  Accuracy:  0.3958120531154239
  number of seq features: 1600

sequences
  analogous to heart patterns, except not human engineered (get citation)

pretty poor results for grammatical. let's look at where it's getting wrong, and look at how the author distributions are different


could just punt and let the NN try to use all features correctly


It may be that the authors have few differentiators - many sentences could plausibly come from distro A or distro B.

tried standardization, improved significantly, but still not great.
