def cart_total(prices: list[float]) -> float:
    return round(sum(prices), 2)


COUPONS = {"WELCOME10": 10, "SUMMER25": 25}


def apply_coupon(total: float, code: str) -> float:
    percent = COUPONS.get(code.upper())
    if percent is None:
        raise ValueError(f"unknown coupon {code!r}")
    return round(total * (1 - percent / 100), 2)
