import numpy as np

me_array = np.array ([
    [12, 13, 14, 15, 16, 17],
    [21, 22, 23, 24, 25, 26],
    [34, 45, 50, 54, 76, 100],
    [111, 125, 131, 116, 171, 142]
])
print('1. Transaction volume array: \n', me_array)

total_per_branch = np.sum(me_array, axis=1)
print("\n2. Total per brunch is:", total_per_branch)
highest_branch = np.argmax(total_per_branch) + 1
print("3. Branch with the highest transaction:", highest_branch)
average_monthly = np.mean(me_array)
print("4. Average volume is:", average_monthly)
reshaped_array = me_array.reshape(3, 8)
print("\n5. Reshaped array (3*8):", reshaped_array)
print("Implication: Reshaping changes data interpretation-rows no longer represent.")
print("Branches and columns no longer represents months. Data is rearranged linearly")

