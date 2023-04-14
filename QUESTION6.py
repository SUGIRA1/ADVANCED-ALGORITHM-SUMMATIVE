# Read input values
nodes, edges, source = map(int, input().split())


# Calculate extra edges and minimum number of cycle edges
extraEdges = edges - (nodes - 1)
minNumCycleEdges = (source + nodes - 2) // (nodes - 1)


# Update source by subtracting minimum number of cycle edges
source -= minNumCycleEdges


# Initialize answer to a very large value
answer = float('inf')


# Loop through possible values of A and B
for A in [0, source // (nodes - 2), source // (nodes - 2) - 1]:
    for B in [0, nodes - 3, (source - A * (nodes - 2)) % (nodes - 2)]:
        x = A * (nodes - 2) + B
        if 0 <= x <= source:
            tempAnswer = (source - x + minNumCycleEdges) * extraEdges \
                + (nodes - 1) * (nodes - 2) // 2 * A \
                + B * (B - 1) // 2 \
                + B * (nodes - B - 1)
            answer = min(answer, tempAnswer)


# Print the final answer
print(answer + edges)


