import MyText

variable = "An apple a day keeps the doctor away"
print(f"Text: {variable}")
print(f"Number of words: {MyText.wordsCount(variable)}")
print(f"Words from longest: {MyText.longToShort(variable)}")
print(f"Words ordered alphabetically: {MyText.alphabetical(variable)}")