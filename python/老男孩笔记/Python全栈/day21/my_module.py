print(12345)
__all__ = ['name','read1','read2']

name = 'disman'

def read1():
    print('in read1 func')

def read2():
    print('in read2 func',name)


print(54321)
if __name__ == '__main__':
    print(__name__)
    print([__name__])