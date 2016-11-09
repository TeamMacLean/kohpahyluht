import time
import os
import config



def get_new_folder():
    current_date = time.strftime("%d_%m_%Y")
    root = config.get_config().get('Files', 'Root')

    folder_name = current_date
    i = 1

    while os.path.exists(folder_name):
        i += 1
        folder_name = str(current_date) + "__" + str(i)

    full_path = os.path.join(root, folder_name)

    os.makedirs(folder_name)

    return full_path
