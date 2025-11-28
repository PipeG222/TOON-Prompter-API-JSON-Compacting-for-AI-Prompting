def optimize(data: dict):
    """
    Renombra claves y reduce estructura redundante.
    Más amigable para prompts y LLM.
    """
    new = {}
    for k, v in data.items():
        short = k[0].lower()
        if isinstance(v, dict):
            new[short] = optimize(v)
        else:
            new[short] = v
    return new
