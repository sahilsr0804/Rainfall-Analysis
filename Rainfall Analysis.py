
#Printing Tabular Form of Data
import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Seattle2014.csv")
print(data.head())

rainfall = data["PRCP"].values
inches = rainfall/254
print(inches.shape)

#Finding Number of days without rain, with rain, with rain more than 0.5 inches and with rain < 0.2 inches
print("Number of days without rain: ", np.sum(inches == 0))
print("Number of days with rain: ", np.sum(inches != 0))
print("Number of days with rain more than 0.5 inches: ", np.sum(inches>0.5))
print("Number of days with rain < 0.2 inches: ", np.sum((inches > 0)& (inches < 0.2)))

#Making Bar Graph
import matplotlib.pyplot as plt
plt.hist(inches, 40)
plt.show()