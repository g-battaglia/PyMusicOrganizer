from os import walk


def folder_count(path: str) -> int:
    count1 = 0
    for root, dirs, files in walk(path):
        count1 += len(dirs)

    return count1
