import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
ct = pickle.load(open("transformer.pkl", "rb"))

# correct format with column names
data = pd.DataFrame([[1500, 3, "city"]],
                    columns=["area", "rooms", "location"])

data = ct.transform(data)

result = model.predict(data)

print("Predicted House Price:", round(result[0], 2))