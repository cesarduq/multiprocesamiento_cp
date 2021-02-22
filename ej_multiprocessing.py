import collections
import time
from pprint import pprint
import multiprocessing
import os

vector= [4,5,6,7,8]

pprint(vector)
print()


def cuadrado(x):
    print(f'Process {os.getpid()} working record {x}')  
    time.sleep(1)
    result = pow(x,2)
    print(f'Process {os.getpid()} done processing record {x}')
    return result


start = time.time()

pool = multiprocessing.Pool() 
result=pool.map(cuadrado, vector) 

end = time.time()


print()
print(f'Time to complete: {end-start}')
print(f'Los numeros elevados al cuadrado son: {result}')
