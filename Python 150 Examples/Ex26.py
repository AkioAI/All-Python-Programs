word=input("Enter a word: ")
first=word[0]
length=len(word)
rest=word[1:length]
if first!='a' and first!='e' and first!='i' and first!='o' and first!='u':
    new_word=rest+first+'ay'
else:
    new_word=rest+first+'way'
print(new_word.lower())
