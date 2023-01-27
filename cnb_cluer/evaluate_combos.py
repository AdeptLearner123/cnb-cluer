from config import SCENARIOS, GENERATED_CLUES, GENERATED_CLUE_GUESSES

from argparse import ArgumentParser
import yaml
import os
import itertools

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-f", nargs="+", required=True)
    args = parser.parse_args()
    return args.f


def main():
    file_names = parse_args()

    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())

    with open(GENERATED_CLUE_GUESSES, "r") as file:
        scenario_guesses = yaml.safe_load(file.read())

    model_clues = dict()

    for file_name in file_names:
        file_path = os.path.join(GENERATED_CLUES, f"{file_name}.yaml")

        with open(file_path, "r") as file:
            model_clues[file_name] = yaml.safe_load(file.read())
    
    model_corrects = dict()
    for model, clues in model_clues.items():
        model_corrects[model] = dict()
        for scenario_id, clue in clues.items():
            guesses = scenario_guesses[scenario_id][clue]
            model_corrects[model][scenario_id] = set(guesses) == set(scenarios[scenario_id]["pos"])

    combo_accuracies = dict()

    for i in range(1, len(model_clues) + 1):
        for models in itertools.combinations(model_clues.keys(), i):
            combo_name = str(i) + "_" + ", ".join(models)
            
            correct = 0
            for scenario_id, scenario in scenarios.items():
                if any([ model_corrects[model][scenario_id] for model in models ]):
                    correct += 1
            
            accuracy = correct / len(scenarios)
            combo_accuracies[combo_name] = accuracy

    combos_sorted = sorted(combo_accuracies.keys(), key=combo_accuracies.get)

    for combo_name in combos_sorted:
        print(combo_name, combo_accuracies[combo_name])


if __name__ == "__main__":
    main()