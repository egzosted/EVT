import importlib
import magic
import os


# this function finds txt files with vocabulary
def get_files(dir_path, file_names, txt_files):
    for i in file_names:
        file_path = os.path.join(dir_path, i)   # file_path of file which extension will be found
        if os.path.exists(file_path):   # to use magic we have to know if file exists
            # print(magic.from_file(file_path))
            file_type = magic.from_file(file_path)
            find_py = i.find('.py')
            # we want only ASCII text files and also we have to exclude python scripts
            if file_type == 'ASCII text' and find_py < 0:
                txt_files.append(i)
    return txt_files

