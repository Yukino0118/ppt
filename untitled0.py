import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import re
import pandas as pd

df = pd.read_excel('1.xlsx', header = None,index_col=None, sheet_name = '1')
print(df)
fig = plt.figure(figsize=(5,3))

column_labels=["B","C"]
plt.axis('off')
plt.grid('off')
tb = plt.table(cellText=df.values,cellLoc='center', loc="center")
#set font bold and color
for (row, col), cell in tb.get_celld().items():
    if (row == 0) or (col == 0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))
        cell.set_facecolor("#56b5fd")

tb.scale(1,2)
plt.savefig('filename.png', dpi=300)

