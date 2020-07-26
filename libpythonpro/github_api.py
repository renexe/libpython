import requests


def buscar_avatar(usuario):
    '''
    Busca o avatar de um usuário no Github
    :param usuario: str com o usuário no github
    :return: str com o link do avatar
    '''
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    usuario = 'renexe'
    print(f'{buscar_avatar(usuario)}')
