import random

from my import *

if __name__ == "__main__":
    for i in range(3, 11):
        a = [random.randint(-100, 100) for _ in range(random.randint(1, 100))]
        with open(f"test{i}.t",'w+') as file:
            file.write(" ".join(map(str, a)))

        with open(f"test{i}.a",'w+') as file:
            file.write("Yes" if checkAlmostSorted(a) else "No")
