with open (r'C:\Users\sales\Downloads\dataset_3363_2.txt') as file_in, open (r'C:\Users\sales\Downloads\file_out.txt', 'w') as file_out:
    text = file_in.read()
    k = 0
    while k < len(text):
        char = text[k]
        count = ''
        k += 1
        while k < len(text) and text[k].isdigit():
            count += text[k]
            k += 1
        if count:
            file_out.write(char * int(count))
