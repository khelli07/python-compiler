log = [
    ['B', 'C', 'D'],
    ['A', 'B'],
    ['B', 'F', 'E']
]

rule = ['A', 'B']

nrlist = []
for grammar in log:
    new_rule = [rule[0]]
    if grammar[0] == rule[1] and grammar != rule:
        new_rule[1:] = grammar[1:]
        nrlist.append(new_rule)


print(nrlist)

lst = [[3, 1], [5, 2], [1, 4]]
lst = set(tuple(li) for li in lst)
print(sorted(lst, key=lambda x: x[0]))

print(str(0))

newrl = ['C', 'B', 'D']
inilist = ['hehe']
name = newrl[0] + "NAME" + str(1)
newrl.insert(0, name)
print(newrl)