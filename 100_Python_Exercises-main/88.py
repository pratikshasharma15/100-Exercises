import pandas

data = pandas.read_csv("countries_by_area.csv")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)


# to iterate over rows use iterrows
for index, row in data[:5].iterrows():
    print(row["country"])
