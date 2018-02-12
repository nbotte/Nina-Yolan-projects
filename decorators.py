import time

def bench_dec(f):
	
	def wrapper(*args, **kwargs):
		before = time.time()
		result = f(*args, **kwargs)
		after = time.time()
		print(after - before)
		return result
	return wrapper

def memoize(f):
	lut = {}
	def wrapper(x):
		if x not in lut:
			lut[x] = f(x)
		return lut[x]
	return wrapper


@memoize
def fibonacci(n):
	try:
		assert n >= 0
		if n > 1:
			return fibonacci(n-1) + fibonacci(n-2)
		else:
			return n
	except AssertionError:
		print("Invalid Argument!")

def fib_dyn(n):
	fib_0 = 0
	fib_1 = 1
	for _ in range(n-1):
		fib_0, fib_1 = fib_1, fib_0 + fib_1
	return fib_1


before = time.time()
print(fibonacci(32))
print(fibonacci(32))
print(fibonacci(32))
after = time.time()
print(after - before)	

before = time.time()
print(fib_dyn(32))
print(fib_dyn(32))
print(fib_dyn(32))
after = time.time()
print(after - before)	