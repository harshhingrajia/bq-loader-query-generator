def quote_field(value):
    """Wrap field name in backticks."""
    return f"`{value}`"

def prepend(value, prefix):
    """Prepend prefix to a single value."""
    return f"{prefix}{value}"

def format_assignment(pair):
    """Format target.field = source.field."""
    source, target = pair
    return f"target.{target} = {source}"

def zip_lists(a, b):
    return zip(a, b)

def build_on_condition(merge_keys):
    """Build the ON condition for the MERGE statement."""
    return " AND ".join([f"target.{key} = source.{key}" for key in merge_keys])

def register_jinja_filters(env):
    """Register custom Jinja filters."""
    env.filters["quote_field"] = quote_field
    env.filters["prepend"] = prepend
    env.filters["zip"] = zip_lists
    env.filters["format_assignment"] = format_assignment
    env.filters["build_on_condition"] = build_on_condition
