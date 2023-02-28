a = 1
b = 2
c = 1

import numpy as np

coeff = [a, b, c]
lower_x = (-b + (b **2 - 4 *a * c) ** 0.5) / (2 * a)
print(round(lower_x, 4))