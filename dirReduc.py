def dirReduc(arr):
    a, b, i = 0, 0, 0
    while i < len(arr)-1:
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH" or arr[i] == "SOUTH" and arr[i+1] == "NORTH"\
                or arr[i] == "EAST" and arr[i+1] == "WEST" or arr[i] == "WEST" and arr[i+1] == "EAST":
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return arr


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(a), ['WEST'])
    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

    b = ["NORTH", "WEST", "SOUTH", "EAST", "WEST", "SOUTH", "EAST", "WEST", "SOUTH", "EAST", "EAST", "EAST", "WEST",
         "SOUTH", "EAST"]
    print(dirReduc(b), ["NORTH", "WEST", "SOUTH", "EAST"])