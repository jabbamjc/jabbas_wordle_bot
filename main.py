import os
import numpy as np

def selectFiveLetterWords():
    #finds all 5 letter words in the official scrabble dictionary and saves them to a seperate file in alphabetical order
    scrabbleWords = open(os.getcwd()+"\\scrabble_dictionary.txt", "r")
    fiveLetterWords = open(os.getcwd()+"\\five_letters.txt", "w")
    for line in scrabbleWords:
        if (len(line) == 6):
            fiveLetterWords.write(f"{line}")

def commonLetters():
    #counts how many times each letter appears and saves to a file in ascending order
    scores = [{"char":'', "count":0} for i in range(26)]
    fiveLetterWords = open(os.getcwd()+"\\five_letters.txt", "r")
    for line in fiveLetterWords:
        for char in line.strip():
            index = ord(char) - 97
            scores[index]["char"] = char
            scores[index]["count"] += 1

    scores.sort(key=lambda d : d["count"])
    letterStats = open(os.getcwd()+"\\letterStats.txt", "w")
    for i in range(26):
        letterStats.write(f"{scores[i]['char']} : {scores[i]['count']:04}\n")

def mostPopularMethod():
    #assigns each word a value based on how popular the letters its composed of are
    #not very useful since words with the most S's are deemed best
    letterScores = []
    letterStats = open(os.getcwd()+"\\letterStats.txt", "r")
    count = 1
    for letter in letterStats:
        char = letter[0]
        score = count
        letterScores.append({"char":char, "score":score})
        count += 1
    letterScores.sort(key=lambda l : l["char"])

    wordScores = []
    fiveLetterWords = open(os.getcwd()+"\\five_letters.txt", "r")
    for line in fiveLetterWords:
        wordScore = 0
        for char in line.strip():
            wordScore += letterScores[ord(char) - 97]["score"]
        wordScores.append({"word":line.strip(), "score":wordScore})
    wordScores.sort(reverse=True, key=lambda w : w["score"])

    fiveLetterWords = open(os.getcwd()+"\\mostPopularMethod.txt", "w")
    for word in wordScores:
        fiveLetterWords.write(f"{word['word']} : {word['score']:03}\n")

def mostPopularUniqueMethod():
    #assigns each word a value based on both, how popular the letters its composed of are and how many unique letters it contains
    letterScores = []
    letterStats = open(os.getcwd()+"\\letterStats.txt", "r")
    count = 1
    for letter in letterStats:
        char = letter[0]
        score = count
        letterScores.append({"char":char, "score":score})
        count += 1
    letterScores.sort(key=lambda l : l["char"])

    wordScores = []
    fiveLetterWords = open(os.getcwd()+"\\five_letters.txt", "r")
    for line in fiveLetterWords:
        wordScore = 0
        uniqueness = len(np.unique(list(line.strip())))
        for char in line.strip():
            wordScore += letterScores[ord(char) - 97]["score"]
        wordScores.append({"word":line.strip(), "score":wordScore*uniqueness})
    wordScores.sort(reverse=True, key=lambda w : w["score"])

    fiveLetterWords = open(os.getcwd()+"\\mostPopularUniqueMethod.txt", "w")
    for word in wordScores:
        fiveLetterWords.write(f"{word['word']} : {word['score']:03}\n")

def calculateNextWord(previousResult, newGame = False):
    allWords = []
    if newGame:
        mpu = open(os.getcwd()+"\\mostPopularUniqueMethod.txt", "r")
        for w in mpu:
            currentWord = w[0:5]
            allWords.append(currentWord)

    while True:
        previousResult = input()
        for i in range(5):
            letter = previousResult[i * 2]
            position = previousResult[i * 2 + 1]

            print(len(allWords))
            for word in allWords:
                #word.strip()
                #print(word)
                
                if position == "0":
                    if letter in word:
                        allWords.remove(word)

                if position == "1":
                    if word[i] == letter:
                        allWords.remove(word)
                        
                    if letter not in word:
                        allWords.remove(word)

                if position == "2":
                    if word[i] != letter:
                        allWords.remove(word)

        nextWord = allWords[0]
        print(nextWord)
        #return nextWord

if __name__ == '__main__':
    #selectFiveLetterWords()
    #commonLetters()
    #mostPopularMethod()
    #mostPopularUniqueMethod()
    calculateNextWord("a1r0o0s0e0", True)