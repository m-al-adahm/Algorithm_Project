# Project: Algorithms Implementation

## Part 1: Heap-Sort Algorithm

# Heapify function to maintain the heap property
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Main Heap-Sort function
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

# Example usage of Heap-Sort
if __name__ == "__main__":
    print("Heap-Sort Example:")
    data = [4, 10, 3, 5, 1]
    print("Unsorted array:", data)
    heap_sort(data)
    print("Sorted array:", data)


## Part 2: Kruskal's Algorithm for MST

# Disjoint Set (Union-Find) implementation
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal's algorithm implementation
def kruskal(vertices, edges):
    mst = []  # Minimum spanning tree
    ds = DisjointSet(vertices)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            mst.append(edge)
            ds.union(u, v)

    return mst

# Example usage of Kruskal's Algorithm
if __name__ == "__main__":
    print("\nKruskal's Algorithm Example:")
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('B', 'C', 4),
        ('A', 'C', 3),
        ('C', 'D', 2),
        ('D', 'E', 5),
        ('B', 'E', 6)
    ]

    mst = kruskal(vertices, edges)
    print("Edges in MST:", mst)