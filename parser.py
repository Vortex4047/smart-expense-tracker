import re

def parse_expense(text):
    amount_match = re.findall(r'\d+\.\d{2}', text)
    amount = max(map(float, amount_match)) if amount_match else 0.0

    lines = text.split('\n')
    merchant = lines[0] if lines else "Unknown"
    date_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
    date = date_match.group() if date_match else "Unknown"

    return {
        "date": date,
        "merchant": merchant.strip(),
        "amount": amount,
        "category": auto_categorize(merchant)
    }

def auto_categorize(merchant):
    merchant = merchant.lower()
    if "pizza" in merchant or "food" in merchant:
        return "Food"
    elif "uber" in merchant or "ola" in merchant:
        return "Transport"
    elif "medical" in merchant or "pharma" in merchant:
        return "Health"
    return "Other"
