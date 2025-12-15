for counter in [1,2,3,4,5]:
    print ("Now the counter is =", counter)

total = 0
for counter in range(0,101,2):
    total = total + counter
print('total = '),
print(total)


num = 5
while (num !=0) :
    print ('Hello World!')
    num = num - 1

#break(Stops the loop completely)
print("Example of break:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 4:
        print("Breaking at:", num)
        break  # loop stops here
    print("Number:", num)
print("Loop ended\n")

#continue(Skips current iteration, continues loop)
print("Example of continue:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", num)
print("Loop ended")

