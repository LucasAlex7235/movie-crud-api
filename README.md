## Documentação da API

#### Movies

```http
  GET /api/movies/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `api_key` | `string` | **Obrigatório**. A chave da sua API |


### Response - 200 (OK):


```json
[
    {
        "id": 1,
        "title": "O Poderoso Chefão",
        "duration": "2h55m",
        "rating": "R",
        "synopsis": "O filme conta a história da família Corleone, uma das mais poderosas famílias da máfia italiana nos Estados Unidos.",
        "orders": [
            {
                "id": 1,
                "buyed_at": "2022-01-01T20:00:00Z",
                "price": "10.00",
                "user": {
                    "id": 1,
                    "username": "admin",
                    "email": "admin@admin.com",
                    "first_name": "Admin",
                    "last_name": "Istrador",
                    "birthdate": null,
                    "is_superuser": true,
                    "is_employee": true
                }
            }
        ],
        "user": {
            "id": 1,
            "username": "admin",
            "email": "admin@admin.com",
            "first_name": "Admin",
            "last_name": "Istrador",
            "birthdate": null,
            "is_superuser": true,
            "is_employee": true
        },
        "added_by": "Admin Istrador"
    },
    {
        "id": 2,
        "title": "Matrix",
        "duration": "2h16m",
        "rating": "R",
        "synopsis": "Um programador de computadores é levado de sua vida cotidiana para se juntar a uma rebelião contra máquinas.",
        "orders": [],
        "user": {
            "id": 1,
            "username": "admin",
            "email": "admin@admin.com",
            "first_name": "Admin",
            "last_name": "Istrador",
            "birthdate": null,
            "is_superuser": true,
            "is_employee": true
        },
        "added_by": "Admin Istrador"
    }
]
```

#### Detalhes do filme

```http
  GET /api/movies/{movie_id}/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `movie_id`      | `int` | **Obrigatório**. O ID do filme que você quer |

### Response - 200 (OK):

```json
{
    "id": 1,
    "title": "Titanic",
    "duration": "194 min",
    "rating": "PG-13",
    "synopsis": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
    "orders": [
        {
            "id": 1,
            "buyed_at": "2023-02-24T15:28:09.556050Z",
            "price": 15.99,
            "user": {
                "id": 1,
                "username": "john.doe",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "birthdate": "1990-01-01",
                "is_employee": true
            }
        },
        {
            "id": 2,
            "buyed_at": "2023-02-23T16:11:20.769900Z",
            "price": 12.99,
            "user": {
                "id": 2,
                "username": "jane.doe",
                "email": "jane.doe@example.com",
                "first_name": "Jane",
                "last_name": "Doe",
                "birthdate": "1995-05-05",
                "is_employee": false
            }
        }
    ],
    "user": {
        "id": 1,
        "username": "john.doe",
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "birthdate": "1990-01-01",
        "is_employee": true
    },
    "added_by": "John Doe"
}
```

#### Pedidos do filme

```http
  POST /api/movies/{movie_id}/orders/
```
Esse endpoint permite que um usuário autenticado faça um pedido de um filme específico fornecendo seu movie_id e o preço pago pelo pedido.

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `movie_id`      | `int` | **Obrigatório**. O ID do filme que você quer |

### Request: 

```json
{
    "price": 15.99
}
```

### Response - 201 (created): 

```json
{
    "id": 3,
    "buyed_at": "2023-02-24T16:10:23.557223Z",
    "price": 15.99,
    "user": {
        "id": 3,
        "username": "james.smith",
        "email": "james.smith@example.com",
        "first_name": "James",
        "last_name": "Smith",
        "birthdate": "1985-03-20",
        "is_employee": false
    }
}
```

#### Update de Pedido do filme

```http
   PACTH /api/movies/{movie_id}/orders/{order_id}/
```
Esse endpoint permite que um usuário autenticado atualize um pedido de um filme específico fornecendo seu movie_id, o ID do pedido e as informações a serem atualizadas.

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `movie_id`      | `int` | **Obrigatório**. O ID do filme que você quer |
| `order_id`      | `int` | **Obrigatório**. O ID do pedido que você quer |

### Request: 

```json
{
    "price": 15.99
}
```

### Response - 200 (OK): 

```json
{
    "id": 3,
    "buyed_at": "2023-02-24T16:10:23.557223Z",
    "price": 14.99,
    "user": {
        "id": 3,
        "username": "james.smith",
        "email": "james.smith@example.com",
        "first_name": "James",
        "last_name": "Smith",
        "birthdate": "1995-12-15",
        "is_employee": false
    }
}
```

#### Delete de Pedido do filme

```http
   DELETE /api/movies/{movie_id}/orders/{order_id}/
```
Esse endpoint permite que um usuário autenticado delete um pedido de um filme específico fornecendo seu movie_id e o ID do pedido que deseja excluir.

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `movie_id`      | `int` | **Obrigatório**. O ID do filme que você quer |
| `order_id`      | `int` | **Obrigatório**. O ID do pedido que você quer |

### Response - 204 (No Content):

```json

```
