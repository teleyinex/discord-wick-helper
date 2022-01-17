with open("ids.txt", "r") as f:
    ids = f.read().splitlines()


def chunker_list(seq, size):
    return (seq[i::size] for i in range(size))


wick = list(chunker_list(ids, int(len(ids) / 4)))

for w in wick:
    print(f"w!b {' '.join(w)}")
