import os

class File:
    path = None
    filename = None
    

    def __init__(self, path = None, filename = None):
        self.path = path
        self.filename = filename

    def move_to_path(self, path) -> (str, str):
        complete_path = path + "/" + self.filename
        clean_path = complete_path[5:]
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        os.rename(self.path, complete_path)

        return complete_path, clean_path
    