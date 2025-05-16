from transactions.services.constants import CATEGORY_KEYWORDS


def categorize(description: str, merchant: str = "") -> str:
    text = f"{description} {merchant}".lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return category
    return "Other"
