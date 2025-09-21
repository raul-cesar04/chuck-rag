from collections.abc import Iterable

## Cosine Similiarity function to compare the similiarity between two vectors
def cosine_similiarity(a: Iterable[any], b: Iterable[any])->float:
    dot_product = sum([x*y for x, y in zip(a, b)])
    
    norm_a = sum([x**2 for x in a]) ** 0.5
    norm_b = sum([x**2 for x in b]) ** 0.5

    return dot_product / (norm_a * norm_b)