import sys
import pathlib


def recursive_print(path, depth=0, margin_symbol=" "):
    margin = margin_symbol * depth
    if path.is_dir():
        print(margin + path.name + "/")
        for element in path.interdir():
            recursive_print(element, depth=depth+1, margin_symbol=margin_symbol)
    else:
        print(margin + path.name)


def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    recursive_print(path)


if __name__ == '__main__':
    main()
