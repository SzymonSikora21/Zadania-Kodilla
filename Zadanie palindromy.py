def palindrome_word(args):
    reversed_word = args[::-1]
    if args == reversed_word:
        print(f"Word {args} is a palindrome")
    else:
        print(f"Word {args} isn't a palindrome")

palindrome_word("kajak")
