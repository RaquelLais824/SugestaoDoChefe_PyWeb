from pywebio.output import *
from pywebio import start_server
from pywebio.input import *

put_image(open('logoSC.png', 'rb').read());

put_text('Precisando daquela sugestão do chefe? Encontre as melhores receitas aqui e aprovete!').style(
    'color: black; font-size:25px; margin-top:30px; margin-bottom:30px');


text = textarea('Pesquisar receita', rows=3, placeholder='Some text')
put_text('text = %r' % text)


