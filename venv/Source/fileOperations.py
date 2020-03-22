import magic
import os


# this function finds txt files with vocabulary
def get_files(dir_path, file_names, txt_files):
    for i in file_names:
        file_path = os.path.join(dir_path, i)   # file_path of file which extension will be found
        if os.path.exists(file_path):   # to use magic we have to know if file exists
            file_type = magic.from_file(file_path)
            # these condition is met with different types of txt files, it can be also some scripts etc
            if file_type.find('text') != -1:
                txt_files.append(i)


def traverse_directory():
    """
        this function traverse directory called "vocabulary" to find all files and then find txt with get_files func
    """
    txt_files = []  # list of files with vocabulary
    # traversing through directory
    for dir_path, dir_names, file_names in os.walk('vocabulary'):
        get_files(dir_path, file_names, txt_files)
    return txt_files


def get_words(file_name):
    path = 'vocabulary/' + file_name
    with open(path, 'r'):
        words = [line.rstrip('\n') for line in open(path)]     # list of words
    return words
