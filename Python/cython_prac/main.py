import time
import pyximport; pyximport.install()
import example_cython

def main():
    start = time.time()
    result = example_cython.count_triples(1000)
    duration = time.time() - start
    print(result,duration)

if __name__ == '__main__':
    main()    