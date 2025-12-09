from summa.summarizer import summarize
from summa import keywords

# Read text from file
with open("Labs/lab4/part3/text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Summarize - define length as a proportion of the text
print("Summary (20% ratio):")
print(summarize(text, ratio=0.2))

# Summarize - define length by word count
print("\nSummary (50 words):")
print(summarize(text, words=50))

# Extract keywords
print("\nKeywords:")
print(keywords.keywords(text))

# Extract top 3 keywords
print("\nTop 3 Keywords:")
print(keywords.keywords(text, words=3))

