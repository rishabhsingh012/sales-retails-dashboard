import sqlite3
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
db_path = base_dir / 'data' / 'cleaned_train.db'
sql_path = base_dir / 'sql' / 'sql' / 'analysis_queries.sql'

conn = sqlite3.connect(db_path)
sql_text = sql_path.read_text(encoding='utf-8')

print('Running queries from:', sql_path)
statements = []
current = []

for line in sql_text.splitlines():
    stripped = line.strip()
    if not stripped or stripped.startswith('--'):
        continue
    current.append(line)
    if stripped.endswith(';'):
        statement = '\n'.join(current).strip()
        if statement:
            statements.append(statement)
        current = []

if current:
    statement = '\n'.join(current).strip()
    if statement:
        statements.append(statement)

for index, statement in enumerate(statements, start=1):
    print(f'\nQuery {index}:')
    for row in conn.execute(statement):
        print(row)

conn.close()
