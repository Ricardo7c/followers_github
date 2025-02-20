# followers_github

![GitHub](https://img.shields.io/badge/GitHub-API-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Uma biblioteca Python para listar seguidores e perfis seguidos no GitHub.

## 🚀 Instalação

```bash
pip install followers_github
```

## 🛠 Uso

### Importação

```python
from followers_github import followers, following
```

### Obtendo seguidores de um usuário

```python
print(followers("torvalds"))
```

### Obtendo perfis seguidos por um usuário

```python
print(following("torvalds"))
```

### Uso com Token de Autenticação
Para evitar limites de requisição na API do GitHub, você pode fornecer um **token de acesso pessoal**:

```python
MEU_TOKEN = "seu_token_aqui"
print(followers("torvalds", MEU_TOKEN))
```

## 📜 Estrutura do Projeto

```
followers_github/
│── followers_github/      # Pacote principal
│   ├── __init__.py        # Exposição das funções principais
│   ├── api.py             # Implementação das funções
│── pyproject.toml         # Configuração do pacote
│── README.md              # Documentação do projeto
│── LICENSE                # Licença
│── .gitignore             # Arquivos a serem ignorados
```

## 📄 Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para contribuir! 🚀

