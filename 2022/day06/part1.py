def find_start_of_packet_marker(datastream):
    for i in range(3, len(datastream)):
        if len(set(datastream[i - 3 : i + 1])) == 4:
            return i + 1
    return -1


# **************************************************************************************************


def main():
    datastream = open("input01.txt").read().strip()

    position = find_start_of_packet_marker(datastream)

    if position == -1:
        print("not found")
    else:
        print(position)


# **************************************************************************************************

if __name__ == "__main__":
    main()
