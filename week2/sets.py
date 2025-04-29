set1 = set()
set2 = set()

n = 5
n1 = 5

while n != 0:
    inp = int(input('Enter a number: '))
    set1.add(inp)
    n -=1

while n1 != 0:
    inp = int(input('Enter a number: '))
    set2.add(inp)
    n1 -=1


set3 = set1 & set2
print(f'Common nums: {set3}')