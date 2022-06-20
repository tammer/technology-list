# usage python3 techstack.py > ./../src/data/attributeLists.jsx

y = {}

files=['original.txt','github.txt']
# files=['github.txt']

for file in files:
    with open(f"sublists/{file}") as file:
        for line in file:
            if len(line) >= 1:
                if "##" in line or "{{" in line:
                    pass
                else:
                    x= line.strip()
                    z=x.lower()
                    y[z] = x


ordered = list(y.keys())
ordered.sort()
for item in ordered:
    print(y[item])