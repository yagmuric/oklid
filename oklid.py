import math
points = [(1, 2), (3, 4), (5, 6), (-1, -3), (0, 0)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))

min_distance = min(distances, key=lambda x: x[2])
print("Minimum mesafeye sahip nokta çifti ve mesafe:")
print(f"{min_distance[0]} ve {min_distance[1]} arasındaki mesafe: {min_distance[2]:.2f}")