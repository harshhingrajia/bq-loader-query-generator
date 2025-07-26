def quote_field(value):
    """Wrap field name in backticks."""
    return f"`{value}`"

def prepend(value, prefix):
    """Prepend prefix to a single value."""
    return f"{prefix}{value}"

def prepend_filter(items, prefix):
    """Prepend a prefix to each item in a list and return a formatted string."""
    return ',\n    '.join(f"{prefix}{item}" for item in items)

def register_jinja_filters(env):
    """Register all custom Jinja filters into the provided environment."""
    env.filters["quote_field"] = quote_field
    env.filters["prepend"] = prepend
    env.filters["prepend_filter"] = prepend_filter
