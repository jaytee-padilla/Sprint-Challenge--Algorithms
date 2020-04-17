'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return "recursion done"
    else:
        return count_th(word[1:])

print(count_th("thuwu"))
