import argparse
import sqlparse
from bq_query_generator.generator import load_schema_from_json, generate_merge_query
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="BigQuery SQL Generator CLI")

    parser.add_argument('--mode', required=True, choices=['merge', 'truncate-insert', 'insert'], help="Query generation mode")
    parser.add_argument('--schema', required=True, help="Path to schema JSON file")
    parser.add_argument('--table', required=True, help="Target BigQuery table (project.dataset.table)")
    parser.add_argument('--staging-table', required=True, help="Staging table (for merge mode)")
    parser.add_argument('--keys', help="Comma-separated merge keys (for merge mode)")
    parser.add_argument('--output', help="Optional path to save generated SQL to a .sql file")
    parser.add_argument('--add-metadata', action='store_true', help="Include metadata fields in source SELECT")
   # parser.add_argument('--on-condition', help="Custom ON condition for MERGE")
    parser.add_argument('--select-sql', help="Path to SQL file with custom source SELECT statement")

    args = parser.parse_args()
    schema = load_schema_from_json(args.schema)

    if args.mode == "merge":
        if not args.staging_table or not args.keys:
            raise ValueError("MERGE mode requires --staging-table and --keys")
        merge_keys = [k.strip() for k in args.keys.split(",")]
        sql = generate_merge_query(
            schema=schema,
            target_table=args.table,
            staging_table=args.staging_table,
            merge_keys=merge_keys
        )

        # Format SQL using sqlparse
        pretty_sql = sqlparse.format(sql, reindent=True)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)  # auto-create folder
            with open(output_path, "w") as f:
                f.write(sql)
            print(f"✅ SQL saved to: {args.output}")
        else:
            print(sql, "\n")
            print("ℹ️  If you want to save this query to a SQL file, provide --output <path>")

    else:
        raise NotImplementedError(f"Mode '{args.mode}' not yet implemented")


if __name__ == "__main__":
    main()
