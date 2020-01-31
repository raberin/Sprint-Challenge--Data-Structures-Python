import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# O(n^2)
# duplicates_slow = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates_slow.append(name_1)
# runtime: 9.403305292129517 seconds

# O(n) - worst case scenario, BUT on avg O(1) :)
names_1_set = set(names_1)
names_2_set = set(names_2)
duplicates = list(names_1_set.intersection(names_2_set))
# runtime: 0.010130882263183594 seconds

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
