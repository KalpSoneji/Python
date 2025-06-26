import random

def scramble(word):
    chars = list(word)
    random.shuffle(chars)
    return "".join(chars)

def play_game(*words, word_dict=None, rounds=5, hint=False):
    print("\nWelcome to Word Scramble Game!")
    print("Try to unscramble the word. Type 'exit' if you're done.\n")
    
    score = 0
    selected = random.sample(words, k=rounds)

    for w in selected:
        mixed = scramble(w)
        print(f"Scrambled word: {mixed}")
        if hint and word_dict:
            print(f"Hint: {word_dict.get(w, 'No hint available')}")
        attempt = input("Your guess: ").strip().lower()
        if attempt == 'exit':
            break
        if attempt == w:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! It was: {w}\n")

    return score, len(selected)

def main_scramble():
    word_list = ("python", "function", "variable", "lambda", "string", "tuple", "dictionary", "loop", "integer", "float", "boolean", "list")

    helper = {
        "python": "Popular programming language",
        "function": "Reusable block of code",
        "variable": "Used to store values",
        "lambda": "Anonymous function",
        "string": "Text data type",
        "tuple": "Immutable sequence",
        "dictionary": "Key-value pair structure",
        "loop": "Used to repeat actions",
        "integer": "Whole number type",
        "float": "Decimal number type",
        "boolean": "True or False",
        "list": "Mutable sequence"
    }

    result, total_rounds = play_game(*word_list, word_dict=helper, rounds=7, hint=True)
    print(f"\nGame Over. Final Score: {result}/{total_rounds}")

main_scramble()
