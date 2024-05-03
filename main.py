from g4f.client import Client # gpt без огранечений
from cards import base # добавляем базу  вопросов с соседнего файла
from googletrans import Translator # библиотека для перевода от гугла

translator = Translator()#создаём объект

client = Client()#необхоимость как на 2 строчки выше

for i in base:
    print(i, end = ":\n") #выводит   card1: 
    for j in base[i]:
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "очень кратко в пару слов ответь на  вопрос: " + j},],
        ) #запрос 

        print("вопрос " + str(base[i].index(j) + 1) + ": " + j)# выводит вопрос

        # print("Ответ(рус):",translator.translate(response.choices[0].message.content, src='kk', dest='ru').text) тут часто гугл ломается
        print("ответ :",response.choices[0].message.content)#ответ

        print("")#декорация

input("нажмите enter для выхода")#что бы сразу не выходило из консоли