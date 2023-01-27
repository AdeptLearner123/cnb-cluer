from argparse import ArgumentParser

from config import SCENARIOS, GENERATED_CLUES, GENERATED_CLUE_GUESSES, SCENARIOS_DATA
import yaml
import os
import random
from collections import defaultdict, Counter

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-f", required=True)
    parser.add_argument("-r", action="store_true")
    args = parser.parse_args()
    return args.f, args.r


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


def evaluate_clue(scenario_id, clue, scenarios, guesses):
    if scenario_id not in guesses:
        guesses[scenario_id] = dict()
    scenario_guesses = guesses[scenario_id]
    
    if clue not in scenario_guesses:
        scenario_guesses[clue] = prompt_guesses(clue, scenarios[scenario_id])
        with open(GENERATED_CLUE_GUESSES, "w+") as file:
            file.write(yaml.dump(guesses, default_flow_style=None))
    
    guessed_words = scenario_guesses[clue]
    return set(guessed_words) == set(scenarios[scenario_id]["pos"])


def main():
    file_name, review = parse_args()
    file_path = os.path.join(GENERATED_CLUES, f"{file_name}.yaml")
    scenario_clues = defaultdict(lambda: [])

    with open(file_path, "r") as file:
        for scenario_id, clue in yaml.safe_load(file.read()).items():
            scenario_clues[scenario_id].append(clue)
    
    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())
    
    with open(SCENARIOS_DATA, "r") as file:
        scenarios_data = yaml.safe_load(file.read())

    with open(GENERATED_CLUE_GUESSES, "r") as file:
        guesses = yaml.safe_load(file.read())
    
    if guesses is None:
        guesses = dict()

    corrects = Counter()
    totals = Counter()
    incorrects = []
    for i, scenario_id in enumerate(scenarios):
        print("Scenario", i)

        keys = ["all"]
        if scenarios_data[scenario_id]["is_easy"]:
            keys.append("easy")
        else:
            keys.append("hard")

        if evaluate_clue(scenario_id, clue, scenarios, guesses):
            for key in keys:
                corrects[key] += 1
        else:
            scenario = scenarios[scenario_id]
            incorrects.append({
                "pos": scenario["pos"],
                "clue": scenario_clues[scenario_id]
            })
        
        for key in keys:
            totals[key] += 1

    for key in corrects:
        print(f"{key}: {corrects[key]} / {totals[key]} = {corrects[key] / totals[key]}")
    
    if review:
        print(yaml.dump(incorrects, default_flow_style=None))


if __name__ == "__main__":
    main()