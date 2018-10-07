print(1 + 1)
for x in range(1, 10):
    print(x)

import sys
has_args = len(sys.argv) == 1
print(has_args)
if has_args:
    print([x for x in range(1, 20) if x % 2 == 0])
