import nltk

paragraph = """Thank you all so very much. Thank you to the Academy, thank you to all of you in this room. I have to congratulate the other incredible nominees this year for their unbelievable performances. The Revenant was the product of the tireless efforts of an unbelievable cast and crew I got to work alongside. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your fierce talent on screen can only be surpassed by your friendship off screen. To Mr. Alejandro Innaritu, as the history of cinema unfolds, you have forged your way into history these past 2 years... thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency…my entire team. I have to thank everyone from the very onset of my career…to Mr. Jones for casting me in my first film to Mr. Scorsese for teaching me so much about the cinematic art form. To my parents, none of this would be possible without you. And to my friends, I love you dearly, you know who you are.

And lastly I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much."""

words = nltk.word_tokenize(paragraph)
tagged_word = nltk.pos_tag(words)

word_tags = []
for tw in tagged_word:
    word_tags.append(tw[0]+"_"+tw[1])

tagged_paragraph = " ".join(word_tags)