import seaborn as sns

sns.set_style(style='whitegrid')

penguins = sns.load_dataset("penguins")
print(penguins)

#line plot
sns.lineplot(data=penguins, x="body_mass_g",
             y="flipper_length_mm",
            errorbar=None,
            hue="species")

#pointplot
sns.pointplot(data=penguins,
             x="species",
             y="body_mass_g",
             hue="sex",
             palette="winter")

#histplot
sns.histplot(data=penguins, x="bill_depth_mm",
            bins=30,
            hue="species",
            multiple="stack")

#barplot
sns.barplot(data=penguins,
           x="island",
           y="body_mass_g",
           hue="sex",
           palette="summer")

#countplot
sns.countplot(data=penguins,
             y="sex")

#boxplot
sns.boxplot(data=penguins,
           x="species",
           y="body_mass_g")

#swarmplot
sns.swarmplot(data=penguins,
             x="sex",
             y="flipper_length_mm")

#scatterplot
sns.scatterplot(data=penguins,
               x="body_mass_g",
               y="flipper_length_mm",
               hue="species")

#heatmap
penguins.corr()
sns.heatmap(penguins.corr(),
           annot=True,
           cmap="Blues")


#pairplot
sns.pairplot(data=penguins,
            hue="species")

