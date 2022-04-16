import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import re

fig = plt.figure(figsize=(6,2))
data=[[1,2,3],
      [5,6,7],
      [8,9,10]]
column_labels=["Column 1", "Column 2", "Column 3"]
plt.axis('off')
plt.grid('off')
tb = plt.table(cellText=data,colLabels=column_labels,cellLoc='center', loc="center")
#set font bold and color
for (row, col), cell in tb.get_celld().items():
    if (row == 0) or (col == 0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))
        cell.set_facecolor("#56b5fd")

tb.scale(1,2)
plt.savefig('filename.png', dpi=300)

