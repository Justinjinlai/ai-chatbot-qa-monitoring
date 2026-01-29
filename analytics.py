import csv
from collections import Counter

sentiment_counter = Counter()

with open("conversations.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        response = row["bot_response"].lower()

        if "sorry" in response or "help" in response:
            sentiment_counter["positive"] += 1
        elif "restart" in response or "error" in response or "broken" in response:
            sentiment_counter["negative"] += 1
        else:
            sentiment_counter["neutral"] += 1

print("\nAI OPERATIONS SUMMARY")
print("---------------------")
for sentiment, count in sentiment_counter.items():
    print(f"{sentiment.capitalize()} responses: {count}")
  
