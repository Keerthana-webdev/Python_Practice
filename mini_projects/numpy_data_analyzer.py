import numpy as np

data = np.random.randint(1, 100, 10)

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Sorted:", np.sort(data))