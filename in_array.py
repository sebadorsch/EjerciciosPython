def in_array(a, b):
    r = []
    for i in set(a):
        for j in set(b):
            if j.find(i) != -1 and i not in r:
                r.append(i)
    return sorted(r)


if __name__ == '__main__':
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    print(in_array(a1, a2))

    a3 = ["arp", "mice", "bull"]
    a4 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp']
    print(in_array(a3, a4))