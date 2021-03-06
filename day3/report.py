import sys, csv

def generate_report(input_file: str, output_file: str):
    my_columns = [0, 4, 5] # USER1,100,90,80,270,90.00,
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'w', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file) 
            filewriter = csv.writer(csv_out_file)
            for row in filereader: 
                row_list_output = []
                for index_value in my_columns:
                    row_list_output.append(row[index_value])
                filewriter.writerow(row_list_output)
