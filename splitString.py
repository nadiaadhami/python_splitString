# splitstring.py

testWords = {"","a","rock","rockstar","arockstar","rockstartar","arockstartarzebra","google","googlerockstar","googlerocks","good","zebrarock"};
dict = {"a","rock","star","tar","zebra","google"}

def splitToTwoWords(word):
    words = set()
    if len(word)  == 0:
        return words
    if len(word) == 1:
        if word in dict:
            words.add(word)
            return words
    for i in range(0,len(word)):  
        s1 = word[0:i+1]
        s2 = word[i+1:]
        if s1 in dict and s2 in dict:
            words.add(s1)
            words.add(s2)
            break
    return words

def splitToTwoWordsRecursive(word):
    words = set()
    if len(word) == 0:
        return words
    if word in dict:
        words.add(word)
        return words
    for i in range(0, len(word)):
        s1 = word[0:i+1]
        s2 = word[i+1:]
        set1 = splitToTwoWordsRecursive(s1)
        set2 = splitToTwoWordsRecursive(s2)
        if (len(set1) > 0 and len(set2) > 0):
            set1.add(set2)
            return set1
    return words
    

def wordFinder(testWords):
    words = set
    for word in testWords:
        words = splitToTwoWords(word)
        if len(words) == 0:
            print(word, " - no match found in the dictionary")
        else:
            print(word," :")
            for w in words:
                print (" ",w)

def recursiveWordFinder(testWords):
    for word in testWords:
        words = splitToTwoWordsRecursive(word)
        print(words , " =>")
        if words == None or len(words) == 0:
            print(" - no match found")
        else:
            for w in words:
                print(w)


wordFinder(testWords)
print("========")
wordFinder(testWords)
