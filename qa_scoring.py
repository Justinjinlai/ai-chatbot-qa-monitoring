import csv

def score_response(response):
    bad_keywords = ["restart", "wait", "error", "can't", "broken"]
    good_keywords = ["help", "sorry", "yes", "can", "fix"]

    response = response.lower()

    if any(word in response for word in bad_keywords):
        return "Needs Review"
    elif any(word in response for word in good_keywords):
        return "Good"
    else:
        return "Neutral"

print("\nAI CHATBOT QA RESULTS")
print("---------------------")

with open("conversations.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        score = score_response(row["bot_response"])
        print(f"User {row['user_id']} | Score: {score}")
