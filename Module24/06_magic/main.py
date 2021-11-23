import random

import Material

material_list = [Material.Water(), Material.Wind(), Material.Fire(), Material.Earth(), Material.Human()]
count = 10
while count > 0:
    a = random.choice(material_list)
    b = random.choice(material_list)
    print("{} + {} = {}".format(a.name, b.name, a + b))
    count -= 1