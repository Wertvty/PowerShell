def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strings have different lengths')
    return sum([1 for a, b in zip(strand_a, strand_b) if a != b])

