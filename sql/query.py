from pathlib import Path
import sqlite3
import pandas as pd

base_dir = Path(__file__).resolve().parent.parent
csv_path = base_dir / 'data' / 'cleaned_sales.csv'
db_path = base_dir / 'data' / 'cleaned_train.db'

df = pd.read_csv(csv_path)
df.columns = [col.strip().replace(' ', '_') for col in df.columns]
df['Postal_Code'] = df['Postal_Code'].astype('string').str.replace(r'\.0$', '', regex=True)

conn = sqlite3.connect(db_path)
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

