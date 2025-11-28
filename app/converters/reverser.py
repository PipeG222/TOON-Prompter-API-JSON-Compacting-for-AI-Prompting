def reverse_optimization(data: dict, original: dict):
    """
    Si quieres restaurar nombres largos desde original.
    """
    restored = {}
    mapping = {k[0]: k for k in original.keys()}

    for k, v in data.items():
        real_key = mapping.get(k, k)
        restored[real_key] = v
    return restored
