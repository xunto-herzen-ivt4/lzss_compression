def find_in_dict(buffer, dictionary):
    shift = len(dictionary)
    substring = ""

    for character in buffer:
        substring_tmp = substring + character
        shift_tmp = dictionary.rfind(substring_tmp)

        if shift_tmp < 0:
            break

        substring = substring_tmp
        shift = shift_tmp

    return len(substring), len(dictionary) - shift


def compress(message, buffer_size=4, dictionary_size=12):
    dictionary = ""
    buffer = message[:buffer_size]

    output = []
    while len(buffer) != 0:
        size, shift = find_in_dict(buffer, dictionary)

        if size == 0:
            output.append((0, message[:1]))
            size = 1
        else:
            output.append((1, shift, size))

        dictionary += message[:size]
        dictionary = dictionary[-dictionary_size:]

        message = message[size:]
        buffer = message[:buffer_size]

    return output


def decompress(compressed_message):
    message = ""
    for part in compressed_message:
        if part[0] == 0:
            _, character = part
            message += character
        else:
            _, shift, size = part
            message += message[-shift:][:size]
    return message
