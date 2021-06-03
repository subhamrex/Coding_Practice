import time


def time_it(func):
    def wrapper(*args, **kwargs):
        Start_time = time.time()
        result = func(*args, **kwargs)
        End_time = time.time()
        print("Execution time of  "+func.__name__ +"= "+
              str((End_time - Start_time)*1000)+" miliseconds")
        return result
    return wrapper