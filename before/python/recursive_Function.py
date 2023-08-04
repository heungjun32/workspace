
j = int(input("Input Number for Factorial Calculation:"))
def multiplication(j):
    result = 1
    for num in range(1, j+1):
         result *= num
    return result
print (multiplication(j))    