def funX(x):
    def funY(y):
        return x*y
    return funY

if __name__=='__main__':
    i=funX(8)
    print(i(5))
    assert i(10)==80
    assert i(20)==160

    i2=funX(10)
    i2(5)
    i2(10)
    i2(20)
