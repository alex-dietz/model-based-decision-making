"""
Created on Sun Oct 29 15:55:19 2017

@author: Gelderlans Province
"""

import pandas as pd





def tidy_results_formulation3(results):
    """Creates and returns a data frame that:
         1) Includes the information of the scenarios and outcomes
         2) Creates a new column with the Dike ring number 
         and melts all the columns that have different values for each Dike ring
       """

    



    return melted_df


def tidy_results(results,formulation):
    """Creates and returns a data frame that:
         1) Includes the information of the scenarios and outcomes
         2) Creates a new column with the Dike ring number 
         and melts all the columns that have different values for each Dike ring
       """

    if formulation == 6:
        experiments, outcomes = results
        
        results_df = pd.concat([pd.DataFrame(experiments),pd.DataFrame(outcomes)], axis=1)

        cols_to_melt=column_dict = {
        'Bmax': ['A.1_Bmax', 'A.2_Bmax', 'A.3_Bmax', 'A.4_Bmax', 'A.5_Bmax'],
        'Brate': ['A.1_Brate', 'A.2_Brate', 'A.3_Brate', 'A.4_Brate', 'A.5_Brate'],
        'pfail': ['A.1_pfail', 'A.2_pfail', 'A.3_pfail', 'A.4_pfail', 'A.5_pfail'],
        'RfR 0': ['0_RfR 0', '1_RfR 0', '2_RfR 0', '3_RfR 0', '4_RfR 0'],
        'RfR 1': ['0_RfR 1', '1_RfR 1', '2_RfR 1', '3_RfR 1', '4_RfR 1'],
        'RfR 2': ['0_RfR 2', '1_RfR 2', '2_RfR 2', '3_RfR 2', '4_RfR 2'],
        'DikeIncrease 0': ['A.1_DikeIncrease 0', 'A.2_DikeIncrease 0', 'A.3_DikeIncrease 0', 'A.4_DikeIncrease 0', 'A.5_DikeIncrease 0'],
        'DikeIncrease 1': ['A.1_DikeIncrease 1', 'A.2_DikeIncrease 1', 'A.3_DikeIncrease 1', 'A.4_DikeIncrease 1', 'A.5_DikeIncrease 1'],
        'DikeIncrease 2': ['A.1_DikeIncrease 2', 'A.2_DikeIncrease 2', 'A.3_DikeIncrease 2', 'A.4_DikeIncrease 2', 'A.5_DikeIncrease 2'],
        'Dike Investment Costs': ['A.1_Dike Investment Costs', 'A.2_Dike Investment Costs', 'A.3_Dike Investment Costs', 'A.4_Dike Investment Costs', 'A.5_Dike Investment Costs'],
        'Expected Annual Damage': ['A.1_Expected Annual Damage', 'A.2_Expected Annual Damage', 'A.3_Expected Annual Damage', 'A.4_Expected Annual Damage', 'A.5_Expected Annual Damage'],
        'Expected Number of Deaths': ['A.1_Expected Number of Deaths', 'A.2_Expected Number of Deaths', 'A.3_Expected Number of Deaths', 'A.4_Expected Number of Deaths', 'A.5_Expected Number of Deaths']
        }

        melted_df=pd.melt(results_df, id_vars=['A.0_ID flood wave shape', 'discount rate 0', 'discount rate 1', 'discount rate 2','EWS_DaysToThreat', 'scenario', 'policy', 'model', 'RfR Total Costs', 'Expected Evacuation Costs'], 
                        value_vars=cols_to_melt["Bmax"],
                        value_name="Bmax", 
                        var_name="Dike ring"
            )

        melted_df["Dike ring"]=melted_df['Dike ring'].str[:3]
        melted_df=melted_df.drop(["Bmax"],axis=1)

        for n in cols_to_melt:
            melted_df_n=pd.melt(results_df, id_vars=[], value_vars=	cols_to_melt[n],value_name=n, var_name="Dike ring"
            )
            melted_df_n=melted_df_n.drop(["Dike ring"],axis=1)
            melted_df = pd.concat([melted_df,melted_df_n],axis=1)
    
    
    elif formulation == 3:
        experiments, outcomes = results
        
        results_df = pd.concat([pd.DataFrame(experiments),pd.DataFrame(outcomes)], axis=1)

        cols_to_melt=column_dict = {
        'Bmax': ['A.1_Bmax', 'A.2_Bmax', 'A.3_Bmax', 'A.4_Bmax', 'A.5_Bmax'],
        'Brate': ['A.1_Brate', 'A.2_Brate', 'A.3_Brate', 'A.4_Brate', 'A.5_Brate'],
        'pfail': ['A.1_pfail', 'A.2_pfail', 'A.3_pfail', 'A.4_pfail', 'A.5_pfail'],
        'RfR 0': ['0_RfR 0', '1_RfR 0', '2_RfR 0', '3_RfR 0', '4_RfR 0'],
        'RfR 1': ['0_RfR 1', '1_RfR 1', '2_RfR 1', '3_RfR 1', '4_RfR 1'],
        'RfR 2': ['0_RfR 2', '1_RfR 2', '2_RfR 2', '3_RfR 2', '4_RfR 2'],
        'DikeIncrease 0': ['A.1_DikeIncrease 0', 'A.2_DikeIncrease 0', 'A.3_DikeIncrease 0', 'A.4_DikeIncrease 0', 'A.5_DikeIncrease 0'],
        'DikeIncrease 1': ['A.1_DikeIncrease 1', 'A.2_DikeIncrease 1', 'A.3_DikeIncrease 1', 'A.4_DikeIncrease 1', 'A.5_DikeIncrease 1'],
        'DikeIncrease 2': ['A.1_DikeIncrease 2', 'A.2_DikeIncrease 2', 'A.3_DikeIncrease 2', 'A.4_DikeIncrease 2', 'A.5_DikeIncrease 2'],
        'Total costs': ['A.1 Total Costs', 'A.2 Total Costs', 'A.3 Total Costs', 'A.4 Total Costs', 'A.5 Total Costs'],
        'Expected Number of Deaths': ['A.1_Expected Number of Deaths', 'A.2_Expected Number of Deaths', 'A.3_Expected Number of Deaths', 'A.4_Expected Number of Deaths', 'A.5_Expected Number of Deaths']
        }

        melted_df=pd.melt(results_df, id_vars=['A.0_ID flood wave shape', 'discount rate 0', 'discount rate 1', 'discount rate 2','EWS_DaysToThreat', 'scenario', 'policy', 'model', 'RfR Total Costs', 'Expected Evacuation Costs'], 
                        value_vars=cols_to_melt["Bmax"],
                        value_name="Bmax", 
                        var_name="Dike ring"
            )

        melted_df["Dike ring"]=melted_df['Dike ring'].str[:3]
        melted_df=melted_df.drop(["Bmax"],axis=1)

        for n in cols_to_melt:
            melted_df_n=pd.melt(results_df, id_vars=[], value_vars=	cols_to_melt[n],value_name=n, var_name="Dike ring"
            )
            melted_df_n=melted_df_n.drop(["Dike ring"],axis=1)
            melted_df = pd.concat([melted_df,melted_df_n],axis=1)

    return melted_df

#'Total costs': ['A.1 Total Costs', 'A.2 Total Costs', 'A.3 Total Costs', 'A.4 Total Costs', 'A.5 Total Costs'],


def merge_results(results):
    """creates a single DataFrame that includes the information of the scenarios and outcomes"""

    experiments, outcomes = results
    
    results_df = pd.concat([pd.DataFrame(experiments),pd.DataFrame(outcomes)], axis=1)

    return results_df