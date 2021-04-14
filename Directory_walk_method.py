import os
def osp(ph):
    for r, d, f in os.walk(ph):
        print(r)
        for e in d:
            print(e)
        for s in f:
            print(s)
if __name__ == "__main__":
    p = r"C:\Users\\ruban.kumar\Downloads"
    osp(p)