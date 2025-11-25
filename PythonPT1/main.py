import os

cwd = os.getcwd()
resource_folder = os.path.join(cwd, 'resource')
resource_files = os.listdir(resource_folder)

txt_file_path_and_sizes = {}

txt_file = ''
txt_file_path = ''
txt_file_size = 0
file_index = 0

print('List of text files:')
for files in range(len(resource_files)):
    if '.txt' in resource_files[files]:
        file_index += 1
        txt_file = resource_files[files]
        txt_file_path = os.path.join(resource_folder, resource_files[files])
        txt_file_size = os.path.getsize(txt_file_path)
        txt_file_path_and_sizes[txt_file_path] = txt_file_size
        print('{}: => {} bytes'.format(txt_file, txt_file_size))

txt_total_size = sum(txt_file_path_and_sizes.values()) /1024
txt_average_size = txt_total_size / file_index

note= '''
Total number of text files : {}
Total size of text file : {:0.2f} KB
Average size of text file : {:0.2f} KB

List of non-text files:
'''

print(note.format(file_index, txt_total_size, txt_average_size))

for files in range(len(resource_files)):
    if not 'txt' in resource_files[files]:
        print(resource_files[files])