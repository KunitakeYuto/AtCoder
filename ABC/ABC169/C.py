from decimal import Decimal
import math
a, b = input().split()
print(math.floor(Decimal(a)*Decimal(b)))