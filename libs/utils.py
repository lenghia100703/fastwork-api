import random


def get_random_digit_code(length: int) -> str:
    return "".join(random.choices("0123456789", k=length))
