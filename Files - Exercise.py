# Read the first two lines from file1.txt
with open("file1.txt", "r") as f1:
    line1 = f1.readline()
    line2 = f1.readline()
# Write the two lines into file2.txt
with open("file2.txt", "w") as f2:
    f2.write(line1)
    f2.write(line2)
# Read file2.txt and print the contents
with open("file2.txt", "r") as f2:
    contents = f2.read()
    print(contents)
