# bq-loader-query-generator

### Description: 
🛠️ A lightweight Python-based plugin that generates BigQuery MERGE, TRUNCATE + LOAD, or INSERT SQL statements from JSON table schema definitions. Designed for data engineers and workflow automation in ELT pipelines.

### Features include:
- Custom `ON` conditions
- Manual `SELECT` clause overrides
- Modular Jinja templates

---

## 📌 Features

- ✅ Generate BigQuery SQL templates from schema
- ✅ Supports dynamic field quoting, prefixing
- ✅ Templated SQL using Jinja2
- ✅ Easily extensible for future operations

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/harshhingrajia/bq-loader-query-generator.git
cd bq-loader-query-generator
```

### 2. (Optional but recommended) Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
```

### 3. Install project dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the project in editable/development mode

```bash
pip install -e .
```

### 5. Run the generator

#### Using CLI entry point

##### Merge Command
```bash
bq-query-generator \
  --mode merge \
  --schema ./examples/sample_schema.json \
  --merge_keys Sales_Id \
  --output tests/sql/merge_generated.sql 
```

##### Truncate and Load Command
```bash
bq-query-generator \
    --mode truncate_load \
    --schema ./examples/sample_schema.json \
    --output tests/sql/truncate_load_generated.sql
```

##### Insert Command
```bash
bq-query-generator \
    --mode insert \
    --schema ./examples/sample_schema.json \
    --output tests/sql/insert_generated.sql
```


## 🛠 Command Line Options

| Flag           | Description                                                 | Required        |
| -------------- | ----------------------------------------------------------- | --------------- |
| `--mode`       | Query generation mode (`merge`, `truncate_load`, `insert`)  | ✅              |
| `--schema`     | Path to input JSON schema file (contains table & columns)   | ✅              |
| `--merge_keys` | Comma-separated list of merge key fields (for `merge` only) | ✅ (merge only) |
| `--output`     | Optional path to save generated SQL to a `.sql` file        | ❌              |

## 📁 Project Structure

```bash
bq-loader-query-generator/
│
├── bq_query_generator/
│   ├── __init__.py
│   ├── query_builder.py           # Core logic for SQL generation
│   ├── utils.py                   # Utility functions and filters
│   └── templates/
│       ├── merge.sql.j2           # Jinja template for MERGE
│       ├── insert.sql.j2          # Jinja template for INSERT
│       └── truncate_load.sql.j2   # Jinja template for TRUNCATE + INSERT
├── cli/
│   ├── generate_sql.py            # CLI entrypoint for query generation
├── pyproject.toml
├── README.md
├── setup.py
```

## 📄 Example Schema File

```json
{
  "target_table": "project_id.dataset.target_table",
  "source_table": "project_id.dataset.source_table",
  "schema": [
    { "name": "ID", "type": "STRING" },
    { "name": "EmployeeName", "type": "STRING" },
    { "name": "JoinDate", "type": "DATE" }
  ]
}
```
