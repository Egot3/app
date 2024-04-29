from flask import Flask, render_template, redirect, url_for, request
from random import randint, choice
import requests

app = Flask(__name__)

answers=-1
colOfPrim = 6

# Главная страница с кнопкой
@app.route('/')
def index():
    return render_template('index.html')

"""# Обработчик для кнопки получения данных
@app.route('/get_data')
def get_data():
    # URL второго API, который мы будем вызывать
    api_url = 'http://127.0.0.1:5001/random_data'
    
    # Отправляем GET запрос к другому API
    response = requests.get(api_url)
    
    # Получаем JSON данные
    data = response.json()
    
    # Перенаправляем на другую страницу и передаем данные в URL
    return redirect(url_for('display_data', temperature=data['temperature'], date=data['date']))"""

# Страница для отображения данных
@app.route('/easyLevel/', methods=['get'])
def easyLevel():
    global answers, colOfPrim
    if colOfPrim==0:
        print(request.form.get("superAnswer"))
        return render_template('answer.html',answer=request.form.get("superAnswer"))
    answers+=1
    colOfPrim-=1
    numsInPrim = randint(3,5)
    prim=list()
    znak=['+','-']
    for i in range(1,numsInPrim+1,2):
        prim.append(str(randint(1,100)))
        prim.append(str(choice(znak)))
    prim.pop(-1)
    truePrim="".join(prim)
    answer=eval(truePrim)
    
    return render_template('display.html',Prim=truePrim,ans=answer,goodAnswer=answers,col=colOfPrim)

@app.route('/normalLevel')
def normalLevel():
    global answers, colOfPrim
    if colOfPrim==0:
        print(request.form.get("superAnswer"))
        return render_template('answer.html',answer=request.form.get("superAnswer"))
    answers+=1
    colOfPrim-=1
    numsInPrim = randint(3,11)
    prim=list()
    znak=['+','-','*','/']
    for i in range(1,numsInPrim+1,2):
        prim.append(str(randint(1,100)))
        prim.append(str(choice(znak)))
    prim.pop(-1)
    truePrim="".join(prim)
    answer=eval(truePrim)
    
    return render_template('display.html',Prim=truePrim,ans=answer,goodAnswer=answers,col=colOfPrim)

@app.route('/hardLevel')
def hardLevel():
    global answers, colOfPrim
    if colOfPrim==0:
        print(request.form.get("superAnswer"))
        return render_template('answer.html',answer=request.form.get("superAnswer"))
    answers+=1
    colOfPrim-=1
    numsInPrim = randint(3,16)
    prim=list()
    znak=['+','-','*','/','**']
    for i in range(1,numsInPrim+1,2):
        prim.append(str(randint(1,100)))
        prim.append(str(choice(znak)))
    prim.pop(-1)
    truePrim="".join(prim)
    answer=eval(truePrim)
    
    return render_template('display.html',Prim=truePrim,ans=answer,goodAnswer=answers,col=colOfPrim)


if __name__ == '__main__':
    app.run(debug=True)

