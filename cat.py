import sys
import os
def main():
    path = sys.argv[1]
    if path == "-help":
        print("Params help\ncat \"file path\" -- Show file.\ncat \"file path\" \"utf-8\" -- input code")
    else:
        if os.path.isfile(path):
            text = ""
            if len(sys.argv) == 2:
                with open(file=path, mode="r", encoding="utf-8") as file:
                    text = file.read()
            elif len(sys.argv) == 3:
                with open(file=path, mode="r", encoding=sys.argv[2]) as file:
                    text = file.read()
            else:
                print("Only up to 2 arguments can be specified")
                return False
            print(text)
            return True
        else:
            print("This directory is not a file")
            return False

if __name__ == "__main__":
    main()