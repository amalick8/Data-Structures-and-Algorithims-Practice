rates = {
    "USD": 1.0,
    "EUR": 0.9,
    "JPY": 110
}

def convert(amount, currency):
    if currency not in rates:
        return f'The rate: {currency}, is not in our database'
    conversion_amount = amount * rates[currency]
    return conversion_amount
print(convert(100,'PKR'))

