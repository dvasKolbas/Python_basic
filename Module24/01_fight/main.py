from Units import Units

import random

new_Units = Units(2)
cont = True
while cont:
    new_Units.fight()
    cont = new_Units.check_health()
