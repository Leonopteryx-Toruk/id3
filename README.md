# ID3

This project implements id3 (Iterative Dichotomiser 3) decision tree algorithm. The following is the application of our code to the very famous tennis example.<br /><br />

This algorithm trains an id3 decision tree algorithm on a dataset given as input by the user. Eventually, this algorithm prints the strcture of the trained tree.<br />

The dataset must be a csv table where each column represents a feature and the class must be present as a column. This algorithm works only with categorical attributes: each numerical attribute will be converted into string and treated as categorical. <br />

## Example of use

It is possible to start the training with the following syntax: <br />

python DecisionTree.py path_to_csv csv_separator target_attribute<br />

<ul>
<li>path_to_csv: path to the dataset (represented as a csv file)</li>
<li>csv_separator: separator character between csv columns</li>
<li>target_attribute: name of the column that contains the class of each row</li>
</ul>

The following example explains how to run the training on the famous tennis dataset <br />

python DecisionTree.py "Examples\tennis.csv" ";" "Play Tennis"<br />

path Examples\tennis.csv<br />separator ;<br />target_column Play Tennis<br />     Outlook  Temp Humidity    Wind Play Tennis<br />0      Sunny   Hot     High    Weak          No<br />1      Sunny   Hot     High  Strong          No<br />2   Overcast   Hot     High    Weak         Yes<br />3       Rain  Mild     High    Weak         Yes<br />4       Rain  Cool   Normal    Weak         Yes<br />5       Rain  Cool   Normal  Strong          No<br />6   Overcast  Cool   Normal  Strong         Yes<br />7      Sunny  Mild     High    Weak          No<br />8      Sunny  Cool   Normal    Weak         Yes<br />9       Rain  Mild   Normal    Weak         Yes<br />10     Sunny  Mild   Normal  Strong         Yes<br />11  Overcast  Mild     High  Strong         Yes<br />12  Overcast   Hot   Normal    Weak         Yes<br />13      Rain  Mild     High  Strong          No<br /><br />Outlook = Overcast: Yes<br />Outlook = Rain<br />|&ensp;&ensp;&ensp;&nbsp;Wind = Strong: No<br />|&ensp;&ensp;&ensp;&nbsp;Wind = Weak: Yes<br />Outlook = Sunny<br />|&ensp;&ensp;&ensp;&nbsp;Humidity = High: No<br />|&ensp;&ensp;&ensp;&nbsp;Humidity = Normal: Yes