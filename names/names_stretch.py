import time

start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Trying to compare with complexity of O()
duplicates = []

# Sort both the lists
names_1.sort()
names_2.sort()

# Iterate through list names_1 and compare with names in names_2
names_2_pos = 0

for name in names_1:
    # Handle case of name in names_1 being greater
    # than name in names_2 by updating lookup
    # position of names_2
    while (names_2_pos < len(names_2) and
           names_2[names_2_pos] < name):
        names_2_pos += 1

    # Find duplicates
    if name == names_2[names_2_pos]:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
