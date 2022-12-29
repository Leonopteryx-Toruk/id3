import pandas as pd
import numpy as np
import math
import copy
from statistics import mode

def most_common(List):
    return (mode(List))

# questo metodo calcola l'entropia sulla colonna target
def get_entropy(df, target_attribute):
    total_number = df.shape[0]
    yes_number = np.sum(df.loc[:, target_attribute] == "Yes")
    p = yes_number / total_number
    if p == 1.0 or p == 0.0:
        return 0
    entropy = -p*math.log2(p) - (1-p)*math.log2(1-p)
    return entropy

# questo metodo effettua il filtro dei dataframe sulla base del valore di una colonna
def filter_df(df, column_name, value):
    df_filtered = df.loc[df.loc[:, column_name] == value, :]
    return df_filtered

def id3(df, columns, target_attribute, level=0):
    if target_attribute in columns:
        columns.remove(target_attribute)

    # print("columns received", columns)
    information_gain = dict()
    initial_entropy = get_entropy(df, target_attribute)
    # print("initial_entropy", initial_entropy)
    for i in range(len(columns)):
        column = columns[i]
        unique_values = np.unique(df.loc[:, column])
        for j in range(len(unique_values)):
            value = unique_values[j]
            # select records for which the column column has the value value
            df_filtered = filter_df(df, column, value)
            if column not in information_gain:
                information_gain[column] = initial_entropy
            # calculate the entropy for the filtered dataframe
            entropy_vi = get_entropy(df_filtered, target_attribute)
            # print("value", value)
            # print("entropy_vi", entropy_vi)
            information_gain[column] -= (df_filtered.shape[0] / df.shape[0]) * entropy_vi
    # print(information_gain)

    max = -1
    best_col = ""
    for col in information_gain:
        if information_gain[col] > max:
            best_col = col
            max = information_gain[col]
    # print("column {column} reached maximum information gain {gain}".format(column=best_col, gain=max))

    best_col_values = np.unique(df.loc[:, best_col])
    for i in range(len(best_col_values)):
        best_col_value = best_col_values[i]
        # print("best_col", best_col)
        # print("level", level)
        for i in range(level):
            print("|", end="\t")
        print("{best_col} = {best_col_value}".format(best_col=best_col, best_col_value=best_col_value), end="")
        # print("value: " + best_col_value)
        df_filtered_vi = filter_df(df, best_col, best_col_value)
        branch_columns = copy.deepcopy(columns)
        branch_columns.remove(best_col)
        next_level = level + 1
        # print("columns passed", branch_columns)

        if len(branch_columns) == 0 or len(list(np.unique(df_filtered_vi.loc[:, target_attribute]))) == 1:
            prediction = most_common(df_filtered_vi[target_attribute].values)
            print(": {prediction}".format(prediction=prediction))
        else:
            print()
            id3(df_filtered_vi, branch_columns, target_attribute, next_level)


if __name__=="__main__":
    dataframe = pd.read_csv("Examples/titanic.csv", sep=",", index_col=False)

    print("dataframe", dataframe)

    columns = dataframe.columns
    for i in range(len(columns)):
        column = columns[i]
        dataframe[column] = dataframe[column].apply(str)

    columns = list(dataframe.columns)
    id3(dataframe, columns, "Survival")