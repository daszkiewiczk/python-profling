import time

def sleeper():
    time.sleep(1.76)

def spinlock():
    for _ in range(1_000_000):
        pass

for function in sleeper, spinlock:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(function.__name__)
    print(t2[0]-t1[0])
    print(t2[1]-t1[1])
