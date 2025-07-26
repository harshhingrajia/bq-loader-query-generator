if __name__ == "__main__":
    schema = load_schema_from_json("examples/sample_schema.json")
    query = generate_merge_query(
        schema=schema,
        target_table="project.dataset.target_table",
        staging_table="project.dataset.staging_table",
        merge_keys=["ID"]
    )
    print(query)
