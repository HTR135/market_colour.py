import requests  # Connects to News API and collects articles

# Personal API and Base_URL
API_KEY = "6b042f73df204d6b821c23a2df1be311"  # My personal API NewsAPI gave me
BASE_URL = "https://newsapi.org/v2/everything"  # NewsAPI endpoint

# Keywords List. This can be altered and changed to preference
keywords = [
    # Macro/markets
    "EM", "DM", "emerging market", "emerging markets", "developed market", "developed markets",

    # Credit and Bonds
    "credit", "credit spread", "credit spreads", "bond", "bonds", "local bond", "local bonds",
    "eurobond", "eurobonds", "investment grade", "IG", "high yield", "HY", "contingent capital",

    # Duration, Yields, etc.
    "duration", "maturity", "YTM", "swap curve", "swap curves", "yield curve", "inversion", "term premium",

    # CBs, Monetary policy (interest rates)
    "interest rate", "interest rates", "interest rate swap", "interest rate swaps", "IRS",
    "BOE", "FED", "ECB", "BOJ", "Bank of England", "Bank of Japan", "Bank of America", "Bank of Canada",
    "FOMC", "Fed minutes",

    # Government bonds and benchmarks
    "US treasuries", "UST", "USTS", "10y", "2y", "5y", "30y", "bunds", "gilts", "jgb", "sovereign debt",

    # Important news
    "CPI", "PCE", "NFP", "payrolls", "ISM", "PMI",
    "unemployment rate", "GDP", "recession",

    # Benchmarks for portfolios
    "EMBIGD", "GBIEM", "JPM EMBI",

    # Risk/volatility
    "VIX",

    # Derivatives
    "swaps", "calls", "puts", "options", "futures", "derivatives", "CDS",

    # Equities
    "equities", "stocks", "equity markets", "dark pool", "lit pool",

    # FX
    "foreign exchange", "FX", "fx forwards", "cross currency swap", "Eurex", "CME", "ICE",

    # Ratings
    "moody's", "s&p", "fitch",

    # Currencies
    "usd", "eur", "jpy", "gbp", "cny", "brl", "inr", "mxn", "zar", "chf", "dollar", "pound", "euro",
]

# Keyword Checking Function


def keyword_found(text):
    # makes everything lowercase to avoid missing articles due to caps sensitivity
    text = text.lower()
    for keyword in keywords:
        if keyword.lower() in text:
            return True  # as soon as a keyword of mine is found, function returns true and stops checking
    return False


# Set Parameters for NewsAPI
parameters = {
    "q": "sovereign bonds",  # Most important line IMO. This specifies the news captured
    "language": "en",       # To make sure we get news in English
    "pageSize": 100,        # Max articles per request
    "apiKey": API_KEY
}

# Send Request to NewsAPI
result = requests.get(BASE_URL, params=parameters)

# Process the Articles
data = result.json()
articles = data["articles"]
print("Total articles fetched:", len(articles))

# Filter for articles containing keywords
matched_articles = []

for article in articles:
    # "" is imporant to make sure we get a string instead of a 'None' response
    title = str(article.get("title") or "")
    description = str(article.get("description") or "")
    content = title + " " + description

    if keyword_found(content):
        matched_articles.append(article)

print("Articles matching keywords:", len(matched_articles))

# Print Matching Articles
count = 1
for article in matched_articles:
    title = article.get("title", "No title available.")
    description = article.get("description", "No description available.")
    url = article.get("url", "No URL available.")

    # \n is used for readability, by providing space after each article
    print("\n[" + str(count) + "] " + title)
    print(description)
    print(url)
    count = count + 1
