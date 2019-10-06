import nltk

sentence = "Bangladesh got its independence in 1971"

words = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words) #draw as namedEntity as a tree
namedEnt.draw() #represent the tree