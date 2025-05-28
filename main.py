import csv
import networkx as nx

def read_input_file(file_path):
    input_data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        i = 1
        for row in reader:
            coords = (float(coord) for coord in row)
            input_data.append((tuple(coords), i))
            i += 1

    return input_data

def write_output_file(file_path, output_data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in output_data:
            writer.writerow(row)

def calculate_distance(point1, point2, dimensions):
    sum = 0
    for i in range(dimensions):
        sum += (point1[i] - point2[i]) ** 2
    
    return sum ** 0.5

def build_distances_list(input_data):
    dimensions = len(input_data[0][0])
    distances = []

    current_point = input_data[0]
    visited_points = [current_point[1]]

    while len(visited_points) < len(input_data):
        min_distance = float('inf')
        next_point = None
        
        for point, index in input_data:
            if index not in visited_points:
                distance = calculate_distance(current_point[0], point, dimensions)
                if distance < min_distance:
                    min_distance = distance
                    next_point = (point, index)
                elif distance == min_distance:
                    if index < next_point[1]:
                        next_point = (point, index)

        if next_point is not None:
            visited_points.append(next_point[1])
            distances.append((current_point[1], next_point[1], min_distance))
            current_point = next_point    

    return distances

def find_groups(distances, k):
    distances = sorted(distances, key=lambda x: (x[2], x[0]), reverse=True)
    distances = distances[k-1:]

    graph = nx.Graph()
    for point1, point2, distance in distances:
        graph.add_edge(point1, point2, weight=distance)
    
    components = list(nx.connected_components(graph))
    return components

def main():
    input_file = input("Forneca o nome do arquivo de entrada: ")
    output_file = input("Forneca o nome do arquivo de saida: ")
    k = int(input("Forneca o numero de grupos (K): "))

    input_data = read_input_file(input_file)
    distances = build_distances_list(input_data)
    groups = find_groups(distances, k)
    
    write_output_file(output_file, groups)

    print("Agrupamentos:")
    for group in groups:
        print(", ".join(str(x) for x in group))
            

main()
