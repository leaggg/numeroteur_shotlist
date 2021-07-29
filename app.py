# Adds numbers to shotlist

shotlist = open("myshotlist.txt", "r")
new_shotlist = open("newshotlist.txt", "w")
n = 0
for line in shotlist.readlines():
    line = line.replace("\n", "")
    if line.startswith("."):
        n = n+1
        newline = str(n) + line
        print(newline)
        new_shotlist.write(newline)
    else:
        print(line)
        new_shotlist.write(line)
