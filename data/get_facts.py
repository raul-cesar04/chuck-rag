### Retrive Chuck Facts from https://api.chucknorris.io/jokes/random
import requests

NUMBER_OF_FACTS = 1500
FACTS = []

if __name__ == "__main__":
    for i in range(NUMBER_OF_FACTS):
        res = requests.get('https://api.chucknorris.io/jokes/random')
        res_json = res.json()
        FACTS.append(f'{res_json['value']}\n')

    try:
        with open('data/chuck_facts.txt', 'x') as file:
            file.writelines("".join(FACTS))
    except FileExistsError:
        with open('data/chuck_facts.txt', 'a') as file:
            file.write("".join(FACTS))
        print("No need to create file.")