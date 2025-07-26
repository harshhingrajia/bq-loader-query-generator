# generate.py

import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from bq_query_generator.utils import register_jinja_filters


def load_schema_from_json(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    return [field for field in schema if 'name' in field and 'type' in field]


def generate_merge_query(schema, target_table, staging_table, merge_keys):
    field_names = [field['name'] for field in schema]
    update_fields = [f for f in field_names if f not in merge_keys]

    env = Environment(
        loader=FileSystemLoader(searchpath=Path(__file__).parent / "templates"),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # ✅ Register shared filters
    register_jinja_filters(env)

    template = env.get_template("merge.sql.j2")
    return template.render(
        target_table=target_table,
        staging_table=staging_table,
        merge_keys=merge_keys,
        update_fields=update_fields,
        all_fields=field_names
    )
