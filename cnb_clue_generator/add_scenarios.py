import yaml
import random
from uuid import uuid4
import csv

NEW_SCENARIOS = "word_pair_tryouts.csv"
SCENARIOS = "scenarios.yaml"
CARDWORDS = "cardwords.txt"


def main():
    add_negs()


def add_negs():
    with open(CARDWORDS, "r") as file:
        cardwords = file.read().splitlines()

    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())
    
    print("Scenarios", len(scenarios))

    scenarios_missing_neg = [ scenario for scenario in scenarios.values() if "neg" not in scenario ]

    for i, scenario in enumerate(scenarios_missing_neg):
        possible_negs = set(cardwords).difference(set(scenario["pos"]))
        neg_words = random.sample(possible_negs, 3)
        print(i, len(scenarios_missing_neg))
        print(scenario["pos"], scenario["clue"])
        print(neg_words)
        confirm = input("good?:")
        if confirm == "y":
            scenario["neg"] = neg_words
        
        with open(SCENARIOS, "w") as file:
            yaml.dump(scenarios, file, default_flow_style=None)


def add_scenarios():
    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())
    
    print("Scenarios", len(scenarios))
    
    with open(NEW_SCENARIOS, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for word1, word2, clue, _, _ in reader:
            scenarios[str(uuid4())] = {
                "pos": [word1, word2],
                "clue": clue
            }

    print("New scenarios", len(scenarios))

    with open(SCENARIOS, "w") as file:
        yaml.dump(scenarios, file, default_flow_style=None)



if __name__ == "__main__":
    main()