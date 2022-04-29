import os
import shutil



dir_d = os.path.dirname(os.path.abspath(__file__))

files = [os.path.relpath(os.path.join(root, file), dir_d) for root, _, files in os.walk(dir_d)
         for file in files if file.endswith(".html")]

for rel_path in files:
    path, file = os.path.split(rel_path)
    test_path = os.path.join(dir_d, "templates", path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    shutil.copyfile(os.path.join(dir_d, rel_path), os.path.join(test_path, file))


