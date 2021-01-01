from state import *

from test_shop import *


x=item()
x.buy()
print(x.getstate())

while x.available():
  x.buy()
  print("")
  print("")

x.restock()

x.buy()

print("")
print("")
print("")
print("new one")
print("")
print("")
print("")

x=item()

x.buy()
print("")

x.restock()
print("")

x.restock()
print("")

