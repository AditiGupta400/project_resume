import pandas as pd

jobs_df = pd.read_csv("postings.csv")

jobs_df = jobs_df[['title', 'description']].dropna()