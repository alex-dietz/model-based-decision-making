from ema_workbench.em_framework import sample_uncertainties
from problem_formulation import get_model_for_problem_formulation

if __name__ == "__main__":
    n_scenarios = 10
    problem_formulation_id = 6
    model, steps = get_model_for_problem_formulation(problem_formulation_id)
    scenarios = sample_uncertainties(model, n_scenarios)
    print(scenarios)
