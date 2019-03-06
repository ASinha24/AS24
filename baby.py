import random
questions=["why earth is round in shape?: ", "why sky is blue?: ", "why papa go to office?: ", "where are all the dinosaurs?: "]
question=random.choice(questions)
answer=input(question).strip()
while answer != "just because!":
    answer=input("why").strip()
print("oh okay.....")
