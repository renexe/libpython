from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.tests.test_spam.conftest import sessao


def test_envio_de_spam():
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'rene@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )