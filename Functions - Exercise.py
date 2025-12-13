# Write a python3 function sqr( n ) that returns the square of its numeric parameter n.
def sqr(n):
    return n * n
num = float(input("Enter a number: "))
result = sqr(num)
print("The square ->", num, "is", result)
