subjects=["english","physics","chemistry","biology","maths"]
print(subjects)
dislike=input("Which subject you dislike: ")
getrid=subjects.index(dislike)
del subjects[getrid]
print(subjects)
