from jsonschema import validate

# Sample JSON data
data = {
    "name": "John",
    "age": 30
}

# Schema you want your JSON data to conform to
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
}

# Validate will raise an exception if given JSON data is not
# what is described in the schema.
validate(instance=data, schema=schema)