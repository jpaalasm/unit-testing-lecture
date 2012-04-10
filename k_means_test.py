
import numpy as np
import matplotlib.pyplot as plt

import k_means


def main():
    N = 100
    
    group_means = [(0, 0), (4, 5), (5, 0)]
    
    all_points = []
    
    for group_x_coord, group_y_coord in group_means:
        group_point_x_coords = np.random.randn(N) + group_x_coord
        group_point_y_coords = np.random.randn(N) + group_y_coord
        
        group_points = zip(group_point_x_coords, group_point_y_coords)
        all_points.extend(group_points)
    
    group_point_lists = k_means.k_means(all_points, 3)
    
    axes = plt.subplots(2, 1, sharex=True, sharey=True)[1]
    
    x_coordinates, y_coordinates = zip(*all_points)
    axes[0].plot(x_coordinates, y_coordinates, ".")
    
    for group_points in group_point_lists:
        x_coordinates, y_coordinates = zip(*group_points)
        axes[1].plot(x_coordinates, y_coordinates, ".", mew=0)
    
    plt.show()


if __name__ == "__main__":
    main()
