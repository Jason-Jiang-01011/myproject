import os


def get_info(source):
    return "hello world from " + source


def set_info(target):
    print(target)


if __name__ == "__main__":
    print(get_info("Jason"))
    os.system("pause")