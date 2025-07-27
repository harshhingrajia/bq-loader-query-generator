import argparse
from bq_query_generator.query_builder import (
    load_schema_from_json, generate_merge_query, 
    generate_truncate_insert_query, generate_insert_query
)
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="BigQuery SQL Generator CLI")

    parser.add_argument('--mode', required=True, choices=['merge', 'truncate_load', 'insert'], help="Query generation mode")
    parser.add_argument('--schema', required=True, help="Path to schema JSON file")
    parser.add_argument('--merge_keys', help="Comma-separated merge keys (for merge mode)")
    parser.add_argument('--output', help="Optional path to save generated SQL to a .sql file")

    args = parser.parse_args()

    schema_data = load_schema_from_json(args.schema)
    target_table = schema_data.get("target_table")
    source_table = schema_data.get("source_table")
    schema = schema_data.get("schema")

    
    if args.mode == "merge":
        if not source_table or not args.merge_keys:
            raise ValueError("MERGE mode requires --source_table and --keys")
        merge_keys = [k.strip() for k in args.merge_keys.split(",")]
        sql = generate_merge_query(
            schema=schema,
            target_table=target_table,
            source_table=source_table,
            merge_keys=merge_keys
        )

    elif args.mode == "truncate_load":
        sql = generate_truncate_insert_query(
            schema=schema,
            target_table=target_table,
            source_table=source_table
        )
    
    elif args.mode == "insert":
        sql = generate_insert_query(
            schema=schema,
            target_table=target_table,
            source_table=source_table
        )

    else:
        raise NotImplementedError(f"Mode '{args.mode}' not yet implemented")

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)  # auto-create folder
        with open(output_path, "w") as f:
            f.write(sql)
        print(f"✅ SQL saved to: {args.output}")
    else:
        print(sql, "\n")
        print("ℹ️  If you want to save this query to a SQL file, provide --output <path>")



if __name__ == "__main__":
    main()
