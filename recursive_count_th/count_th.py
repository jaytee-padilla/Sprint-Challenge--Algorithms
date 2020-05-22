'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0

    # each iteration of the recursion removes the first element of whatever's currently stored in word
    # in other words, everytime recursion occurs, the value of the word parameter is shortened character by character
    # if the first two elements of the word parameter is equal to 'th', then add to the count of occurrences of 'th'
    if word[0] + word[1] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

# print(count_th("thuwu"))
