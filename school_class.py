import pandas as pd

school_class_data = {
    "Name":["Precious", "Thomas", "Sarah", "Laura", "Teddy", "Nora"],
    "Age":["60", "20", "25", "30", "35", "40"],
    "Grade":[80, 75, 25, 30, None,None,],
}

df = pd.DataFrame(school_class_data)
df.to_csv(r"C:\Users\Admin\Downloads\school.csv")
filtered_data = df[df["Grade"] > 70]
print(filtered_data)
print()
clean_data = df.fillna(0)
print(clean_data)