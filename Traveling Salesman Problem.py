from itertools import permutations

def tsp_brute_force(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    best_route = []

    for perm in permutations(cities):
        distance = 0
        for i in range(len(perm)):
            distance += distances[perm[i]][perm[(i + 1) % len(cities)]]
        if distance < min_distance:
            min_distance = distance
            best_route = perm
    return list(best_route), min_distance

# User Input
n = int(input("Enter number of cities: "))
distances = []
for i in range(n):
    row = list(map(int, input(f"Enter distances from city {i} (space separated): ").split()))
    distances.append(row)

route, dist = tsp_brute_force(distances)
print("Best Route:", route)
print("Minimum Distance:", dist)
