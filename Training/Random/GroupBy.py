import pandas as pd 

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Department": ["HR", "IT", "IT", "HR", "Finance", "Finance", "IT"],
    "Salary": [120000, 50000, 160000, 80000, 210000, 67000, 500000]
}


df = pd.DataFrame(data)
print("\n Original DataFrame:\n", df)

# Group by department and count number of names in each
grouped_count = df.groupby("Department") ["Name"].count()
print("\nGrouped By department and counted each empoyee which is apart of that Department:\n", grouped_count)

# Group by deparment and calculate average Salary
avg_sal_dep = df.groupby("Department") ["Salary"].mean()
print("\nAverge Salary by Department:\n", avg_sal_dep)




