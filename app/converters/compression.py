import json

def compress(json_data: dict) -> str:
    """
    Compacta el JSON sin espacios ni indentación.
    Es reversible.
    """
    return json.dumps(
        json_data,
        separators=(",", ":"),
        ensure_ascii=False,
    )
