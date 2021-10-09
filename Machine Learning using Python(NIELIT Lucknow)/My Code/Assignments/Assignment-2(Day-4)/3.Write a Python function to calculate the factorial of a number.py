# Write a Python function to calculate the factorial of a number

def fact(num):
    result=1
    if num<0:
        return f'The number should be positive'
    elif num==0 or num==1:
        return result
    else:
        for i in range(1,num+1):
            result*=i
        return result

print(fact(5))