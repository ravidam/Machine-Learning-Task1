#Matala 1:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

file = pd.read_csv('C:/Users/RAVID/Desktop/Ariel/3rd year/semester 2/למידת מכונה/מטלה 1/sample.csv')

#plt.scatter(file['x'], file['y'])
#plt.show()
#print(file)

def GradientDescent (file, L, GD):
    m = c = 0
    M = []
    C = []
    E = []
    x_values = file['x'].values
    y_values = file['y'].values
    length = len(file['x'])

    for x in range(1000):
        suming1 = suming2 = suming3 = 0
        if GD == "B":
            for i in range(length):
                adding = y_values[i] - (m*x_values[i]) - c
                suming1 += (adding**2)
                suming2 += (adding*x_values[i])
                suming3 += adding
            Dm = suming2*(-2/length)
            Dc = suming3*(-2/length)
        
            E.append(suming1/length)
        elif GD == "S":
            i = random.randint(0,length-1)
            adding = y_values[i] - (m*x_values[i]) - c
            suming1 += (adding**2)
            suming2 += (adding*x_values[i])
            suming3 += adding
            Dm = suming2*(-2)
            Dc = suming3*(-2)
        
            E.append(suming1)
        elif GD == "M":
            n= []
            for r in range(10):
                n.append(random.randint(0,length-1))
            for i in n:
                adding = y_values[i] - (m*x_values[i]) - c
                suming1 += (adding**2)
                suming2 += (adding*x_values[i])
                suming3 += adding
            Dm = suming2*(-2/10)
            Dc = suming3*(-2/10)
        
            E.append(suming1/10)
        M.append(m)
        C.append(c)
        m -= (L*Dm)
        c -= (L*Dc)
    Epoches = [i for i in range(1000)]
    data = [Epoches, M, C, E]
    data = np.array(data).T
    return pd.DataFrame(data, columns= ['Epoch', 'A_values', 'B_values', 'E_values'])


gradient = GradientDescent (file, 0.1, "B")

print(gradient.tail())
print(gradient.iloc[999])

plt.plot(gradient['Epoch'],gradient['E_values'])
plt.title("E data")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

plt.plot(gradient['Epoch'],gradient['A_values'])
plt.title("a data")
plt.xlabel("Epoch")
plt.ylabel("a")
plt.show()

plt.plot(gradient['Epoch'],gradient['B_values'])
plt.title("b data")
plt.xlabel("Epoch")
plt.ylabel("b")
plt.show()