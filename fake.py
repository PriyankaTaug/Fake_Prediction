import pandas as pd
import matplotlib.pyplot as plt


# set plot options
plt.rcParams['figure.figsize'] = (12, 8)
default_plot_colour = "#00bfbf"



data = pd.read_csv("fake_news_data.csv")
data.head()


data.info()


data['fake_or_factual'].value_counts().plot(kind='bar',color=default_plot_colour)