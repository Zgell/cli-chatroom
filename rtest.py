import time
import sys

'''
Test file for getting text to overwrite itself
'''

if __name__ == '__main__':
    print('Hello!', end='\r')
    time.sleep(1)
    print('World!', end='\r')
    time.sleep(1)
    print('Hello!', end='\r')
    time.sleep(1)
    print('World!', end='\r')