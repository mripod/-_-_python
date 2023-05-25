with open (r"C:\Users\sales\Downloads\dataset_3363_4.txt") as file_in:
    lines = file_in.read().split('\n')

avg1_values = 0
avg2_values = 0
avg3_values = 0

with open (r'C:\Users\sales\Downloads\file_out_2.txt', 'w') as file_out:
    for line in lines:
        data = line.strip().split(';')
        name = data[0]
        scores = list(map(int, data[1:]))

        if scores:
            avg_score = sum(scores) / len(scores)

            file_out.write(f'{avg_score}\n')

            file_out.write(f'{scores[0]}\n')
            file_out.write(f'{scores[1]}\n')
            file_out.write(f'{scores[2]}\n')
                       
            avg1_values += scores[0]
            avg2_values += scores[1]
            avg3_values += scores[2]

    num_students = len(lines)
    avg1_total = avg1_values / num_students
    avg2_total = avg2_values / num_students
    avg3_total = avg3_values / num_students

    file_out.write(f'{avg1_total} {avg2_total} {avg3_total}')

