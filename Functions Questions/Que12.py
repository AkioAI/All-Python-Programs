# 12. Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(str):
    if str[:]==str[::-1]:
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} not a palindrome.")
str="madam"
palindrome(str)