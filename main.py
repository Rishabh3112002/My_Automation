import sys

first_arg = sys.argv[0]

def create(word1=first_arg):
    print("{}".format(word1))

if __name__ == "__main__":
    create()
