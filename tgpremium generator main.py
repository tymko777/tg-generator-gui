import random

def generate_giftcode_link():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890-_"
    link = "https://t.me/giftcode/"
    for i in range(27):
        link += random.choice(characters)
    return link

for _ in range(10):
    print(generate_giftcode_link())
