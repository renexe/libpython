import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import sessao

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rene', email='rene@email.com'),
            Usuario(nome='Pedro', email='rene@email.com')
        ],
        [
            Usuario(nome='Rene', email='rene@email.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rene@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rene', email='rene@email.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )
    assert enviador.parametros_de_envio == (
        'pedro@email.com',
        'rene@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )