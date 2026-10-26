data = [
    [85, 90],
    [80, 88],
    [82, 91],
    [35, 50],
    [40, 55],
    [38, 52]
]
students = ["S1", "S2", "S3", "S4", "S5", "S6"]

def distance(p, c):
    return ((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2) ** 0.5

centroids = [[85, 90], [35, 50]]

for iteration in range(100):
    clusters = [[], []]
    for point in data:
        d1 = distance(point, centroids[0])
        d2 = distance(point, centroids[1])
        clusters[0 if d1 <= d2 else 1].append(point)

    new_centroids = []
    for i, cluster in enumerate(clusters):
        if cluster:
            mean_x = sum(p[0] for p in cluster) / len(cluster)
            mean_y = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append([mean_x, mean_y])
        else:
            new_centroids.append(centroids[i])

    if new_centroids == centroids:
        break
    centroids = new_centroids

print("K-Means Clustering Results")
for i, cluster in enumerate(clusters):
    print("\nCluster", i + 1)
    for point in cluster:
        print(students[data.index(point)], "Marks:", point[0], "Attendance:", point[1])
    print("Centroid:", centroids[i])

# Input: No input required; student data is predefined.
# K = 2. Expected groups: S1-S3 and S4-S6.
# Run: python exp-exp8-k-means-clustering.py
