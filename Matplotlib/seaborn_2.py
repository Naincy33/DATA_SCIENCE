import seaborn as sns

print(sns.get_dataset_names())
tips = sns.load_dataset('tips')
print(tips.head())

