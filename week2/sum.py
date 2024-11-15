inputList = []
sum = 0
n = 4

while n !=0:
    inputList.append(int(input(f'Enter num {n}:')))
    n -=1
    
for i in inputList:
    sum += i

print(f'List: {inputList}' )
print(f'Sum: {sum}')
