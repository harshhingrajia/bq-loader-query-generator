# bq-loader-query-generator

### Description: 
🛠️ A lightweight Python-based plugin that generates BigQuery MERGE, TRUNCATE + LOAD, or INSERT SQL statements from JSON table schema definitions. Designed for data engineers and workflow automation in ELT pipelines.

### Features include:
- Optional metadata fields
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

### Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the generator
#### Option 1: Using Python module directly

```bash
python -m bq_query_generator.cli.generate \
  --schema path/to/schema.json \
  --target_table project.dataset.final_table \
  --staging_table project.dataset.staging_table \
  --merge_keys ID,Date
```

#### Option 2: Using CLI entry point (if installed)

```bash
bq-query-generator \
  --schema path/to/schema.json \
  --target_table project.dataset.final_table \
  --staging_table project.dataset.staging_table \
  --merge_keys ID,Date
```

## 🛠 Command Line Options

| Flag              | Description                              | Required |
|-------------------|------------------------------------------|----------|
| `--schema`        | Path to input JSON schema file           | ✅       |
| `--target_table`  | BigQuery target table                    | ✅       |
| `--staging_table` | BigQuery staging/source table            | ✅       |
| `--merge_keys`    | Comma-separated list of merge key fields | ✅       |


## 📁 Project Structure

```bash
bq-loader-query-generator/
│
├── bq_query_generator/
│   ├── __init__.py
│   ├── cli/
│   │   └── generate.py            # CLI entrypoint
│   ├── generator.py               # Core logic for SQL generation
│   ├── utils.py                   # Utility functions and filters
│   └── templates/
│       ├── merge.sql.j2           # Jinja template for MERGE
│       ├── insert.sql.j2          # Jinja template for INSERT
│       └── truncate_insert.sql.j2 # Jinja template for TRUNCATE + INSERT
│
├── requirements.txt
├── README.md
```

## 🧪 Running Tests
If tests are located under tests/, run them using:

```bash
python -m unittest discover tests
```

## 📄 Example Schema File

```json
[
  { "name": "ID", "type": "STRING" },
  { "name": "EmployeeName", "type": "STRING" },
  { "name": "JoinDate", "type": "DATE" }
]
```

## 🧰 Planned Enhancements

- 🔁 Support for additional SQL operations
- 📝 YAML schema compatibility
- 📅 Optional metadata configuration (e.g., insert timestamps, job IDs)

