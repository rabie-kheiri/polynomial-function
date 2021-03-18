
# importing the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# importing points values
df = pd.read_csv('index.CSV')

# axis values 
inp = np.array([])
out = np.array([])

for index, row in df.iterrows():
    inp = np.append (inp, row['x'])
    out = np.append (out, row['y'])

# polynomial matrix
PM = np.array([])
for C in range(len(inp)):
    MaListe = np.array([])
    for i in range(len(inp)):
        MaListe = np.append (MaListe, inp[C]**i)
    PM = np.append (PM, MaListe)
PM = PM.reshape(len(inp),len(inp))

IPM = np.linalg.inv(PM)
# PM*co=out ==> co=(PM)^-1*out

Co =np.matmul(IPM, out)
# make the funtion

x = np.linspace(inp[0],inp[len(inp)-1], num=100)
fx = []

for i in range(len(x)):
    f=0
    for I in range(len(Co)):
        f += Co[I]*(x[i]**I)
    fx = np.append (fx, f)

# plotting the points  
plt.plot(inp, out) 
plt.plot(x, fx) 

# naming the axis 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('polynomial funtion') 
  
# function to show the plot
plt.show() 
