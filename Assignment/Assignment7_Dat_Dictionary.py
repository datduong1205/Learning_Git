# Name: Dat , ID: 100886108

#Program2: dictionary.py

def main(keywordsList):
    dictionary = dict()
    for keyword in keywordsList:
        if keyword in dictionary:
            dictionary[keyword] += 1
        else:
            dictionary[keyword] = 1
    
    return dictionary

keywordsList = ["and", "del", "global", "while", "for", "in", "else", "print", "return", "import", "if", "elif", "break", "continue", "and", "and", "global", "and", "or", "raise"]

dictionary = main(keywordsList)
SortedDictionary = dict(sorted(dictionary.items(),key= lambda item: item[1], reverse=True))

print("Keyword_name".ljust(15), "Count\n")
for key, value in SortedDictionary.items():
    print(key.ljust(15), value)