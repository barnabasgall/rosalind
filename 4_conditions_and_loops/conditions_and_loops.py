# Problem
# Giveb: Two positive integers a and b (a<b<100000)
#Return: The sum of all odd integers from a through b, inclusively

a = 4556
b = 8796
c = 0

# check if a is even
if (a % 2)==0:
    a = a + 1
else:
    a = a


while a < b:
    c = c + a
    a = a + 2
print(c)

