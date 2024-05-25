from random import shuffle

dic = {
    "wonderful":"merveilleuse",
    "joyful":"joyeuse",
    "sad":"triste",
    "boring":"ennuyeuse",
    "gentle":"douce",
    "original":"originale",
    "pleasant":"agréable",
    "dynamic":"dynamique",
    "classic":"classique"
}

words = list(dic)
shuffle(words)

score = 0

mistakes = []

for word in words:
    inp = input(f"What is the translation of {word}? ")
    if inp == dic[word]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        mistakes.append([word, inp, dic[word]])

print(f"You got {round(score/len(words)*100)}%.")
print("Here are your mistakes:")

for mistake in mistakes:
    print(f"{mistake[0]}: {mistake[1]} --> {mistake[2]}")