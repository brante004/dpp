import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

fig, ax = plt.subplots()
grouped = df.groupby('species')
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}

for key, group in grouped:
    group.plot(x='sepal_length', y='petal_length',
               ax=ax,
               kind='scatter',
               color=colors[key],
               label=key.capitalize())

leg = ax.legend()
leg.set_title('species')
plt.show()

test = [(key, group) for key, group in grouped]
test
grouped.groups

#recreate this plot in Seaborn!
sns.set()
fig, ax = plt.subplots()
for key, group in grouped:
    sns.scatterplot(x='sepal_length', y='petal_length',
                    ax=ax,
                    data=group,
                    color=colors[key],
                    label=key.capitalize())
legend = ax.legend()
legend.set_title('Species')
plt.show()