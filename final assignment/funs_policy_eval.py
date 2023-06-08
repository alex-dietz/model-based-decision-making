import pandas as pd
import ema_workbench
from ema_workbench import Policy






def create_optimization_policies(file_name, name_of_policy_batch,dike_model):
    # Read the CSV file into a DataFrame
    df = pd.read_csv("policies/" + str(file_name))
    
    # Initialize the list of optimization policies
    optimization_policies = []
    
    #Create the dictionary to make the empty policy
    def get_do_nothing_dict():
        return {l.name: 0 for l in dike_model.levers}

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the values from the row
        name_of_policy = str(name_of_policy_batch) + f"({index})"
        rfr_values = [row[f"{i}_RfR 0"] for i in range(5)]
        dike_increase_values = [row[f"A.{i}_DikeIncrease 0"] for i in range(1, 6)]
        ews_days_to_threat = row['EWS_DaysToThreat']
        
        # Create a dictionary for the policy
        policy_dict = {
            '0_RfR 0': rfr_values[0],
            '1_RfR 0': rfr_values[1],
            '2_RfR 0': rfr_values[2],
            '3_RfR 0': rfr_values[3],
            '4_RfR 0': rfr_values[4],
            'A.1_DikeIncrease 0': dike_increase_values[0],
            'A.2_DikeIncrease 0': dike_increase_values[1],
            'A.3_DikeIncrease 0': dike_increase_values[2],
            'A.4_DikeIncrease 0': dike_increase_values[3],
            'A.5_DikeIncrease 0': dike_increase_values[4],
            'EWS_DaysToThreat': ews_days_to_threat
        }
        
        # Create the optimization policy and add it to the list
        policy = Policy(name_of_policy, **dict(get_do_nothing_dict(), **policy_dict))
        optimization_policies.append(policy)
    
    return optimization_policies