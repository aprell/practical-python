# Exercises 1.7-1.11, 1.17

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > payment:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    print(f"{month:5d}{total_paid:12,.2f}{principal:12,.2f}")
    month += 1

total_paid += principal
principal = 0
print(f"{month:5d}{total_paid:12,.2f}{principal:12,.2f}")
