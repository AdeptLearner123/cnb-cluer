from argparse import ArgumentParser

from tqdm import tqdm
import os

from .utils import get_model
from config import SCENARIOS, GENERATED_CLUES
import yaml

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-m", type=str, required=True)
    args = parser.parse_args()
    return args.m


def main():
    model_name = parse_args()
    model = get_model(model_name)

    output_path = os.path.join(GENERATED_CLUES, f"{model_name}_clues.yaml")

    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())

    clues = dict()
    if os.path.exists(output_path):
        with open(output_path, "r") as file:
            clues = yaml.safe_load(file.read())

    missing_scenarios = set(scenarios.keys()) - set(clues.keys())

    for key in tqdm(missing_scenarios):
        clue = model.generate_clue(scenarios[key]["pos"], scenarios[key]["neg"])
        clues[key] = clue

        with open(output_path, "w+") as file:
            file.write(yaml.dump(clues))
        

    model.print_usage()