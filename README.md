# ID3

This project implements id3 (Iterative Dichotomiser 3) decision tree algorithm. The following is the application of our code to the very famous tennis example.<br /><br />

# Example of use

python DecisionTree.py "Examples\tennis.csv" ";" "Play Tennis"<br />

path Examples\tennis.csv<br />separator ;<br />target_column Play Tennis<br />     Outlook  Temp Humidity    Wind Play Tennis<br />0      Sunny   Hot     High    Weak          No<br />1      Sunny   Hot     High  Strong          No<br />2   Overcast   Hot     High    Weak         Yes<br />3       Rain  Mild     High    Weak         Yes<br />4       Rain  Cool   Normal    Weak         Yes<br />5       Rain  Cool   Normal  Strong          No<br />6   Overcast  Cool   Normal  Strong         Yes<br />7      Sunny  Mild     High    Weak          No<br />8      Sunny  Cool   Normal    Weak         Yes<br />9       Rain  Mild   Normal    Weak         Yes<br />10     Sunny  Mild   Normal  Strong         Yes<br />11  Overcast  Mild     High  Strong         Yes<br />12  Overcast   Hot   Normal    Weak         Yes<br />13      Rain  Mild     High  Strong          No<br /><br />Outlook = Overcast: Yes<br />Outlook = Rain<br />|&nbsp;&nbsp;&nbsp;Wind = Strong: No<br />|&nbsp;&nbsp;&nbsp;Wind = Weak: Yes<br />Outlook = Sunny<br />|&nbsp;&nbsp;&nbsp;Humidity = High: No<br />|&nbsp;&nbsp;&nbsp;Humidity = Normal: Yes