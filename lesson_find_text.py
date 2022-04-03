"""
Find texts
"""
import sys
import os


def test_words(files, base_word):
    return [x for x in files if set(x).issubset(set(base_word))]


def main():
    print(sys.argv)
    path = os.path.dirname(sys.argv[1])
    extension = sys.argv[2]

    fname = []
    fname_not = []
    for root, d_names, f_names in os.walk(path):
        for f in f_names:
            if f.find(extension) != -1:
                fname.append(os.path.join(root, f))
            else:
                fname_not.append(os.path.join(root, f))

    print(fname)

    for f in fname:
        fin = open(f, 'r', encoding='utf-8')
        for line in fin:
            print(line)
        fin.close()


if __name__ == "__main__":
    main()
