import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# make the array from list
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
meas = np.array([np_height, np_weight])
# np.ndinter() function to output all items in array
for val in np.nditer(meas):
    print(val)
# np.logical_and np.logical_or np.logical_not logical operators in NumPy
print(bmi[np.logical_and(bmi > 21, bmi < 22)])
# create DataFrame from dictionary
dict_1 = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]}
bric = pd.DataFrame(dict)
# read the CSV file to Python
brics = pd.read_csv("path/to/brics.csv", index_col=0)
# .apply() do action in brackets
brics["name_length"] = brics["country"].apply(len)

world = {"afghanistan": 30.55,
         "albania": 2.77,
         "algeria": 39.21}
# .items()function to output all items in dictionary
for key, value in world.items():
    print(key + "--" + str(value))
# sort_values sort values by adjusted parameters
# acsending - по возрастанию, in breckets value which we sorted
dogs.sort_values(["weight_kg", "height_cm"], ascending=[True, False])
# .isin() find values in columns
is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
# .groupby() group object and show the mean() of values in square breckets
dogs.groupby(["color", "breed"])["weight_kg"].mean()
# pivot_table do the same things as well as groupby() but simplify
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median, columns="breed", fill_value=0,margins= True)
# set_index() set necessary data
dogs_ind = dogs.set_index("name")
dogs_ind.reset_index()
# .loc[] function slice the df by values or chhose columns or rows
dogs_ind3 = dogs_ind3.loc[["Labrador", "Chihuahua"]]
# sort_index sort values by adjusted parameters
dogs_ind3.sort_index(level=["color","breed"], ascending=[True, False])
# .groupby(index) and show the sum of [values]
# MATPLOTLIB.PYPLOT
avg_weight_by_breed = dog_pack.groupby("breed")["weight_kg"].sum()
# make a plot , kind = bar
avg_weight_by_breed.plot(kind="bar")
# make a plot of dog sully
sully.plot(x="date", y="weight_kg", kind="line", rot=45)

dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7)
plt.show()
# itterations in DataFrames
for row, value in netflix_movies_col_subset.iterrows() :
    if genre == "Children" :
        colors.append("red")
    elif genre == "Documentaries" :
        colors.append("blue")
    elif genre =="Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")