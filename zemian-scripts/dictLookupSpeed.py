# result:

# With doing nothing (pass)
# >>> 2.1e+02
# 210.0
# >>> _ / 60
# 3.5 mins

# with dict lookup
# >>> 8.05e+02 / 60
# 13.416666666666666 mins

import time, random

# Seepd of empty loop
t1 = time.time()
n = 3_600_000_000
for _ in range(n):
	pass
print(f"{n} iteration - empty loop. Cost {time.time() - t1:.3} secs")

# Speed of dict lookup
data = {}
for i in range(1000):
	data['foo' + str(i)] = i * random.random()

t1 = time.time()
n = 3_600_000_000
count = 0
for _ in range(n):
	if 'foo99' in data:
		count += 1
print(f"{n} iteration - dict lookup of {count}. Cost {time.time() - t1:.3} secs")
