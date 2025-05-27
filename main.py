import csv

def read_input_file(file_path):
    input_data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    return input_data

def write_output_file(file_path, output_data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in output_data:
            #writer.writerow(row)
            print(row)


def main():
    input_file = input("Forneca o nome do arquivo de entrada: ")
    output_file = input("Forneca o nome do arquivo de saida: ")
    k = int(input("Forneca o numero de grupos (K): "))

    input_data = read_input_file(input_file)

main()
