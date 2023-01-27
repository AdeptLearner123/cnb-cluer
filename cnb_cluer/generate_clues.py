from argparse import ArgumentParser

from tqdm import tqdm
import os

from .utils import get_clue_giver
from config import SCENARIOS, GENERATED_CLUES, GENERATED_CLUES_NOTES
import yaml

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-m", type=str, required=True)
    args = parser.parse_args()
    return args.m


def main():
    model_name = parse_args()
    model = get_clue_giver(model_name)

    output_path = os.path.join(GENERATED_CLUES, f"{model_name}_clues.yaml")
    notes_path = os.path.join(GENERATED_CLUES_NOTES, f"{model_name}_clues.yaml")

    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())

    clues = dict()
    if os.path.exists(output_path):
        with open(output_path, "r") as file:
            clues = yaml.safe_load(file.read())

    scenario_notes = dict()
    if os.path.exists(notes_path):
        with open(notes_path, "r") as file:
            scenario_notes = yaml.safe_load(file.read())

    missing_scenarios = [ scenario_id for scenario_id in scenarios if scenario_id not in clues ]

    for key in tqdm(missing_scenarios):
        clue, notes = model.generate_clue(scenarios[key]["pos"], scenarios[key]["neg"])
        clues[key] = clue
        scenario_notes[key] = notes

        with open(output_path, "w+") as file:
            file.write(yaml.dump(clues))
        
        with open(notes_path, "w+") as file:
            file.write(yaml.dump(scenario_notes, default_style=None))        
        
        print(model.get_usage())
        break
