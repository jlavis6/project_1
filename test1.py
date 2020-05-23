import os
import pandas as pd

#os.chdir("Users/jlavi/OneDrive - IPADE Business School/Coding")

print(os.getcwd())
print()
df = pd.read_excel("Bank Accounts.xlsx", sheet_name="2Now")

print(df)
