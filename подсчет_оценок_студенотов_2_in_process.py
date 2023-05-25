with open (r"C:\Users\sales\Downloads\dataset_3363_4.txt") as file_in, open (r'C:\Users\sales\Downloads\file_out_2.txt', 'w') as file_out:
    avg1_values = []
    avg2_values = []
    avg3_values = []
    avg_students = []
    for line in lines:
        if len(sublist) >= 4:
            values = [int(item) for item in sublist[1:]]
            average = sum(values) / len(values) if len(values) > 0 else 0
            avg_students.append(average)
            avg1_values.append(int(sublist[1]))
            avg2_values.append(int(sublist[2]))
            avg3_values.append(int(sublist[3]))

        avg_all = sum(avg_students) / len(avg_students) if len(avg_students) > 0 else 0
        avg1 = sum(avg1_values)/len(avg1_values) if len(avg1_values) > 0 else 0
        avg2 = sum(avg2_values)/len(avg2_values) if len(avg2_values) > 0 else 0
        avg3 = sum(avg3_values)/len(avg3_values) if len(avg3_values) > 0 else 0
        
        file_out.write(f'{avg_all}\n')
        file_out.write('\n')
        for i, sublist in enumerate(data):
            if len(sublist) >= 4:
                file_out.write(f'{int(sublist[1])}, {int(sublist[2])}, {int(sublist[3])}')
    
            