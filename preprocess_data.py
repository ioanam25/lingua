import json
import os

task_folder = '/gpfs/data/oermannlab/users/im2178/lingua/re_arc/tasks'
out_folder = '/gpfs/data/oermannlab/users/im2178/lingua/sources'

for filename in os.listdir(task_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(task_folder, filename)
        # print(filename)
        output_filename = filename[:-5] + '/' + f"{os.path.splitext(filename)[0]}.chunk.00.jsonl"  # Use the filename without extension
        # print(output_filename)
        output_file_path = os.path.join(out_folder, output_filename)
        print(output_file_path)
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        with open(output_file_path, 'w') as f:
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for entry in data:
                        io_string = 'i['
                        # print(entry)
                        input = entry['input']
                        output = entry['output']
                        for row in input:
                            io_string += '[' + "".join(map(str, row)) + ']'
                        io_string += ']o['
                        for row in output:
                             io_string += '[' + "".join(map(str, row)) + ']'
                        io_string += ']'
                        # print(io_string)
                        # print({'text': io_string})
                        # break
                        f.write(json.dumps({'text': io_string}) + "\n")

                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in file {filename}. Skipping this file.")
    # break
