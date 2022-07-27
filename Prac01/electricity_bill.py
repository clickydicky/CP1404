print("Electricity bill estimator")
tariff = input("Which tariff? 11 or 31: ")
while tariff not in ("11", "31"):
    print("Invalid input")
    tariff = input("Which tariff? 11 or 31: ")
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff == "11":
    cents_per_kWh = 0.244618
else:
    cents_per_kWh = 0.136928
total = daily_use_in_kwh * number_of_billing_days * cents_per_kWh
print("Estimated bill: ${:.2f}" .format(total))
