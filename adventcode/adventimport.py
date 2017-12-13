import os

def read_file(file):
    with open(file, 'r') as f:
        return [line.replace('\t', ' ').replace('\n', '').split(" ") for line in f]


class ImportData:
    def text_import(self, fname):
        "import from a text file return a matrix"
        script_dir = os.path.dirname(__file__)
        abs_file = os.path.join(script_dir, fname)
        return read_file(abs_file)

if __name__ == "__main__":
    i = ImportData()
    print(i.text_import("data/daytwo.txt"))