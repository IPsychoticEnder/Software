subject = {"Computing": 401, "Biology": 211, "Electronics": 75}

print("What is your name?")
name = input()
print("What are you studying?")
user_subject = input()

if user_subject in subject:
    print(f"Hello {name}, go to room {subject[user_subject]}")
else:
    print("I dont know what class this is in.")
