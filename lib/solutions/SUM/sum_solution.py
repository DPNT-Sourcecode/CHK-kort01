# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if 0 <= x <= 100 and 0 <= y <= 100:
        return x+y
    else:
        raise ValueError("Both parameters must be integers between 0 and 100")
