import re
String = '1XA1Xb1Xc1Ya'
s = '1P17M'
print(re.findall(r'[0-9][A-Z][a-z]',String))
metal_num = re.search(r'\d+',re.search(r'\d+M',s).group())
print(metal_num)