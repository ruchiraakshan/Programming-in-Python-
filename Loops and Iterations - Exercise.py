#Question 1

val = int(input())
for x in range (0, val):
    for y in range(val):
      print('*',end='')
    print()    

#Question 2

#i = int(input())
#j = 5 # fix the code (1) 
#while (j <= (i/j)):
    #if not(i%j): 
        #print("not a prime")
        #continue # fix the code (2)
    #j = j + 2 # fix the code (3)
#if (j > i/j): 
    #print ("prime")

i = int(input())
j = 2 # fix the code (1) 
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        is_prime = False
        break # fix the code (2)
    j = j + 1 # fix the code (3)
if (j > i/j): 
    print ("prime")    