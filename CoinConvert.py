Money = {
    "USD": 1, #American dollars
    "EUR": 0.9672, #Euro
    "GBP": 0.8133, #UK pound
    "INR": 86.3432, #Indian rupee
    "CAD": 1.4314, #Canadian dollar
    "AUD": 1.6024, #Australian dollar
    "JPY": 156.1044, #Japanese yen
    "CHF": 0.91, #Swiss franc
    "RUB": 102.6768, #Russian Rubles
    "NZD": 1.7726, #New Zealand dollar
    "ZAR": 18.7693, #South African Rand
    "BGN": 1.8913, #Bulgarian Lev
    "SGD": 1.3636, #Singapore dollar
    "HKD": 7.7847, #Hong Kong dollar
    "SEK": 11.1129, #Swedish crown
    "THB": 34.535, #Thai Baht
    "HUF": 397.7833, #Hungarian Forint
    "CNY": 7.3296, #Chinese Renminbi
    "NOK": 11.3061, #Norwegian Koruna
    "MXN": 20.4486 #Mexican peso
}

base_currency = input("Entry the base currency :")
sum_entry = int(input("Entrer the sum of exchange :"))
target_currency = input("Entry the target currency :")

base = Money[base_currency]
target = Money[target_currency]

exchange = ((target * Money["USD"]) / base) * sum_entry

print(f"{sum_entry} {base_currency} is equal to {exchange} {target_currency}")
