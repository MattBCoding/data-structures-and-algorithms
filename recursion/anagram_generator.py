# anagram generator using recursion for a given string
# this has a time complexity of O(n!) and a space complexity of O(n!)
# where n is the number of characters in the string
# n! is factorial n, which is n * (n-1) * (n-2) * ... * 1
# this is the slowest form of algorithm.


def anagram_generator(input_string):
    # base case - if the string is only one character
    if len(input_string) == 1:
        return input_string[0]

    # recursive case
    # create an empty list to store the anagrams
    collection = []

    # find all anagrams of the substring from the second character onwards
    # eg if the string is 'abcd', the substring is 'bcd'
    # so find all anagrams of 'bcd'
    substring_anagrams = anagram_generator(input_string[1:])

    # iterate over each substring
    for substring in substring_anagrams:
        # iterate over each index of the substring, from 0 to len(substring)
        for index in range(len(substring) + 1):
            # create a copy of the substring anagram
            anagram = str(substring)
            copy = anagram[:index] + input_string[0] + anagram[index:]
            # append the anagram to the collection
            collection.append(copy)

    # return the collection
    return collection


# test the function
my_string = "abcd"
result = anagram_generator(my_string)
print(result)
assert result == [
    "abcd",
    "bacd",
    "bcad",
    "bcda",
    "acbd",
    "cabd",
    "cbad",
    "cbda",
    "acdb",
    "cadb",
    "cdab",
    "cdba",
    "abdc",
    "badc",
    "bdac",
    "bdca",
    "adbc",
    "dabc",
    "dbac",
    "dbca",
    "adcb",
    "dacb",
    "dcab",
    "dcba",
]
