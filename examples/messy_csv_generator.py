import pandas as pd # type: ignore
import numpy as np # type: ignore
import random
import string

np.random.seed(42)

def random_string(n=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

rows = 200
data = {
    "age": np.random.choice([25, 30, 35, None, "unknown", -5, 1000], size=rows),
    "fare": np.random.choice([7.25, 71.2833, None, "NA", -10, 500, "error"], size=rows),
    "name": [random_string(random.randint(3,10)) for _ in range(rows)],
    "joined": np.random.choice(
        ["2020-01-01", "not_a_date", None, "05/12/2022", "02-30-2020", "2021/07/15"],
        size=rows
    ),
    "survived": np.random.choice([0, 1, None, "yes", "no"], size=rows),
    "random_noise": np.random.randn(rows) * np.random.randint(1, 100)
}

df = pd.DataFrame(data)

df.loc[5, "age"] = "###"
df.loc[10, "fare"] = "??"
df.loc[15, "joined"] = 12345
df.loc[20, "random_noise"] = "infinite"
df.loc[25] = [None, None, None, None, None, None]  

df.to_csv("examples/messy_dataset.csv", index=False)

print("Generated messy_dataset.csv in examples/")
