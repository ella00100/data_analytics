import seaborn as sns

sns.set_style(style='whitegrid')

penguins = sns.load_dataset("penguins")
print(penguins)

#line plot
penguins_line = sns.lineplot(data=penguins, x="body_mass_g",
             y="flipper_length_mm",
            errorbar=None,
            hue="species")

#pointplot
sns.pointplot(data=penguins,
             x="species",
             y="body_mass_g",
             hue="sex",
             palette="winter")
