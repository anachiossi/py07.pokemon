MODULUS = 2 ** 31
MULTIPLIER = 1103515245
INCREMENT = 12345

state = 1


def seed(value: int) -> None:
    global state
    state = value % MODULUS


def between(low: int, high: int) -> int:
    global state
    if high <= low:
        return low
    state = (state * MULTIPLIER + INCREMENT) % MODULUS
    span = high - low + 1
    return low + state % span
