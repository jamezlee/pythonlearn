stdHeights = input().split()

for n in range(0, len(stdHeights)):
    stdHeights[n]=int(stdHeights[n])
    
total_height = 0
for height in stdHeights:
    total_height += height

print(f"total height = {total_height}")

num_std = 0
for std in stdHeights:
    num_std += 1

print(f"total students = {num_std}")

average_height = round(total_height / num_std )
print(f"average height = {average_height}")