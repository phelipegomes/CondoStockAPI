# Índice

* [Descrição do Projeto](#Descrição-do-Projeto)
* [Rotas Disponíveis](#Rotas-Disponíveis)
* [Instalação do projeto](#Instalação-do-Projeto)
* [Instalação da aplicação](#Instalação-da-aplicação)
* [Testes](#Testes)
* [Conclusão](#Conclusão)

# Descrição do Projeto

Esta aplicação trata-se de uma API desenvolvida utilizando o framework FastAPI, onde é importado funcionalidades que agilizam o processo de criação de ending-points usando a classe de rotas.

As querys são controladas pela biblioteca do python mysqlAlquemy e pyMySQL, auxilia respectivamente a criaçao de modelos e squemas e facil conexão com o banco de dados.

O servidor da aplicação utiliza o package uviCorn para criar ambiente virtual e executar a aplicaçao local e Anaconda para um deploy rápido da aplicação.

# Rotas Disponíveis

Aplicação configurada com rotas para a realização controle de produtos usando o ending-point /products:

```
POST: -> /products/: Inclui um novo produto com ID sequencial; 
GET/id -> /products/id: Busca um objeto a partir de um ID válido; 
GET/ -> /products: Mostra todos os produtos cadastrados; 
PUT/id -> products/id: Atualiza um objeto a partir de um ID válido; 
DELETE/id -> /products/id: Deleta um objeto a partir de um ID existente.
```

OBS: As rotas PUT e DELETE possuem previamente um validador de ID nulo.

Estrutura do banco de dados

A tabela principal do banco de dados "inventorydb" que será utilizado no projeto possui as seguintes características:

```
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int          | NO   | PRI | NULL    | auto_increment |
| name        | varchar(255) | YES  |     | NULL    |                |
| description | varchar(255) | YES  |     | NULL    |                |
| price       | float        | YES  |     | NULL    |                |
| quantity    | int          | YES  |     | NULL    |                |
| color       | varchar(255) | YES  |     | NULL    |                |
| serial      | varchar(255) | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
```
Em andamento: 

--> Pallet de testes ainda em desenvolvimento </br>
--> Auth com token JWT

# Instalação do Projeto

Para que a API funcione, siga os passos abaixo. Lembre-se: é necessário possuir o banco de dados mysql e executar o script em anexo para que as configuraçoes já definidas sejam lidas da forma correta. Caso contrário, siga o passo a passo de instalação do mySQL.

## Windows

Faça o download do instalador: Acesse o site oficial do MySQL e faça o download do instalador para Windows. 

Execute o instalador: Dê um duplo clique no arquivo baixado e execute o instalador. Siga as instruções na tela para completar a instalação.

Configuração do servidor: Durante o processo de instalação, você será solicitado a definir uma senha para o usuário root do MySQL e a configurar o servidor. Siga as instruções para definir as opções que deseja.

Verifique a instalação: Após a instalação, abra o prompt de comando e execute o comando abaixo para verificar se o MySQL está instalado corretamente.

```
mysql --version
```

## Linux (Ubuntu)

Atualize o gerenciador de pacotes: Abra o terminal e execute o comando abaixo para atualizar o gerenciador de pacotes.
```
sudo apt update
````

Instale o MySQL: Execute o comando abaixo para instalar o MySQL.
```
sudo apt install mysql-server
```

Configuração do servidor: Durante a instalação, você será solicitado a definir uma senha para o usuário root do MySQL e a configurar o servidor. Siga as instruções para definir as opções que deseja.

Verifique a instalação: Após a instalação, execute o comando abaixo para verificar se o MySQL está instalado corretamente.
```
mysql --version
```

## macOS

Faça o download do instalador: Acesse o site oficial do MySQL e faça o download do instalador para macOS. Download for macOS.

Execute o instalador: Dê um duplo clique no arquivo baixado e execute o instalador. Siga as instruções na tela para completar a instalação.

Configuração do servidor: Durante o processo de instalação, você será solicitado a definir uma senha para o usuário root do MySQL e a configurar o servidor. Siga as instruções para definir as opções que deseja.

Verifique a instalação: Após a instalação, abra o terminal e execute o comando abaixo para verificar se o MySQL está instalado corretamente.

```
mysql --version
```

Com a instalação concluída, execute o script deste repositorio no banco de dados para criar o banco de dados e sua tabela de produtos. Script link.

# Instalação da aplicação

(Opcional) Instale os pacotes necessários pelo requirements.txt: Basta executar o seguinte comando na raíz da aplicação:
```
pip install -r requirements.txt
```

Instale os pacotes necessários manualmente: Instale os pacotes com o comando abaixo.
```
pip install fastapi sqlalchemy pymysql uvicorn 
```

Instale o Anaconda: Baixe e instale o Anaconda a partir do site oficial.

Faça o download do repositorio em um caminho de sua preferência.
```
git clone https://github.com/phelipegomes/CondoStockAPI.git
```

Crie um ambiente virtual: Abra o terminal ou prompt de comando e crie um ambiente virtual usando o Anaconda com o comando abaixo.
```
conda create --name myenv
```

Ative o ambiente virtual: Ative o ambiente virtual com o comando abaixo.
```
conda activate myenv
```

Configure o banco de dados: No arquivo db.py que esta na pasta config da aplicação, altere somente os parametros YOUR_USER e YOUR_PASSWORD com suas respectivas credenciais configuradas na instalação inicial do mysql.

Exemplo:
```
db = Database("mysql+pymysql", "YOUR_USER", "YOUR_PASSWORD", "127.0.0.1:3306", "inventorydb")
```

Execute o servidor: Inicie o servidor usando o Uvicorn com o seguinte comando no terminal.
```
uvicorn app:app --reload
```

Teste a API: Agora a API está pronta para ser testada. Abra o navegador e acesse o endereço http://localhost:8000/docs para abrir a documentação gerada automaticamente pelo FastAPI. Você pode testar os endpoints diretamente na documentação ou usando um software como o Postman.

# Testes

Para realizar testes nas rotas, instale o package conforme o comando abaixo:
```
pip install pytest
```

Crie um banco de dados novo com o nome 'tests' e execute o seguinte script:

```
CREATE TABLE products(
  id INT NOTE NULL AUTO_INCREMENT, 
  name VARCHAR(255), 
  description VARCHAR(255), 
  price VARCHAR(255), 
  quantity VARCHAR(255), 
  color VARCHAR(255), 
  serial VARCHAR(255), 
  PRIMARY KEY (id)
);
```

Altere o nome da base de dados no arquivo db.py:
```
db = Database("mysql+pymysql", "YOUR_USER", "YOUR_PASSWORD", "127.0.0.1:3306", "tests")
```

Execute o arquivo de testes com o comando:
```
pytest
```

# Conclusão

CondoStockAPI é uma REST API desenvolvida com FastAPI, que usa a classe de rotas para criar endpoints. O banco de dados é gerenciado por PyMySQL e sqlalchemy. A API é configurada para controlar os produtos por meio do endpoint /products, que oferece rotas para incluir, buscar, atualizar e excluir produtos. 

O projeto está em desenvolvimento e, em breve, será implementado a autenticação com token JWT. O MySQL é o banco de dados recomendado e um script é fornecido para criar o banco de dados e sua tabela de produtos. Para instalar a aplicação, é necessário instalar o Anaconda e criar um ambiente virtual.
