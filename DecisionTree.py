import pandas as pd
import numpy as np
import math

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
    columns.remove(target_attribute)

    if len(list(np.unique(df.loc[:, target_attribute]))) == 1:
        prediction = list(np.unique(df.loc[:, target_attribute]))[0]
        print("prediction", prediction)
        return None

    print("columns", columns)
    information_gain = dict()
    initial_entropy = get_entropy(df, target_attribute)
    # print("initial_entropy", initial_entropy)
    for i in range(len(columns)):
        column = columns[i]
        unique_values = np.unique(df.loc[:, column])
        for j in range(len(unique_values)):
            value = unique_values[j]
            df_filtered = filter_df(df, column, value)
            if column not in information_gain:
                information_gain[column] = initial_entropy
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
    print("best_col", best_col)
    print("max", max)

    best_col_values = np.unique(df.loc[:, best_col])
    for i in range(len(best_col_values)):
        best_col_value = best_col_values[i]
        print("level", level)
        print("value: " + best_col_value)
        df_filtered_vi = filter_df(df, best_col, best_col_value)
        columns = list(df.columns)
        columns.remove(best_col)
        next_level = level + 1
        id3(df_filtered_vi, columns, target_attribute, next_level)


if __name__=="__main__":
    tennis_df = pd.read_csv("tennis.csv", sep=";", index_col=False)
    columns = list(tennis_df.columns)
    id3(tennis_df, columns, "Play Tennis")