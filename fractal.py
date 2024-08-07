import torch
import matplotlib.pyplot as plt
import numpy as np

def calc_diff(start, finish):
    return (finish[0]- start[0],finish[1]-start[1])

start_points = torch.tensor([[1, -1],
                       [-1, -1],
                       [-1, 1],
                       [1, 1],
                       [1,-1]], dtype=torch.float32)  

x = start_points[:, 0]
y = start_points[:, 1]
print(start_points[0])
plt.plot(x, y, 'b-')  

angle = np.pi/4
clk_rotation_matrix = torch.tensor([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]], dtype=torch.float32)

current_points = start_points

for _ in range(5):
    rotated_points = torch.matmul(current_points, clk_rotation_matrix)
    rotated_points= rotated_points/np.sqrt(2)
    x_delta, y_delta = calc_diff(current_points[2],rotated_points[3])
    x = (rotated_points[:, 0] + x_delta)
    y = (rotated_points[:, 1] + y_delta)
    current_points = rotated_points
    plt.plot(x, y, 'b-') 

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
print("End")