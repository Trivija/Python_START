"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
"""
result = []
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            result.append(not (x or y or z) == (not x and not y and not z))
print(all(result))
"""

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            print(not(X or Y or Z) == (not X and not Y and not Z))

