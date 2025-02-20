import requests
from typing import List, Optional

def followers(username: str, token: Optional[str]=None) -> List[str]:
    """
    Obtém dados da API do GitHub (seguidores ou seguindo).
    
    :param username: Nome de usuário do GitHub.
    :param token: Token de acesso pessoal (opcional).
    :param tipo: Tipo de dados ('followers' ou 'following').
    :return: Lista de nomes de usuários.
    """
    
    url = f"https://api.github.com/users/{username}/followers"
    headers = {"Authorization": f"token {token}"} if token else {}
    lista = []
    
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro: {response.status_code}, {response.json().get('message')}")
            return []
        
        data = response.json()
        lista.extend([item['login'] for item in data])
        
        # Verificar se há uma próxima página
        url = response.links.get('next', {}).get('url')
    
    return lista


def following(username: str, token: Optional[str]=None) -> List[str]:
    """
    Obtém dados da API do GitHub (seguidores ou seguindo).
    
    :param username: Nome de usuário do GitHub.
    :param token: Token de acesso pessoal (opcional).
    :return: Lista de nomes de usuários.
    """
    
    url = f"https://api.github.com/users/{username}/following"
    headers = {"Authorization": f"token {token}"} if token else {}
    lista = []
    
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro: {response.status_code}, {response.json().get('message')}")
            return []
        
        data = response.json()
        lista.extend([item['login'] for item in data])
        
        # Verificar se há uma próxima página
        url = response.links.get('next', {}).get('url')
    
    return lista

