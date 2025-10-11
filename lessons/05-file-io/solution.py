# Solution: File I/O

def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def append_to_file(filename, content):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)

def count_lines_in_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)