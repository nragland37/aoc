def find_start_of_message_marker(datastream):
    for i in range(13, len(datastream)):
        if len(set(datastream[i - 13 : i + 1])) == 14:
            return i + 1
    return -1


# **************************************************************************************************


def main():
    datastream = open("input01.txt").read().strip()

    position = find_start_of_message_marker(datastream)

    if position == -1:
        print("not found")
    else:
        print(position)


# **************************************************************************************************

if __name__ == "__main__":
    main()
