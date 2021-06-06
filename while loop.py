# while loop executes it's statement until the condition is true

n = int(input("Input a integer number: "))
i = sum = 0
while i <= n:
    sum = sum+i
    i = i+1

print("Result is: " + str(sum))
