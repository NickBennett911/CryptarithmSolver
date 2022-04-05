from itertools import permutations
import time

def CreateUniqueLettersList(words):
    '''
    Takes in a list of words and creates a list of all the unique letters
    :param words: list of strings
    :return: list of unique letters from all the words
    '''
    letters = []
    for word in words:
        for letter in word:     # go over all the letters in the word
            if letter not in letters:   # if the letter is not already in the list then add it
                letters.append(letter)
    return letters

def CreateLookUp(letters, numbers):
    '''
    creates a look up dict from the letters and numbers given (letters are the keys)
    :param letters: what we want as the keys
    :param numbers: what we want as the corresponding value
    :return: look up dictionary
    '''
    table = {}
    for i, n in enumerate(letters):
        table[n] = numbers[i]   # add entry into table with letter as key and number as value
    return table

def WordToNum(word, lookup):
    '''
    Converts a word to a number using a look up table
    :param word: the word we want to convert
    :param lookup: the lookup table for the current permutation
    :return: the number associated with it
    '''
    output = ""
    for letter in word:
        output += str(lookup[letter])   # get the number by using  the letter to lookup
    return int(output)

def IsValuePermutation(perm_nums, words, letters, LeadingZeros):
    '''
    Check to see if permutation is a valid one given the words and unique letters
    :param perm_nums: permutation being checked i.e. a list of numbers
    :param words: a list of our words that was given to us
    :param letters: the unique letters for the given words
    :param LeadingZeros: tells us if we are allowing leading zeros or not
    :return: True if possible, False otherwise
    '''
    lookup = CreateLookUp(letters, perm_nums)   # create our lookup table to be passed
    WordsAsNums = []
    for word in words:
        num = WordToNum(word, lookup)
        if LeadingZeros != "Yes":
            if len(str(num)) < len(word):   # this means we had a leading zero so we return false
                return (False, [])
        WordsAsNums.append(num)

    result = 0
    for i in range(len(WordsAsNums)-1): # add up our results except for the last
        result += WordsAsNums[i]

    if result == WordsAsNums[-1]:   # if our addition matches then return true
        return (True, WordsAsNums)
    return (False, [])


if __name__ == '__main__':
    inp = input("Input at least 3 words all separated by once space: ")
    inp = inp.split(" ")
    isLeadingZeros = input("Allow for leading zeros? (Yes/No): ")

    letters = CreateUniqueLettersList(inp)  # create the unique letters from the input given

    if len(letters) > 10:       # make sure there arent too many letters
        print("too many unique letters")

    start = time.time()

    # create all possible permutations from the unique letters
    possible = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(letters)))

    solutions = []  # keep track of solutions
    for perm in possible:
        # if permutation creates a series of numbers that corresponds with the letters that solves the problem
        # then we know the permuation is a possible solution
        IsValid, Solution = IsValuePermutation(perm, inp, letters, isLeadingZeros)
        if IsValid:
            solutions.append((Solution, perm))

    end = time.time()

    print("---------- DONE ----------")
    print(str(len(solutions)) + " solution(s) found in " + str(end-start) + " seconds: ")

    # print the solutions
    for i, solution in enumerate(solutions):
        output = "Solution " + str(i) + ": "
        for i, num in enumerate(solution[0]):
            output += str(num)
            if i < len(solution[0])-2:
                output += " + "
            elif i == len(solution[0])-2:
                output += " = "
        output += "\n     Letters/numbers: " + str(CreateLookUp(letters, solution[1]))
        print(output)
