
import os
folder_structure = {"my_project": [{'settings': []},
                                {'mainapp': [{'templates': [{'mainapp': []}]}]},
                                {'authapp': [{'templates': [{'authapp': []}]}]},
                                {'adminapp': []}]}
def create_dir(pth, struct):
    for fold_node, ch_node in struct.items():

        dir_path = os.path.join(pth, fold_node)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        if len(ch_node) > 0:
            for node in ch_node:
                create_dir(dir_path, node)




create_dir(os.getcwd(), struct=folder_structure)

