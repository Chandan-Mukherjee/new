import pandas as pd
import Relative_Project_Path
import os

os.chdir(Relative_Project_Path.ROOT_DIR)
# df = pd.read_csv('FL_insurance_sample.csv')
df = pd.read_csv(r"C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\FL_insurance_sample.csv")
print(df)


