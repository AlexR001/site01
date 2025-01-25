from mbib.sistem_file import app
import mbib.rfact
import mbib.rname
import mbib.secret 


@app.route("/")
def main_hello():
    return f'''
    <h1>Привет, это интересный сайт!</h1> 
    <a href="/rfact"><h2>Посмотреть случайный факт про технлогические зависимости...</h2></a>
    <a href = '/rname'><h2>Хочешь увидеть случайное имя?! Нажимай!</h2></a>
    '''
@app.route("/rfact")
def rfact():
    return f'''
    <h2>{mbib.rfact.rfact()}</h2>
    '''
@app.route('/secret')
def secret():
    pas8 = mbib.secret.gen_pass8()
    pas16 = mbib.secret.gen_pass16()
    monetka = mbib.secret.monetka()
    color = mbib.secret.color()
    num = mbib.secret.rnum()

    return f'''
    <h1>Вот безопасный пароль:
    {pas8}.</h1>
    <h1>А вот ещё более безопасный пароль:
    {pas16}.</h1>
    <h1>И я подоросил монетку. Вот выпавшая сторона: {monetka}.</p>
    <h1>Мне нравится число {num}.</h1>
    <h1>Сейчас {color} момент!</h1>
    <a href = '/secret'><h2>Нажми чтобы перезагрузить страницу!</h2></a>
    '''
@app.route('/rname')
def rname():
    return f'''
    <h1>Меня зовут {mbib.rname.rname()}.</h1>
    <a href = '/rname'><h2>Нажми чтобы перезагрузить страницу!</h2></a>
    '''


app.run(debug=True)