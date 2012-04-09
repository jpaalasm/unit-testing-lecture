
import math


# -- Functions --

def distance(x1, y1, x2, y2):
    square_distance = (x1 - x2)**2 + (y1 - y2)**2
    distance = math.sqrt(square_distance)
    return distance


# -- Tests --

def test_distance_is_zero():
    x1, y1, x2, y2 = 1, 2, 1, 2
    calculated_distance = distance(x1, y1, x2, y2)
    assert calculated_distance == 0.0

def test_distance_is_one():
    x1, y1, x2, y2 = 0, 0, 0, 1
    calculated_distance = distance(x1, y1, x2, y2)
    assert calculated_distance == 1.0

def run_tests():
    print "Running tests..."
    test_distance_is_zero()
    test_distance_is_one()
    print "All tests passed"


if __name__ == "__main__":
    run_tests()
