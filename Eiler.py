# Первая задача эйлера!
sum = 0
for i in range(1000):

    if (i % 3) == 0 and i // 3 != 0 or (i % 5) == 0 and i // 5 != 0:
        sum += i
print(sum)

def binary_search(data, item):
    low = 0
    print(low)
    high = len(data) - 1
    print(high)
    while low <= high:
        mid = int((low + high) / 2)
        print(mid)
        guess = data[mid]
        print(guess)
        if guess == item:
            return guess
        if guess > item:
            print('high до if: ', high)
            high = mid - 1
            print('high после if: ', high)
            return high
        else:
            print('low до else: ', low)
            low = mid + 1
            print('low после else: ', low)
            return low
    return None

list = []
for i in range(101):
    list.append(i)

print(list)
print(binary_search(list, 48))