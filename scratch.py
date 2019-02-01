def sumOutside(a,b):
    return a+b

def multOutside(a,b):
    return a*b

def combineFuncs(sum, mult):
    # def returnFunc(a,b):
    #     sumValue = sum(a,b)
    #     return mult(sumValue, sumValue)
    # return returnFunc
    return lambda x,y: mult(sum(x,y), sum(x,y))

combinedFunction = combineFuncs(sumOutside, multOutside)
print(combinedFunction(1,2));