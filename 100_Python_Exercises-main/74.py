import pandas as pd

frames = [pd.read_csv("data_multiply.csv"), pd.read_csv("new_data.csv")]

result = pd.concat(frames, ignore_index=True)
print(result)
