def odd(x):
    return x%2

if __name__=='__main__':
    temp=filter(odd,range(20))
    print(list(temp))
    # alternate expression with lambda function
    print(list(filter(lambda x:x%2,range(20))))
