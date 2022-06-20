# usage python3 techstack.py > ./../src/data/attributeLists.jsx

from os import listdir

files = listdir('sublists')
y = {}

for file in files:
    with open(f"sublists/{file}") as file:
        for line in file:
            if len(line) >= 1:
                if "##" in line or "{{" in line:
                    pass
                else:
                    x= line.strip()
                    if len(x) > 0:
                        z=x.lower()
                        y[z] = x


ordered = list(y.keys())
ordered.sort()
for item in ordered:
    print(y[item])