from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Rene', email='rene@email.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Rene', email='rene@email.com'),
        Usuario(nome='Pedro', email='rene@email.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
