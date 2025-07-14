def longest_word(word):

    count = 0

    word_list = word.split(" ")

    for n in word_list :

        if len(n) > count :

            count = len(n)

            longest = n

    return longest

print(longest_word("This Sentence for testing the function"))
