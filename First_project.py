from tkinter import messagebox, ttk
import mysql.connector
import requests
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

def inserir_dados():  # Função que insere os dados no MySQL
    conexao = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conexao.cursor()
       
# Coletando os dados da interface
    data = entrada_data.get()
    distancia = entrada_distancia.get()
    tempo = entrada_tempo.get()
    ritmo = entrada_ritmo.get()
    tipo = entrada_tipo.get()
    observacoes = entrada_observacoes.get()
    
    
 # Verificando se os campos estão preenchidos
    if not data or not distancia or not tempo or not ritmo or not tipo or not observacoes:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        return
    
 # Comando SQL para inserir os dados
    comando = "INSERT INTO corrida (data, distancia, tempo, ritmo, tipo, observacoes) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (data, distancia, tempo, ritmo, tipo, observacoes)    
    
    try:
        cursor.execute(comando, valores)
        conexao.commit()  # Confirma a inserção no banco de dados
        messagebox.showinfo("Sucesso", f"Treino {tipo} adicionada com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao inserir dados: {err}")
    finally:
        cursor.close()
        conexao.close() 
        
    def atualizar_tabela():
        for row in tabela.get_children():
            tabela.delete(row)  # Remove todas as linhas da tabela atual

##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   

#                                                           INTERFACE


#CRIANDO A INTERFACE

janela = Tk() ## criando janela principal usando Tkinter
janela.title("Treinos corrida") # definindo o titulo da janela
janela.geometry("600x400")  # Definir tamanho fixo da janela
janela.resizable(False, False)

#Frame para titulo
frame_titulo = Frame(janela, bg="lightblue", bd=1500)
frame_titulo.pack(fill=X)

## criando frame
frame_treino = Frame(janela, bg="light gray", highlightthickness=10) # definindo cor "bg=light gray" e espessura da borda "hightthickness"
frame_treino.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9) # posicionando o frame com coordenadas e definindo o tamanho.


# criando variáveis para entrada de dados:
    # essas variáveis armazenam os dados inseridos pelo usuário nos campos de entrada(data, atividade e distância)
entrada_data = StringVar()
entrada_distancia = StringVar()
entrada_tempo = StringVar()
entrada_ritmo = StringVar()
entrada_tipo = StringVar()
entrada_observacoes = StringVar()

# campo de entrada para os dias, atividade e distancia
# label: é usado para exibir texto descritivo para usuário: "Data do treino, atividade e distância"
# entry: é o campo onde o usuário pode digitar os dados, cada campo está ligado a uma variável (StringVar)
    
Label(frame_treino, text="Data do treino:", bg="light gray").grid(column=0, row=0, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_data).grid(column=1, row=0, padx=10, pady=10)

Label(frame_treino, text="Distância (km):", bg="light gray").grid(column=0, row=1, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_distancia).grid(column=1, row=1, padx=10, pady=10)

Label(frame_treino, text="Tempo (min):", bg="light gray").grid(column=0, row=2, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_tempo).grid(column=1, row=2, padx=10, pady=10)

Label(frame_treino, text="Ritmo (min/km):", bg="light gray").grid(column=0, row=3, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_ritmo).grid(column=1, row=3, padx=10, pady=10)

Label(frame_treino, text="Tipo :", bg="light gray").grid(column=0, row=4, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_tipo).grid(column=1, row=4, padx=10, pady=10)

Label(frame_treino, text="Observacoes :", bg="light gray").grid(column=0, row=5, padx=10, pady=10, sticky="w")
Entry(frame_treino, textvariable=entrada_observacoes).grid(column=1, row=5, padx=10, pady=10)



# Criando botão para inserir atividade
ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")  # Personalizando o botão
botao_inserir = ttk.Button(frame_treino, text="Enviar atividade", command=inserir_dados)
botao_inserir.grid(column=1, row=7, padx=10, pady=10)


janela.mainloop()   # mantém a janela aberta.

# Função que será chamada quando o botão for pressionado
def mostrar_notificacao():
    messagebox.showinfo("Notificação", "Botão foi pressionado!")

# Tabela para exibir atividades
frame_tabela = Frame(janela)
frame_tabela.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)


# Definindo tabela
cols = ('Data do treino', 'Distância', 'Tempo', 'Ritmo', 'Tipo', 'Observacoes')
tabela = ttk.Treeview(frame_tabela, columns=cols, show='headings')
for col in cols:
    tabela.heading(col, text=col)
    tabela.column(col, width=100)
    
tabela.pack(fill=BOTH, expand=True)

janela.mainloop()


