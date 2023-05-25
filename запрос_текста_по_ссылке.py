import requests
with open (r"C:\Users\sales\Downloads\dataset_3378_2.txt") as file_in:
    text = file_in.read().strip()
    response = requests.get(text)
    print(response.text.count('\n'))
    
