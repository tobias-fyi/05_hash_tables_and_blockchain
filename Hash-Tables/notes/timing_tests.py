

# O(n^2)
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - i)
    return x

# O(n)
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# O(n)
def pre_allocate(n):
    x = [None] * n
    for i in range(0, n):
        x[i] = i + 1
    return x


import time

start_time = time.time()
add_to_back(100000)  # O(n)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
# runtime: 0.07669210433959961 seconds





start_time = time.time()
add_to_front(100000)  # O(n^2)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
# runtime: 56.415611743927 seconds




n = 500000          # n = 500 thousand
add_to_back(n)      # 0.0752871036529541 seconds
pre_allocate(n)     # 0.05263519287109375 seconds


n = 5000000         # n = 5 million
add_to_back(n)      # 0.72271728515625 seconds
pre_allocate(n)     # 0.5194799900054932 seconds


n = 50000000        # n = 50 million
add_to_back(n)      # 7.198451995849609 seconds
pre_allocate(n)     # 5.220464706420898 seconds

# Preallocating memory is consistently ~40% faster

