def calculate_score(
    monthly_income: float,
    requested_amount: float,
    term_months: int
) -> int:
    # Учебная модель, не реальный банковский скоринг.
    ratio = monthly_income / requested_amount

    if ratio >= 0.5:
        score = 850
    elif ratio >= 0.3:
        score = 750
    elif ratio >= 0.2:
        score = 650
    elif ratio >= 0.1:
        score = 550
    else:
        score = 450

    if term_months > 60:
        score -= 30

    return max(300, min(850, score))
