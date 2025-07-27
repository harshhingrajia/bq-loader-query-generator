import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from bq_query_generator.utils import register_jinja_filters


def load_schema_from_json(schema_path):
    with open(schema_path, 'r') as f:
        schema_data = json.load(f)

    if 'target_table' not in schema_data or 'source_table' not in schema_data or 'schema' not in schema_data:
        raise ValueError("JSON must include 'target_table', 'source_table', and 'schema' keys")

    # Filter schema to include only fields with both name and type
    filtered_schema = [field for field in schema_data['schema'] if 'name' in field and 'type' in field]

    return {
        "target_table": schema_data["target_table"],
        "source_table": schema_data["source_table"],
        "schema": filtered_schema
    }


def generate_merge_query(schema, target_table, source_table, merge_keys):
    field_names = [field['name'] for field in schema]
    update_fields = [f for f in field_names if f not in merge_keys]


    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # ✅ Register shared filters
    register_jinja_filters(env)

    template = env.get_template("merge.sql.j2")
    
    return template.render(
        target_table=target_table,
        source_table=source_table,
        merge_keys=merge_keys,
        update_fields=update_fields,
        all_fields=field_names
    )


def generate_truncate_insert_query(schema, target_table, source_table):
    field_names = [field['name'] for field in schema]

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # ✅ Register shared filters
    register_jinja_filters(env)

    template = env.get_template("truncate_load.sql.j2")

    return template.render(
        target_table=target_table,
        source_table=source_table,
        all_fields=field_names
    )


def generate_insert_query(schema, target_table, source_table):
    field_names = [field['name'] for field in schema]

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True
    )

    # ✅ Register shared filters
    register_jinja_filters(env)

    template = env.get_template("insert.sql.j2")

    return template.render(
        target_table=target_table,
        source_table=source_table,
        all_fields=field_names
    )