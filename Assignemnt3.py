def factorial(a):
    if a<2:
        return 1
    else:
        return factorial(a-1)*a

Sample_Number = 10
Result=factorial(Sample_Number)
print('Factorial of',Sample_Number,'is',Result)
