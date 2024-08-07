import torch
import matplotlib.pyplot as plt
import numpy as np

#Start point for the first square
start_points = torch.tensor([[-1, -1],
                       [-1, 1],
                       [1, 1],
                       [1, -1],
                       [-1, -1]], dtype=torch.float32)  

x = start_points[:, 0]
y = start_points[:, 1]
plt.plot(x, y, 'b-')  # Blue line to draw the square

angle = np.pi/4
clk_rotation_matrix = torch.tensor([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]], dtype=torch.float32)

rotated_points = torch.matmul(start_points, clk_rotation_matrix)

rotated_points_np = rotated_points.numpy()
print(rotated_points_np)

x = rotated_points_np[:, 0]
y = rotated_points_np[:, 1]

plt.plot(x, y, 'b-')  # Blue line to draw the square
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
print("End")