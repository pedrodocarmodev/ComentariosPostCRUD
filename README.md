<img width="1280" height="720" alt="Imagem App 1" src="https://github.com/user-attachments/assets/6ae4d086-f86f-4738-b880-fc1549f67f00" />
<img width="1280" height="720" alt="Imagem App 2" src="https://github.com/user-attachments/assets/34347fab-b62a-48d4-9813-17e35f06a3fd" />


````md

## 🚀 Tecnologias

- Django
- Bootstrap
- Python
- Sqlite

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Python 3.10+ (recomendado)
- pip
- pipenv

Para instalar o pipenv:

pip install pipenv

````

---

## ⚙️ Instalação e execução

### 1. Clone o repositório

```bash
git clone https://github.com/piudi2121/ComentariosPostCRUD
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pipenv install
```

### 3. Ative o ambiente virtual

```bash
pipenv shell
```

---

## 🔐 Variáveis de ambiente

Este projeto utiliza variáveis de ambiente.
O arquivo `.env` **não é versionado** por questões de segurança.

### 1. Crie o arquivo `.env`

```bash
cp .env.example .env
```

### 2. Preencha as variáveis necessárias

Exemplo de `.env`:

```env
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
```

---

## 🗄️ Banco de dados

Aplique as migrações:

```bash
python manage.py migrate
```

---

## ▶️ Executando o projeto

```bash
python manage.py runserver
```

Acesse em:

```
http://127.0.0.1:8000/
```

---

## 🧪 Criar superusuário


```bash
python manage.py createsuperuser
```

---
