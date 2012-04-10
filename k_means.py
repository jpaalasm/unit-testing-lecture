
import numpy as np


# -- Pre-defined functions --

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


def k_means(points, K):
    # Intialize group centroids to random points
    centroids = []
    for i in range(K):
        centroid = np.random.randn(2)
        centroids.append(centroid)
    
    max_steps = 10
    
    for step_index in range(max_steps):
        # Create an empty list of data points for each group
        group_point_lists = []
        for i in range(K):
            group_point_lists.append([])
        
        # Iterate over data points and add the point to the closest group
        for point in points:
            group_index = find_nearest_centroid_index(centroids, point)
            group_point_lists[group_index].append(point)
        
        # Calculate new centroids based on the close points
        centroids = calculate_centroids(group_point_lists)
    
    return group_point_lists


# -- Functions to be defined --


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


# -- Tests --

def test_calculate_distance():
    distance1 = calculate_distance(0, 1, 0, 1)
    distance2 = calculate_distance(0, 0, 1, 1)
    distance3 = calculate_distance(0, 0, 0, 1)
    
    assert distance1 == 0
    assert distance2 == 2**0.5
    assert distance3 == 1


def test_calculate_centroids():
    group_point_lists1 = [[[0, 0], [2, 2]], [[10, 5], [0, 5]]]
    centroids1 = calculate_centroids(group_point_lists1)
    
    assert centroids1 == [[1, 1], [5, 5]]


def test_find_nearest_centroid_index():
    centroids = [[0, 0], [10, 0], [10, 10]]
    
    index1 = find_nearest_centroid_index(centroids, [0, 0])
    index2 = find_nearest_centroid_index(centroids, [4.9, 0])
    index3 = find_nearest_centroid_index(centroids, [5.1, 0])
    index4 = find_nearest_centroid_index(centroids, [10, 5.1])
    
    assert index1 == 0
    assert index2 == 0
    assert index3 == 1
    assert index4 == 2


def run_tests():
    test_calculate_distance()
    test_calculate_centroids()
    test_find_nearest_centroid_index()
    print "All tests passed"


if __name__ == "__main__":
    run_tests()
