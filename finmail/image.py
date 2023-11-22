import matplotlib.pyplot as plt
from config import DARK_RED

class Plot:
    def __init__(self):
        pass
    
    def plot(self, x, y, title=None, xlabel=" ", ylabel="m", color1="tab:red", linewidth=3.0, label="None"):
        plt.plot(x, y, color=color1, linewidth=linewidth, label=label)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.gca().set_aspect(0.8)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.show()
        
        


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]

p = Plot()
p.plot(x,y, title="Test", xlabel="X", ylabel="Y", color1=DARK_RED)