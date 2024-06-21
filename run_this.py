from g4f.client import Client # gpt без огранечений
import json
from googletrans import Translator # библиотека для перевода от гугла
from multiprocessing import Pool

translator = Translator()#создаём объект

client = Client()#необхоимость как на 2 строчки выше

with open("cards.json","r", encoding="utf-8") as file:
    base = json.load(file)


def func(card_id):
    result = []
    for j in base["card"+str(card_id+1)]:
        
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": "Beantworten Sie die Frage ganz kurz in wenigen Worten:" + translator.translate(j, src='kk', dest='de').text},],
        ) #запрос 

        result.append(["вопрос " + str(base["card"+str(card_id+1)].index(j) + 1) + ": " + j, translator.translate( response.choices[0].message.content, src='de', dest='kk').text])

    return result

if __name__ == '__main__':

    with Pool(5) as p:
        list_of_out = p.map(func, range(13))
    with open("result.txt", "w", encoding="utf-8") as out_file:
        for i in list_of_out:
            print("card" + str(list_of_out.index(i) + 1) + ":")
            out_file.write("card" + str(list_of_out.index(i) + 1) + ":" + "\n")
            for j in i:
                print(j[0])
                print("ответ:",j[1])
                print()
                out_file.write(j[0]+"\n")
                out_file.write("ответ:" + j[1] + "\n")
                out_file.write(" ")
