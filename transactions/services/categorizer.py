CATEGORY_KEYWORDS = {
    "Food": ["mcdonalds", "kfc", "burger", "pizza", "restaurant", "eat", "coffee"],
    "Transport": ["taxi", "uber", "bus", "metro", "train", "transport", "aero"],
    "Entertainment": ["cinema", "netflix", "games", "movie", "theater"],
    "Utilities": ["electricity", "water", "gas", "internet", "phone", "mobile"],
}


def categorize(description: str, merchant: str = "") -> str:
    text = f"{description} {merchant}".lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return category
    return "Other"
