import random

def get_random_question(level='easy'):
    ops = ['+', '-', '*']  
    chosen_op = random.choice(ops)

    if level == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 'medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    else:
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)

    if chosen_op == '+':
        correct_ans = num1 + num2
    elif chosen_op == '-':
        correct_ans = num1 - num2
    else:
        correct_ans = num1 * num2

    question_text = f"{num1} {chosen_op} {num2}"
    return question_text, correct_ans

def run_quiz(*player_names, **options):
    print("Welcome to Math Quiz Battle!\n")
    
    level = options.get('difficulty', 'easy')
    total_rounds = options.get('rounds', 5)
    
    print(f"Participants: {', '.join(player_names)}")
    print(f"Mode: {level.capitalize()} | Total Rounds: {total_rounds}\n")

    scores = {}
    for name in player_names:
        scores[name] = 0

    for round_num in range(1, total_rounds + 1):
        print(f"Rpund {round_num}: ")
        for pname in player_names:
            q, actual_answer = get_random_question(level)
            print(f"{pname}, What’s: {q} ?")

            try:
                response = int(input("Your answer: "))
                if response == actual_answer:
                    print("Nice one!\n")
                    scores[pname] += 1
                else:
                    print(f"Oops, the answer was {actual_answer}\n")
            except ValueError:
                print(f"Answer was {actual_answer}\n")

    print("=== Final Scores ===")
    for who, pts in scores.items():
        print(f"{who}: {pts} point(s)")

    winner = max(scores, key=lambda k: scores[k])
    print(f"\nWinner: {winner}")

run_quiz("Kalp", "Vidhi", difficulty="medium", rounds=5)
