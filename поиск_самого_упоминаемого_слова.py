with open (r'C:\Users\sales\Downloads\dataset_3363_2.txt') as file_in, open (r'C:\Users\sales\Downloads\file_out.txt', 'w') as file_out:
    text = file_in.read().replace('\n', '').lower().split()
    word_counts = {}
    for word in text:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    most_common_word = max(word_counts, key = word_counts.get)
    count = word_counts[most_common_word]
    
    file_out.write(f'{most_common_word} ')
    file_out.write(f'{count}')