import spacy
nlp = spacy.load('en_core_web_md')
'''If this is replaced with en_core_web_sm, the following output is generated:
"The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive 
tensors. You can always add your own word vectors, or use one of the larger models instead if available."
The similarity levels are completely different and don't make sense conceptually.
'''

# Code extract 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
'''I found it interesting that banana was more similar to monkey than it was to cat.
It seems that NLP considers the association between the topics. However, cat and monkey 
are most similar of these words, probably because they are both animals (and both mammals).'''

# Code extract 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Trying with my own example words
tokens = nlp("pancakes waffles breakfast maple bacon flat")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
'''One interesting note is that waffles and pancakes are practically at the maximum
similarity and their similarity indexes with the other words is identical even when
in practice, it might make sense for them to be different. For example, flat should
probably be more similar to pancake than waffle since pancakes are flat and are 
associated with the phrase "flat as a pancake". However, they are the same.'''

# Code extract 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
