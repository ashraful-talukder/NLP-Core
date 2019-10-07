import random

paragraph = """Global warming is a gradual increase in the temperature of the earth surface and atmosphere all around the world. It is caused due to the greenhouse effect of increased level of green house gases such as carbon dioxide, CFCs, etc. There are various types of pollutants also which involved in increasing the atmospheric temperature of the earth. Increasing use of fossil fuels by the people and deforestation is increasing carbon dioxide emissions which trap heat and cause greenhouse effect.

Water vapor is also a significant greenhouse gas which is not directly produced by humankind but involve in global warming hugely. A slight increase in the level of CO2 causes marked increase in earth temperature. Green house gases absorb and re-radiate infrared radiations which ultimately cause green house effect. Because of deforestation, CO2 is not absorbed well and remain in the atmosphere for long time and trap heat."""

n = 5
ngrams = {}

#creating n-grams
for i in range(len(paragraph)-n):
    gram = paragraph[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(paragraph[i+n])

#testing n-gram model
currentGram = paragraph[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result+= nextItem
    currentGram = result[len(result)-n:len(result)]
print(result)