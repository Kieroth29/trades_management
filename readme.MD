# trades_management

## Aplicação em Django para geração e gerenciamento de trades, e seus respectivos dados

### Dependências
- [Docker](https://docs.docker.com/desktop/windows/install/)
- [Compose](https://docs.docker.com/compose/install/)

### Instalação
O primeiro passo é clonar o projeto.
```
git clone https://github.com/kieroth29/trades_management.git
```

Em seguida, abra a pasta do projeto no terminal, e rode o seguinte comando para criar o container e o banco de dados:
```
docker-compose up
```

A seguinte mensagem confirmará o sucesso na inicialização:
```
web_1  | Django version 3.2.12, using settings 'trades_management.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```
Aperte Ctrl + C para encerrar a tarefa.

Para rodar o projeto, utilize no terminal, na pasta onde se encontra o arquivo _.yml_:
```
docker-compose up -d
```

E para interrompê-lo, é só utilizar
```
docker-compose down
```

Para criar as tabelas necessárias no banco de dados, insira o comando
```
docker-compose run web python3 manage.py migrate
```
### Utilização

#### Gerar trades (rota /stock_form)
Inserir os códigos dos ativos separados por vírgula, conforme instrução na página

Ex.: ATIVO1,ATIVO2,ATIVO3

#### Consultas (rota /stored_stock_data)
Escolher dentre as opções no select localizado no topo da página, e após inserir os dados, clicar no botão para exibir os resultados filtrados.

Consulta extra 1: Maior preço de ativo
Consulta extra 2: Filtrar por ativo