# excwption = events during execution that interrupt the flow of a program

try:
    num1 = int(input("Enter a number to divide: "))
    num2 = int(input("Enter a number to divide: "))
    result = num1/num2


except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print(result)
