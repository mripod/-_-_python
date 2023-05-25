import requests
with open (r"C:\Users\sales\Downloads\dataset_3378_3.txt") as file_in:
    text = file_in.read().strip()
    s = requests.get(text)
    while True:
        if not s.text.startswith('We'):
            s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s.text)
        else:
            print(s.text)
            break
