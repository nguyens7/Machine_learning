import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# Load the data
oecd_bli = pd.read_csv("oecd_bli_2016.csv", thousands=',')
gdP_per_capita = pd.read_csv("gdp_per_capita.csv",thousands=',', delimiter='\t')

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdP_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

# Select a linear model
lin_reg_model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[22587]] # Cprus' GDP per capita
print(lin_reg_model.predict(X_new))  # outputs [[5.96242338]]
