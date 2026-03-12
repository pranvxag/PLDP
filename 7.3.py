d = {"a": 10, "b": None, "c": 30, "d": None}

result = {k: (v if v is not None else 0) for k, v in d.items()}

print(result)
