from timeit import timeit

def fib(n):
	return n if n < 2 else fib(n-1)+fib(n-2)


iters = 50

total_time = timeit("fib(11)", number=iters, globals=globals())
#total_time = timeit("fib(11)", number=iters)

print(f"average time : {total_time/iters}")
