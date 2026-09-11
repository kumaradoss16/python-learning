def search_within_buckets(bucket_chain, key):
    for stored_key, stored_value in bucket_chain:
        if stored_key == key:
            return stored_valuegit

    return None

bucket_chain = [
    ("name", "Kumar"),
    ("age", 25),
    ("city", "Puducherry")
]
key = "age"

result = search_within_buckets(bucket_chain, key)
print(result)