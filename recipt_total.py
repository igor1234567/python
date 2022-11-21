import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' already exist")

# Get a list of all receipts
receipts = glob.glob("C:\\Users\\igorr\\git\\py_project\\python\\new\\recipt-*.json")
print(receipts)
print(receipts)
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        path = path.replace("\\", '/')
        content = json.load(f)
        print(path)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = f"processed\{name}"
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}")

print("receipt Subtotal : $%.2f" % subtotal)