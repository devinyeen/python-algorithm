#Recursive
import time

def fact(x):
	if x == 1:
		return 1
	else:
		return x*fact(x-1)

#print(fact(1))
#print(fact(5))
start = time.perf_counter();
print(fact(10))
end = time.perf_counter();
print(end-start)

def fact0(x, prod = 1):
	if x == 1:
		return prod
	return fact0(x-1,x*prod)

#print(fact0(1))
#print(fact0(5))
start = time.perf_counter();
print(fact0(10))
end = time.perf_counter();
print(end-start)