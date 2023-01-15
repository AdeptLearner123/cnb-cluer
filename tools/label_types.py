import yaml
import os

from config import SCENARIOS, SCENARIOS_DATA

def main():
    scenario_data = dict()
    if os.path.exists(SCENARIOS_DATA):
        with open(SCENARIOS_DATA) as file:
            scenario_data = yaml.safe_load(file.read())

    with open(SCENARIOS) as file:
        scenarios = yaml.safe_load(file.read())
    
    for i, (scenario_id, scenario) in enumerate(scenarios.items()):
        if scenario_id not in scenario_data:
            scenario_data[scenario_id] = dict()
        
        if "is_easy" in scenario_data[scenario_id]:
            continue

        print(i)
        print(scenario["pos"], scenario["neg"])

        is_easy = input("Easy:") == "y"
        scenario_data[scenario_id]["is_easy"] = is_easy

        with open(SCENARIOS_DATA, "w+") as file:
            file.write(yaml.dump(scenario_data))


if __name__ == "__main__":
    main()