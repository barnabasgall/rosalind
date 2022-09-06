n = int(input('First number\n')) # months
m = int(input('Second number\n')) # months lived per rabbit

pairs = 1
history = []
birth_history = []

for i in range(1,n+1):
    history.append(pairs)
    if i >1:
        pairs = pairs + (history[i-1])
        birth_history.append(history[i-1])
    print(history)
    if i >= m:
        pairs = pairs - (birth_history[i-m])
    print(birth_history)

print(pairs)