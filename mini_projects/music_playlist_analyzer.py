import pandas as pd

data = {
    "Song": ["S1", "S2", "S3", "S4"],
    "Artist": ["A", "B", "A", "A"]
}

df = pd.DataFrame(data)

count = df["Artist"].value_counts()

print(count)
print("\nTop Artist:", count.idxmax())