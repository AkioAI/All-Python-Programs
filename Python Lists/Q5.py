# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def main(lst):
    count = 0
    for word in lst:
        if len(word) > 2 and word[0] == word[-1]:
            count+=1
    return count
lst = ['abc', 'xyz', 'aba', '1221']
print(main(lst))