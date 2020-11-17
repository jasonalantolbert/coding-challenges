import itertools
import time

n_steps = int(input("Enter a number of steps:\n> "))
steps_at_a_time = [*[0] * n_steps]
for i in input("Enter the simultaneous climb range (e.g. 1, 3, 5):\n> ").replace(" ", "").split(","):
    steps_at_a_time.extend([*[int(i)] * n_steps])
combos = set()
start_time = time.time()
for i in {i for i in itertools.permutations(steps_at_a_time, r=n_steps) if sum(i) == n_steps}:
    combos.add(tuple(j for j in i if j != 0))

print(combos)
print(time.time() - start_time)
