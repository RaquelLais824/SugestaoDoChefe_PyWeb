from pywebio.output import *

put_image(open('logoSC.png','rb').read());

put_text('Precisando daquela sugestão do chefe? Encontre as melhores receitas aqui e aprovete!').style('color: black; font-size:25px; margin-top:30px; margin-bottom:30px');

put_table([
    ['TypeTypeTypeTypeTypeTypeTypeTypeTypeTypeTypeTypeTypeType', 'Content'],
    ['html', put_html('X<sup>2</sup>')],
    ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    ['buttons', put_buttons(['A', 'B'], onclick=...)],
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
])


