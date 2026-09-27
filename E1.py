import  sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("python :",sys.version.split()[0])
print("numpy :",np.__version__)
print("pandas :",pd.__version__)
print("matplotlib :",matplotlib.__version__)
print("commit3")
print("25EC01013")
plt.plot([1,2,3,4],[1,4,9,16],marker='o')
plt.title("If you can see this, matplotlib is working")
plt.xlabel("x-axis")
plt.ylabel("y=x^2")
plt.grid(True)
plt.show()