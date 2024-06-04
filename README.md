# Projeto Laboratório de Software

Aqui estão os passos necessários para configurar o ambiente de desenvolvimento e começar a trabalhar no projeto.

## Pré-Requisitos

Certifique-se de ter o Python 3.9 ou superior instalado no seu sistema.

## Configuração do Ambiente Virtual

1. Instale a dependência `virtualenv`:
    ```bash
    pip install virtualenv
    ```

2. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate.bat
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```

## Instalação das Dependências

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Migre o banco de dados:
```bash
cd projeto
python manage.py migrate
```

## Executando o Projeto

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

Isso iniciará o servidor local em http://127.0.0.1:8000/. Você pode acessar esta URL no seu navegador para visualizar o projeto em execução.

## Iniciando o Cadastro de Usuários

Para iniciar o cadastro de usuários, utilize as credenciais do usuário administrador pré-cadastrado:
- **Usuário:** admin
- **Senha:** admin