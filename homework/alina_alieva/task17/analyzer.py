import argparse
import os


def is_block_start(line):
    return (
            len(line) > 19 and
            line[0:4].isdigit() and
            line[4] == '-' and
            line[5:7].isdigit() and
            line[7] == '-' and
            line[8:10].isdigit()
    )


parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to file or folder")
parser.add_argument("--text", help="string for search")
args = parser.parse_args()

print("Path:", args.path)
print("Text:", args.text)

if args.text is None:
    print("Please add --text")
    exit()

search_text = args.text

if os.path.isfile(args.path):
    print("it's file")
    files = [args.path]
elif os.path.isdir(args.path):
    print("it's folder")
    files = []
    for name in os.listdir(args.path):
        full_path = os.path.join(args.path, name)
        if os.path.isfile(full_path):
            files.append(full_path)
else:
    print("The path is not exist")
    exit()

for file in files:
    filename = os.path.basename(file)
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        if search_text in line:
            words = line.split()
            clean_words = [w.strip() for w in words]
            for i, w in enumerate(clean_words):
                if search_text in w:
                    start = max(i - 5, 0)
                    end = min(i + 6, len(words))
                    snippet = " ".join(words[start:end])

                    print(f"{filename}, строка {line_number}: {snippet}")

for block in files:
    with open(block, encoding="utf-8") as f:
        lines = f.readlines()

    blocks = []
    current_block = []

    for line in lines:
        if is_block_start(line):
            if current_block:
                blocks.append(current_block)
            current_block = [line]
        else:
            current_block.append(line)

    if current_block:
        blocks.append(current_block)

    for block in blocks:
        block_text = "".join(block)
        if search_text in block_text:
            print("\n--- block of the text ---")
            print(block_text[:500], "...")
