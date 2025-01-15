# interest_utils.py

def calculate_monthly_interest(balance, annual_rate, periods):
    return (balance * (annual_rate / 100)) / 12 * periods

def calculate_monthly_interest_compounded(balance, annual_rate, periods):
    return balance * ((1 + (annual_rate / 100) / 12) ** periods - 1)

def calculate_daily_interest(balance, annual_rate, periods):
    return (balance * (annual_rate / 100)) / 365 * periods

def calculate_daily_interest_compounded(balance, annual_rate, periods):
    return balance * ((1 + (annual_rate / 100) / 365) ** periods - 1)

def get_interest_rate_to_use(base_rate, adjustment_factor):
    return base_rate + adjustment_factor
