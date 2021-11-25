# Problem:
# Given A dile containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file

f = open('sample.txt','r')
w = open('output.txt','w')
a = 0
for line in f:
    a = a + 1
    if (a % 2)==0:
        w.write(line)
