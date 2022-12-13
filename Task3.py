def start_rle_compression(file_in, file_out, sort_elem):
    list_line = []
    with open(file_in, 'r') as file:
        for line in file:
            list_line.append(line)
    with open(file_out, 'w') as file:
        chet = 1
        for i in range(len(list_line)):
            for j in range(1, len(list_line[i])):
                str_line = list_line[i]
                if str_line[j - 1] == str_line[j]:
                    chet += 1
                else:
                    print(str(chet) + sort_elem + str_line[j - 1], file=file)
                    chet = 1
            print("", file=file)
    print("Сжатие прошло успешно")


def start_rle_recovery(file_in, file_out, sort_elem):
    list_line = []
    with open(file_in, 'r') as file:
        for line in file:
            list_line.append(line)
    with open(file_out, 'w') as file:
        for i in range(len(list_line) - 1):
            if list_line[i] == "\n":
                print("", file=file)
            else:
                str_line = (list_line[i].split(sort_elem)[1])[0] * int(list_line[i].split(sort_elem)[0])
                print(str_line, file=file, sep="", end="")
    print("Восстановление прошло успешно")


# sort_element = " "
# sort_element = "$"
sort_element = "_"  # его не должно быть в тексте
start_rle_compression('file_in.txt', 'file_out.txt', sort_element)
start_rle_recovery('file_out.txt', 'file_out_2.txt', sort_element)