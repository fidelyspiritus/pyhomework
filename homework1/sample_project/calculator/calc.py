def check_power_of_2(a: int) -> bool:
    return not (a > 0 and bool(a & (a - 1)))
