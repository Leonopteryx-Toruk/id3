#ID3

This project implements id3 (Iterative Dichotomiser 3) decision tree algorithm. The following is the application of our code to the very famous tennis example.

# Example of use

python DecisionTree.py "Examples\tennis.csv" ";" "Play Tennis"

path Examples\tennis.csv
separator ;
target_column Play Tennis
     Outlook  Temp Humidity    Wind Play Tennis
0      Sunny   Hot     High    Weak          No
1      Sunny   Hot     High  Strong          No
2   Overcast   Hot     High    Weak         Yes
3       Rain  Mild     High    Weak         Yes
4       Rain  Cool   Normal    Weak         Yes
5       Rain  Cool   Normal  Strong          No
6   Overcast  Cool   Normal  Strong         Yes
7      Sunny  Mild     High    Weak          No
8      Sunny  Cool   Normal    Weak         Yes
9       Rain  Mild   Normal    Weak         Yes
10     Sunny  Mild   Normal  Strong         Yes
11  Overcast  Mild     High  Strong         Yes
12  Overcast   Hot   Normal    Weak         Yes
13      Rain  Mild     High  Strong          No

Outlook = Overcast: Yes
Outlook = Rain
|       Wind = Strong: No
|       Wind = Weak: Yes
Outlook = Sunny
|       Humidity = High: No
|       Humidity = Normal: Yes