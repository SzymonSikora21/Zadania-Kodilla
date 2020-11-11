def palindrome_word(args):
    reversed_word = args[::-1]
    if args == reversed_word:
        return True
    else:
        return False

print(palindrome_word("word"))
