from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def main():
    put_image(open('logoSC.png', 'rb').read());

    put_text('Precisando daquela sugestão do chefe? Encontre as melhores receitas aqui e aprovete!').style(
        'color: #025D00; font-size:25px; margin-top:25px; margin-bottom:30px');

    text = textarea('Pesquisar receita', rows=3, placeholder='Nome da Receita')


    put_row([
        put_column([
            put_row([
                put_table([['Nome receita', 'Ingredientes'], [put_text('%r' % text), 'D']]),
                put_image(open('chefLogo.png', 'rb').read())
,
            ]),
        ]),

    ])

<<<<<<< Updated upstream
text = textarea('Pesquisar receita', rows=3, placeholder='Nome da Receita')
put_text('text = %r' % text)
=======


start_server(main, port=8080, debug=True)
>>>>>>> Stashed changes
