# Projeto REST API com Flask

Este projeto é uma API REST desenvolvida com o framework Flask, projetada para autenticação de usuários e criação de tokens JWT (JSON Web Tokens). A API permite o registro de novos usuários, login e acesso a uma rota protegida que requer autenticação.

## Funcionalidades

- **Registro de Usuários**: Permite criar novos usuários com nome e senha.
- **Autenticação via JWT**: Login dos usuários autenticados e geração de tokens JWT.
- **Acesso a Rota Protegida**: Apenas usuários autenticados podem acessar a rota `/dashboard`, onde podem ver o nome do usuário logado.

## Endpoints

### Registro de Usuários
- **Rota**: `/register`
- **Método**: `POST`
- **Requisição**: JSON contendo `username` e `password`.
- **Resposta**: Mensagem de sucesso ou erro.

### Login de Usuários
- **Rota**: `/login`
- **Método**: `POST`
- **Requisição**: JSON contendo `username` e `password`.
- **Resposta**: Token de acesso JWT.

### Dashboard (Rota Protegida)
- **Rota**: `/dashboard`
- **Método**: `GET`
- **Requisição**: Header com o token JWT.
- **Resposta**: Nome do usuário autenticado.

## Como Rodar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/projeto-rest-api.git
   cd projeto-rest-api
