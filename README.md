# Backend Frameworks e Projeto de Banco de Dados 2024.1

Projeto final das disciplinas Backend Frameworks e Projeto de Banco de Dados 2024.1

### Equipe

- Fillipe Miranda - 03341457
- Breno Ferraz - 03338074
- Gabriel Padilha - 03338824

### Enunciado

> TEMA LIVRE
>
> Construa uma API com, no mínimo, 5 tabelas.
>
> Construa CRUD total para as 5 tabelas.
>
> O seu projeto deve ter pelo menos 5 consultas extras (Além do CRUD)
>
> Front no Postman

---

# Films Log

Esta é uma API construída com Flask que permite gerenciar usuários, filmes, resenhas, avaliações e favoritos.

Esta documentação fornece uma visão geral dos endpoints disponíveis e como utilizá-los.

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/famgz/films-log-api.git
   cd films-log-api
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Execute a aplicação:

   ```sh
   cd src
   flask run
   ```

### Acesse a documentação:

- Em inglês: `/docs/en`

- Em português: `/docs/pt`

## Endpoints

### Usuários

- **POST /user**

  Cria um novo usuário.

  **Parâmetros da Requisição (form-data):**

  - `username`: string
  - `email`: string
  - `password`: string

  **Resposta:**

  ```json
  { "message": "User criado com sucesso" }
  ```

- **GET /user/<int:id>**

  Obter um usuário pelo ID.

  **Resposta:**

  ```json
  {
      "id": int,
      "username": string,
      "email": string,
      "password": string
  }
  ```

- **PUT /user/<int:id>**

  Atualizar um usuário pelo ID.

  **Parâmetros da Requisição (form-data):**

  - `username`: string
  - `email`: string
  - `password`: string

  **Resposta:**

  ```json
  { "message": "User atualizado com sucesso" }
  ```

- **DELETE /user/<int:id>**

  Excluir um usuário pelo ID.

  **Resposta:**

  ```json
  { "message": "User excluído com sucesso" }
  ```

### Filmes

- **POST /film**

  Cria um novo filme.

  **Parâmetros da Requisição (form-data):**

  - `title`: string
  - `year`: int
  - `director`: string
  - `duration`: int

  **Resposta:**

  ```json
  { "message": "Filme adicionado com sucesso" }
  ```

- **GET /film/all**

  Obter todos os filmes.

  **Resposta:**

  ```json
  [
      {
          "id": int,
          "title": string,
          "year": int,
          "director": string,
          "duration": int
      },
      ...
  ]
  ```

- **GET /film/<int:id>**

  Obter um filme pelo ID.

  **Resposta:**

  ```json
  {
      "id": int,
      "title": string,
      "year": int,
      "director": string,
      "duration": int
  }
  ```

- **PUT /film/<int:id>**

  Atualizar um filme pelo ID.

  **Parâmetros da Requisição (form-data):**

  - `title`: string
  - `year`: int
  - `director`: string
  - `duration`: int

  **Resposta:**

  ```json
  { "message": "Filme atualizado com sucesso" }
  ```

- **DELETE /film/<int:id>**

  Excluir um filme pelo ID.

  **Resposta:**

  ```json
  { "message": "Filme excluído com sucesso" }
  ```

### Resenhas

- **POST /user/{username}/film/{film_id}/review**

  Cria uma nova resenha para um filme por um usuário.

  **Parâmetros da Requisição (form-data):**

  - `review`: string

  **Resposta:**

  ```json
  { "message": "Review adicionado com sucesso" }
  ```

- **GET /user/{username}/film/{film_id}/review**

  Obter uma resenha para um filme por um usuário.

  **Resposta:**

  ```json
  {
      "user_id": int,
      "film_id": int,
      "review": string
  }
  ```

- **PUT /user/{username}/film/{film_id}/review**

  Atualizar uma resenha para um filme por um usuário.

  **Parâmetros da Requisição (form-data):**

  - `review`: string

  **Resposta:**

  ```json
  { "message": "Review atualizado com sucesso" }
  ```

- **DELETE /user/{username}/film/{film_id}/review**

  Excluir uma resenha para um filme por um usuário.

  **Resposta:**

  ```json
  { "message": "Review excluído com sucesso" }
  ```

### Avaliações

- **POST /user/{username}/film/{film_id}/rating**

  Cria uma nova avaliação para um filme por um usuário.

  **Parâmetros da Requisição (form-data):**

  - `rating`: int (entre 1 e 10)

  **Resposta:**

  ```json
  { "message": "Rating adicionado com sucesso" }
  ```

- **GET /user/{username}/film/{film_id}/rating**

  Obter uma avaliação para um filme por um usuário.

  **Resposta:**

  ```json
  {
      "user_id": int,
      "film_id": int,
      "rating": int
  }
  ```

- **PUT /user/{username}/film/{film_id}/rating**

  Atualizar uma avaliação para um filme por um usuário.

  **Parâmetros da Requisição (form-data):**

  - `rating`: int (entre 1 e 10)

  **Resposta:**

  ```json
  { "message": "Rating atualizado com sucesso" }
  ```

- **DELETE /user/{username}/film/{film_id}/rating**

  Excluir uma avaliação para um filme por um usuário.

  **Resposta:**

  ```json
  { "message": "Rating excluído com sucesso" }
  ```

### Favoritos

- **POST /user/{username}/film/{film_id}/favorite**

  Adicionar um filme aos favoritos de um usuário.

  **Resposta:**

  ```json
  { "message": "Favorite adicionado com sucesso" }
  ```

- **GET /user/{username}/film/{film_id}/favorite**

  Obter um favorito para um filme por um usuário.

  **Resposta:**

  ```json
  {
      "user_id": int,
      "film_id": int,
      "favorite": boolean
  }
  ```

- **DELETE /user/{username}/film/{film_id}/favorite**

  Excluir um favorito para um filme por um usuário.

  **Resposta:**

  ```json
  { "message": "Favorite excluído com sucesso" }
  ```

## Contribuição

Sinta-se à vontade para fazer um fork do repositório e enviar pull requests. Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de mudar.

Por favor, certifique-se de atualizar os testes conforme apropriado.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
