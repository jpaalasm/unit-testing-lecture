
import numpy as np

def find_smallest_value_index(values):
    return np.argmin(values)


def calculate_mean_point(points):
    mean_point = np.mean(points, 0).tolist()
    return mean_point


def calculate_distance_to_centroid(point, centroid):
    x1, y1 = point
    x2, y2 = centroid
    
    distance = calculate_distance(x1, y1, x2, y2)
    return distance

def calculate_distance(x1, y1, x2, y2):
    square_distance = (x1 - x2)**2 + (y1 - y2)**2
    distance = np.sqrt(square_distance)
    return distance


def calculate_centroids(group_point_lists):
    centroids = []
    
    for group_points in group_point_lists:
        centroid = calculate_mean_point(group_points)
        centroids.append(centroid)
    
    return centroids


def find_nearest_centroid_index(centroids, point):
    distances = []
    
    for centroid in centroids:
        distance = calculate_distance_to_centroid(point, centroid)
        distances.append(distance)
    
    nearest_centroid_index = find_smallest_value_index(distances)
    return nearest_centroid_index
