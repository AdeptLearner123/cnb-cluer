from argparse import ArgumentParser

from config import SCENARIOS, GENERATED_CLUES, GUESSES
import yaml
import os
import random

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-f", type=str, required=True)
    args = parser.parse_args()
    return args.f


def prompt_guesses(clue, scenario):
    words = scenario["pos"] + scenario["neg"]
    random.shuffle(words)
    
    print("Clue:", clue)
    print(words)

    guessed_words = []
    for i in range(len(scenario["pos"])):
        guess = input(f"Word {i}:")
        if len(guess) == 0:
            break
        guessed_words.append(guess)

    if any([ word not in words for word in guessed_words ]):
        raise ValueError()
    
    return guessed_words


def evaluate_clue(scenario_id, clues, scenarios, guesses):
    clue = clues[scenario_id]

    if scenario_id not in guesses:
        guesses[scenario_id] = dict()
    scenario_guesses = guesses[scenario_id]
    
    if clue not in scenario_guesses:
        scenario_guesses[clue] = prompt_guesses(clue, scenarios[scenario_id])
        with open(GUESSES, "w+") as file:
            file.write(yaml.dump(guesses, default_flow_style=None))
    
    guessed_words = scenario_guesses[clue]
    return set(guessed_words) == set(scenarios[scenario_id]["pos"])


def main():
    file_name = parse_args()
    file_path = os.path.join(GENERATED_CLUES, f"{file_name}.yaml")

    with open(file_path, "r") as file:
        clues = yaml.safe_load(file.read())
    
    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())
    
    with open(GUESSES, "r") as file:
        guesses = yaml.safe_load(file.read())
    
    if guesses is None:
        guesses = dict()

    correct = 0
    for i, scenario_id in enumerate(scenarios):
        print("Scenario", i)
        good_clue = evaluate_clue(scenario_id, clues, scenarios, guesses)

        if good_clue:
            correct += 1
    
    print(f"Accuracy: {correct} / {len(scenarios)} = {correct / len(scenarios)}")


if __name__ == "__main__":
    main()