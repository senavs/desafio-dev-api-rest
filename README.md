# Desafio DEV API REST
DOCK Python challenge

## Como subir a aplicação
Clocar o repositório e rodar o seguinte comando na pasta raiz do projeto. É necessário ter o `docker` e `docker-compose` instalado.
```
docker-compose up
```

Após subir todos os containers, é necessário criar o schema, tabelas e registros default do banco de dados. Optou-se por não criar diretamente com o SQLAlchemy para mostrar os scripts de DDL e DML. 
Para isso, acessar `localhost:8081` e logar no MySQL Admin com as credenciais e rodar os scripts presentes na pasta `/database` na aba `SQL` ou no link `http://localhost:8081/index.php?route=/server/sql`. Seguir a ordem `ddl.sql`, `dml.sql` e `users.sql`

	host: database
	user: root
	password: foo-bar
	

Agora já é possível acessar e testar a aplicação através do swager no link `localhost:8080/docs`.

## Banco de dados (MER)
![database mer](https://raw.githubusercontent.com/senavs/desafio-dev-api-rest/master/docs/mer.png)

## Rotas

### Swagger
	GET /docs

### Usuário
	GET    /user/{id} -> buscar informações do usuário
	POST   /user/ -> criar um novo usuário

### Conta Bancária
	POST   /account/ -> criar nova conta
	GET    /account/{id} -> buscar informações da conta
	PUT    /account/{id} -> atualizar limite de saque por dia
	POST   /account/{id} -> ativar conta
	DELETE /account/{id} -> desativar conta
	POST   /account/user/{id} -> listar todas as contas de um usuário

### Operações
	GET    /account/operation/{id} -> listar transações de uma conta por período
	POST   /account/operation/deposit -> inserir dinheiro na conta
	POST   /account/operation/withdraw -> remove dinheiro da conta
	POST   /account/operation/transaction -> transfir dinheiro de uma conta para outra