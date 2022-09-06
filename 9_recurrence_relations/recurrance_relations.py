from importlib.metadata import packages_distributions


a = int(input('First number\n'))
b = int(input('Second number\n'))

pairs = 1
history = []

for i in range(1,a+1):
    if i>2:
        pairs = pairs + (history[i-3]*b)
    history.append(pairs)

print(pairs)