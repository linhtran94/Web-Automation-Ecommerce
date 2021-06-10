import os

location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_root_folder_path():
    """
    Get root folder path of the project
    :return: Root folder path as String
    """
    return location


def get_files_path(file_name):
    """
    Get list of files in the project
    :param file_name: file name or extension of the filename
    :return: list of files as List
    """

    files_in_dir = []

    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            if file_name in item:
                files_in_dir.append(os.path.join(r, item))

    return files_in_dir


def get_folders_path(folder_name):
    """
    Get list of folders in the project
    :param folder_name: folder name
    :return: list of folders as List
    """
    dirs_in_dir = []

    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in d:
            if folder_name in item:
                dirs_in_dir.append(os.path.join(r, item))

    return dirs_in_dir
