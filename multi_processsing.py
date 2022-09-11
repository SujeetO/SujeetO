import time
from  multiprocessing import Pool
import os
from joblib import delayed , Parallel


print(f'number of cores {os.cpu_count()}')

def is_perfect(n):
    # time.sleep(0.01)
    sum_factors = 0
    for i in range(1, n):
        if(n % i == 0):
            sum_factors = sum_factors + i
    if (sum_factors == n):
        print('{} is a Perfect number'.format(n))
        return n

# def is_perfect(n):
    # time.sleep(5)
    # return n

def is_perfect(n):
    return sum([n*n for i in range(n) ])

counter = 19000

if 0:
    tic = time.time()
    data = [is_perfect(i) for i in range(1,29009)]
    # print(data)
    toc = time.time()

    print('Done in {:.4f} seconds'.format(toc-tic))


if 0:
    print("inside pool")
    tic = time.time()
    pool = Pool()
    data = pool.map(is_perfect, range(1,100000))
    
    
    pool.close()
    print(len(data) , type(data))
    toc = time.time()
    
    print('Done in {:.4f} seconds'.format(toc-tic))

if 1:
    tic = time.time()
    print("inside joblib threads")
    delayed_func = [ delayed(is_perfect)(i) for i in range(1,counter)]

    with Parallel(prefer="threads",verbose=0,n_jobs=-1) as p:
        data = p(delayed_func)

    # print(data)
    print(len(data) , sum(data))
    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))

if 1:
    tic = time.time()
    print("inside joblib process")
    delayed_func = [ delayed(is_perfect)(i) for i in range(1,counter)]

    with Parallel(prefer="processes",verbose=0,n_jobs=-1) as p:
        data = p(delayed_func)

    print(len(data) , sum(data))
    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))


