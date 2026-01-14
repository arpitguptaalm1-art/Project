def calculate_total_impact(impact):
    return sum(impact.values())


def calculate_butterfly_intensity(impact, frequency, time_period):
    base = sum(impact.values())
    return base * frequency * time_period
