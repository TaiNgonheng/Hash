import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = {}

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = distance
        self.vertices[to_vertex][from_vertex] = distance

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    def display_graph(self):
        for vertex in self.vertices:
            print(f"{vertex}: {self.vertices[vertex]}")

# Initialize the graph
Heng = Graph()
provinces = [
    "Phnom Penh", "Kandal", "Takeo", "Kampong Speu", "Kampong Chhnang",
    "Battambang", "Siem Reap", "Preah Sihanouk", "Kampot", "Koh Kong",
    "Banteay Meanchey", "Kampong Thom", "Kampong Cham", "Prey Veng", 
    "Svay Rieng", "Pursat", "Preah Vihear", "Stung Treng", 
    "Ratanakiri", "Mondulkiri", "Kratie", "My Home"
]
for province in provinces:
    Heng.add_vertex(province)

# Add edges with distances
edges = [
    ("Phnom Penh", "Kandal", 30),
    ("Phnom Penh", "Takeo", 75),
    ("Phnom Penh", "Kampong Speu", 48),
    ("Phnom Penh", "Kampong Chhnang", 91),
    ("Phnom Penh", "Battambang", 291),
    ("Phnom Penh", "Siem Reap", 314),
    ("Phnom Penh", "Preah Sihanouk", 230),
    ("Phnom Penh", "Kampot", 148),
    ("Phnom Penh", "Koh Kong", 278),
    ("Phnom Penh", "My Home", 146),
    ("Kandal", "Takeo", 55),
    ("Kandal", "Kampong Speu", 78),
    ("Takeo", "Kampong Speu", 93),
    ("Kampong Speu", "Kampong Chhnang", 63),
    ("Kampong Speu", "Kampot", 90),
    ("Preah Sihanouk", "Kampot", 105),
    ("Battambang", "Siem Reap", 170),
    ("Siem Reap", "Banteay Meanchey", 104),
    ("Siem Reap", "Kampong Thom", 147),
    ("Kampong Thom", "Kampong Cham", 138),
    ("Kampong Cham", "Phnom Penh", 124),
    ("Prey Veng", "Phnom Penh", 90),
    ("Prey Veng", "Svay Rieng", 45),
    ("Pursat", "Battambang", 106),
    ("Pursat", "Kampong Chhnang", 95),
    ("Preah Vihear", "Kampong Thom", 212),
    ("Stung Treng", "Preah Vihear", 143),
    ("Stung Treng", "Ratanakiri", 142),
    ("Ratanakiri", "Mondulkiri", 219),
    ("Kratie", "Kampong Cham", 136),
    ("Kratie", "Mondulkiri", 180),
    ("Banteay Meanchey", "Battambang", 65),
    ("Battambang", "Kampong Chhnang", 193),
    ("Preah Vihear", "Siem Reap", 170),
    ("Preah Vihear", "Stung Treng", 143),
    ("Stung Treng", "Kratie", 152),
    ("Ratanakiri", "Kratie", 210),
    ("Mondulkiri", "Kampong Cham", 236),
    ("Svay Rieng", "Kampong Cham", 107),
    ("Koh Kong", "Kampot", 237),
    ("Battambang", "Pursat", 106),
    ("Pursat", "Kampong Thom", 160),
    ("Kampong Thom", "Preah Vihear", 210),
    ("Kampong Cham", "Kratie", 136),
    ("Mondulkiri", "Kratie", 180),
    ("Ratanakiri", "Stung Treng", 142),
    ("Preah Vihear", "Siem Reap", 170)
]
for from_vertex, to_vertex, distance in edges:
    Heng.add_edge(from_vertex, to_vertex, distance)

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Display the graph's adjacency list")
        print("2. Find shortest paths from a specific province")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            Heng.display_graph()
        elif choice == '2':
            get_shortest_paths()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def get_shortest_paths():
    print("Available provinces:")
    print(", ".join(provinces))
    start_province = input("Enter the starting province: ").title()
    if start_province not in Heng.vertices:
        print("Invalid province name.")
        return
    shortest_paths = Heng.dijkstra(start_province)
    print(f"Shortest distances from {start_province}:")
    for province, distance in shortest_paths.items():
        print(f"  to {province}: {distance} km")

main_menu()
