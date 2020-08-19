from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rene@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rene', email='rene@email.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )
    enviador.enviar.assert_called_once_with == (
        'pedro@email.com',
        'rene@email.com',
        'Educação EAD',
        'Aprendendo ACAD em dois meses'
    )
