from .compression import compress
from .optimizer import optimize

def convert_json(data: dict, mode: int):
    if mode == 1:
        return {
            "mode": "compression",
            "original": data,
            "result": compress(data)
        }

    if mode == 2:
        opt = optimize(data)
        return {
            "mode": "optimization",
            "original": data,
            "result": opt
        }

    if mode == 3:
        opt = optimize(data)
        return {
            "mode": "toon",
            "original": data,
            "result": compress(opt)
        }

    return {"error": "invalid mode"}
