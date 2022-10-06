with open("name.txt", "w") as f:
    f.writelines(["Henry", "HEnry", "HENry"])


with open("name.txt", "r") as f:
    print(f.readlines())