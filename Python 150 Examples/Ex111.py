import csv

file = open("Books.csv", 'w')
record = "To kill a mockingbird,Harper Lee,1960\n"
file.write(str(record))
record="The Great Gatsby,F. Scott Fitzgerald,1922\n"
file.write(str(record))
record="The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
file.write(str(record))
record="Pride and Prejudice,Jane Austen,1813\n"
file.write(str(record))
record="A Brief History of Time,Stephen Hawking,1988\n"
file.write(str(record))
file.close()