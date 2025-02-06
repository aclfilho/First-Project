Projeto de Registro de Treinos de Corrida
Este projeto é uma aplicação desktop desenvolvida em Python com interface gráfica usando a biblioteca tkinter. Ele permite ao usuário registrar treinos de corrida, armazenando os dados em um banco de dados MySQL e exibindo-os em uma tabela na interface.



Funcionalidades
Registro de Treinos:

Permite ao usuário inserir dados como:

Data do treino.

Distância percorrida (em km).

Tempo gasto (em minutos).

Ritmo (em min/km).

Tipo de treino (ex: longão, tiros, etc.).

Observações adicionais.

Armazenamento no Banco de Dados:

Os dados são armazenados em um banco de dados MySQL.

Interface Gráfica:

Interface simples e intuitiva para inserção e visualização dos dados.

Validação de Dados:

Verifica se todos os campos foram preenchidos antes de inserir os dados no banco.


Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

Python 3.x:

Download Python

Bibliotecas Python:

Instale as bibliotecas necessárias usando o comando:
pip install mysql-connector-python requests python-dotenv


Banco de Dados MySQL:

Certifique-se de ter um servidor MySQL instalado e configurado.

Crie um banco de dados e uma tabela para armazenar os dados dos treinos. Exemplo de SQL:
CREATE DATABASE treinos_corrida;

USE treinos_corrida;

CREATE TABLE corrida (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    distancia FLOAT NOT NULL,
    tempo FLOAT NOT NULL,
    ritmo FLOAT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    observacoes TEXT
);



