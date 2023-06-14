sample_dict = {
    "Mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"

}

while True:
    user_input = input("Enter a word in English or EXIT: ")
    if user_input == "EXIT":
        print("Bye!")
        break
    elif user_input in sample_dict:
        print("Translation:", sample_dict[user_input])
    elif user_input not in sample_dict:
        print("No match!")