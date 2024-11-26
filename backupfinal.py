import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk


conexao_banco = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "clube_futebol"
)





def cadastro():
    
    def cadastrar_comissao():
        janela_comissao = tk.Toplevel()
        janela_comissao.title('Cadastro Comissão Técnica')
        janela_comissao.geometry('400x600')
        label_font = ("Bahnschrift SemiCondensed", 10)

        labels = [
            "nome", "cpf","data_nascimento", "telefone","endereco","cidade","estado","nacionalidade", "ocupacao","contrato"
        ]
        entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(janela_comissao, text=label_text, font=label_font)
            label.grid(row=i, column=0, padx=10, pady=5)
            
            entry = tk.Entry(janela_comissao, font=label_font)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        (
            entry_nome, entry_cpf, entry_data_nasc, entry_telefone,
            entry_endereco, entry_cidade, entry_estado, entry_nacionalidade,
            entry_ocupacao, entry_contrato
        ) = entries

        cursor = conexao_banco.cursor()
        def salvar_comissao():
            dados_jogador = (
                    entry_nome.get(),
                    entry_cpf.get(),
                    entry_data_nasc.get(),
                    entry_telefone.get(),
                    entry_endereco.get(),
                    entry_cidade.get(),
                    entry_estado.get(),
                    entry_nacionalidade.get(),
                    entry_ocupacao.get(),
                    entry_contrato.get(),
                )
            comando_sql = """
                INSERT INTO comissao_tecnica
                (nome, cpf, data_nascimento, telefone, endereco, cidade, estado, nacionalidade, ocupacao, contrato)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(comando_sql, dados_jogador)
            conexao_banco.commit()
            cursor.close()
            janela_comissao.destroy()
        botao_salvar = tk.Button(janela_comissao, text='Salvar', command=salvar_comissao)
        botao_salvar.grid(row=len(labels), column=1, pady=20)

    def cadastrar_campeonato():
        janela_campeonato = tk.Toplevel()
        janela_campeonato.title('Cadastro Campeonato')
        janela_campeonato.geometry('400x600')
        label_font = ("Bahnschrift SemiCondensed", 10)

        labels = [
            "nome", "qtd_jogo","inicio_camp", "fim_camp"
        ]
        entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(janela_campeonato, text=label_text, font=label_font)
            label.grid(row=i, column=0, padx=10, pady=5)
            
            entry = tk.Entry(janela_campeonato, font=label_font)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        (
            entry_nome, entry_qtd_jogo, entry_inicio_camp, entry_fim_camp
        ) = entries

        cursor = conexao_banco.cursor()
        def salvar_comissao():
            dados_jogador = (
                    entry_nome.get(),
                    entry_qtd_jogo.get(),
                    entry_inicio_camp(),
                    entry_fim_camp(),
                )
            comando_sql = """
                INSERT INTO campeonatos
                (nome, qtd_jogo, inicio_camp, fim_camp)
                VALUES (%s, %s, %s, %s)
                """
            cursor.execute(comando_sql, dados_jogador)
            conexao_banco.commit()
            cursor.close()
            janela_campeonato.destroy()
        botao_salvar = tk.Button(janela_campeonato, text='Salvar', command=salvar_comissao)
        botao_salvar.grid(row=len(labels), column=1, pady=20)

    def cadastrar_jogador():
        # Criando a janela de cadastro de jogador
        janela_jogador = tk.Toplevel()
        janela_jogador.title('Cadastro de Jogador')
        janela_jogador.geometry('400x600')
        label_font = ("Bahnschrift SemiCondensed", 10)

        # Campos de entrada
        labels = [
            "Nome", "CPF", "Altura", "Data de Nascimento", "Telefone", "Endereço", "Cidade", "Estado",
            "Nacionalidade", "Salário", "Número da Camisa", "Dominância", "Posição", "Contrato", "Condição"
        ]
        entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(janela_jogador, text=label_text, font=label_font)
            label.grid(row=i, column=0, padx=10, pady=5)
            
            entry = tk.Entry(janela_jogador, font=label_font)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)
        (
            entry_nome, entry_cpf, entry_altura, entry_data_nasc, entry_telefone,
            entry_endereco, entry_cidade, entry_estado, entry_nacionalidade,
            entry_salario, entry_numero_camisa, entry_dominancia, entry_posicao,
            entry_contrato, entry_condicao
        ) = entries

        cursor = conexao_banco.cursor()
        def salvar_jogador():
            dados_jogador = (
                    entry_nome.get(),
                    entry_cpf.get(),
                    entry_altura.get(),
                    entry_data_nasc.get(),
                    entry_telefone.get(),
                    entry_endereco.get(),
                    entry_cidade.get(),
                    entry_estado.get(),
                    entry_nacionalidade.get(),
                    entry_salario.get(),
                    entry_numero_camisa.get(),
                    entry_dominancia.get(),
                    entry_posicao.get(),
                    entry_contrato.get(),
                    entry_condicao.get()
                )
            comando_sql = f'INSERT INTO jogadores (nome, cpf, altura, data_nascimento, telefone, endereco, cidade, estado, nacionalidade, salario, numero_camisa, dominancia, posicao, contrato, condicao)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(comando_sql, dados_jogador)
            conexao_banco.commit()
            cursor.close()
            janela_jogador.destroy()
        botao_salvar = tk.Button(janela_jogador, text='Salvar', command=salvar_jogador)
        botao_salvar.grid(row=len(labels), column=1, pady=20)

    def cadastrar_jogador_no_campeonato():
        # Criar a janela para cadastro
        janela_cadastro = tk.Toplevel()
        janela_cadastro.title("Cadastrar Jogador no Campeonato")
        janela_cadastro.geometry("400x400")
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e Entry para ID do jogador
        tk.Label(janela_cadastro, text="ID do Jogador:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_id_jogador = tk.Entry(janela_cadastro, font=label_font)
        entry_id_jogador.grid(row=0, column=1, padx=10, pady=10)

        # Label e Entry para ID do campeonato
        tk.Label(janela_cadastro, text="ID do Campeonato:", font=label_font).grid(row=1, column=0, padx=10, pady=10)
        entry_id_campeonato = tk.Entry(janela_cadastro, font=label_font)
        entry_id_campeonato.grid(row=1, column=1, padx=10, pady=10)

        # Label e Entry para gols
        tk.Label(janela_cadastro, text="Gols:", font=label_font).grid(row=2, column=0, padx=10, pady=10)
        entry_gols = tk.Entry(janela_cadastro, font=label_font)
        entry_gols.grid(row=2, column=1, padx=10, pady=10)

        # Label e Entry para cartões amarelos
        tk.Label(janela_cadastro, text="Cartões Amarelos:", font=label_font).grid(row=3, column=0, padx=10, pady=10)
        entry_cartoes_amarelos = tk.Entry(janela_cadastro, font=label_font)
        entry_cartoes_amarelos.grid(row=3, column=1, padx=10, pady=10)

        # Label e Entry para cartões vermelhos
        tk.Label(janela_cadastro, text="Cartões Vermelhos:", font=label_font).grid(row=4, column=0, padx=10, pady=10)
        entry_cartoes_vermelhos = tk.Entry(janela_cadastro, font=label_font)
        entry_cartoes_vermelhos.grid(row=4, column=1, padx=10, pady=10)

        # Função para salvar os dados
        def salvar():
            jogador_id = entry_id_jogador.get()
            campeonato_id = entry_id_campeonato.get()
            gols = entry_gols.get() or 0  # Se vazio, insere 0
            cartoes_amarelos = entry_cartoes_amarelos.get() or 0
            cartoes_vermelhos = entry_cartoes_vermelhos.get() or 0

            try:
                cursor = conexao_banco.cursor()
                comando_sql = """
                INSERT INTO jogador_campeonato (id_jogador, id_campeonato, gols, cartoes_amarelos, cartoes_vermelhos)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(comando_sql, (jogador_id, campeonato_id, gols, cartoes_amarelos, cartoes_vermelhos))
                conexao_banco.commit()
                cursor.close()
                tk.Label(janela_cadastro, text="Cadastro realizado com sucesso!", fg="green", font=label_font).grid(row=6, column=0, columnspan=2)
            except Exception as e:
                tk.Label(janela_cadastro, text=f"Erro: {e}", fg="red", font=label_font).grid(row=6, column=0, columnspan=2)

        # Botão para salvar
        botao_salvar = tk.Button(janela_cadastro, text="Salvar", command=salvar, font=label_font, bg="green", fg="white")
        botao_salvar.grid(row=5, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_cadastro, text="Voltar", command=janela_cadastro.destroy, font=label_font)
        botao_voltar.grid(row=7, column=0, columnspan=2, pady=10)

    def atualizar_estatisticas():
        # Janela para atualizar estatísticas
        janela_atualizar = tk.Toplevel()
        janela_atualizar.title("Atualizar Estatísticas")
        janela_atualizar.geometry("600x400")
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Campo para selecionar o jogador por ID ou Nome
        tk.Label(janela_atualizar, text="ID ou Nome do Jogador:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_jogador = tk.Entry(janela_atualizar, font=label_font)
        entry_jogador.grid(row=0, column=1, padx=10, pady=10)

        # Campo para selecionar o campeonato pelo ID
        tk.Label(janela_atualizar, text="ID do Campeonato:", font=label_font).grid(row=1, column=0, padx=10, pady=10)
        entry_id_campeonato = tk.Entry(janela_atualizar, font=label_font)
        entry_id_campeonato.grid(row=1, column=1, padx=10, pady=10)

        # Campos para atualizar os valores de gols e cartões
        tk.Label(janela_atualizar, text="Atualizar Gols:", font=label_font).grid(row=2, column=0, padx=10, pady=10)
        entry_gols = tk.Entry(janela_atualizar, font=label_font)
        entry_gols.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(janela_atualizar, text="Atualizar Cartões Amarelos:", font=label_font).grid(row=3, column=0, padx=10, pady=10)
        entry_cartoes_amarelos = tk.Entry(janela_atualizar, font=label_font)
        entry_cartoes_amarelos.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(janela_atualizar, text="Atualizar Cartões Vermelhos:", font=label_font).grid(row=4, column=0, padx=10, pady=10)
        entry_cartoes_vermelhos = tk.Entry(janela_atualizar, font=label_font)
        entry_cartoes_vermelhos.grid(row=4, column=1, padx=10, pady=10)

        def confirmar_atualizacao():
            jogador = entry_jogador.get().strip()
            id_campeonato = entry_id_campeonato.get().strip()
            gols = entry_gols.get().strip()
            cartoes_amarelos = entry_cartoes_amarelos.get().strip()
            cartoes_vermelhos = entry_cartoes_vermelhos.get().strip()

            if not id_campeonato or (not jogador):
                tk.Label(janela_atualizar, text="Jogador ou Campeonato não preenchido!", fg="red", font=label_font).grid(row=6, column=0, columnspan=2, pady=10)
                return

            try:
                # Conexão com o banco de dados
                cursor = conexao_banco.cursor()

                # Verificar se jogador foi inserido por ID ou Nome
                if jogador.isdigit():
                    condicao_jogador = "id_jogador = %s"
                    parametros = (jogador, id_campeonato)
                else:
                    condicao_jogador = "nome = %s"
                    parametros = (jogador, id_campeonato)

                # Verifica se o registro existe
                cursor.execute(f"SELECT * FROM jogador_campeonato WHERE {condicao_jogador} AND id_campeonato = %s", parametros)
                registro = cursor.fetchone()

                if not registro:
                    tk.Label(janela_atualizar, text="Jogador ou Campeonato não encontrados!", fg="red", font=label_font).grid(row=6, column=0, columnspan=2, pady=10)
                    return

                # Atualiza os valores informados
                comando_update = f"""
                    UPDATE jogador_campeonato 
                    SET gols = %s, cartoes_amarelos = %s, cartoes_vermelhos = %s 
                    WHERE {condicao_jogador} AND id_campeonato = %s
                """
                cursor.execute(comando_update, (gols, cartoes_amarelos, cartoes_vermelhos, *parametros))
                conexao_banco.commit()
                cursor.close()

                tk.Label(janela_atualizar, text="Estatísticas atualizadas com sucesso!", fg="green", font=label_font).grid(row=6, column=0, columnspan=2, pady=10)
            except Exception as e:
                tk.Label(janela_atualizar, text=f"Erro ao atualizar: {e}", fg="red", font=label_font).grid(row=6, column=0, columnspan=2, pady=10)

        # Botão para confirmar atualização
        botao_confirmar = tk.Button(janela_atualizar, text="Atualizar", font=label_font, bg="green", fg="white", command=confirmar_atualizacao)
        botao_confirmar.grid(row=5, column=0, columnspan=2, pady=20)

        # Botão para voltar
        botao_voltar = tk.Button(janela_atualizar, text="Voltar", font=label_font, command=janela_atualizar.destroy)
        botao_voltar.grid(row=7, column=0, columnspan=2, pady=10)

    janela2 = tk.Toplevel()
    janela2.title('Cadastro')
    janela2.geometry('400x400')
    label_font = ("Bahnschrift SemiCondensed", 18)
    label_nome = tk.Label(janela2)
    label_nome.grid(row=0, column=0)
    janela2.configure(bg="black")

  
    botao_cadastrar = tk.Button(janela2, text='CADASTRAR JOGADOR', font = label_font ,command=cadastrar_jogador,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_cadastrar.grid(row=1, column=2, columnspan=2)
    botao_comissao = tk.Button(janela2, text = 'CADASTRAR COMISSÃO',font = label_font , command=cadastrar_comissao,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_comissao.grid(row = 2, column=2)
    botao_campeonato = tk.Button(janela2, text = 'CADASTRAR CAMPEONATO',font = label_font , command = cadastrar_campeonato,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_campeonato.grid(row = 3, column=2)
    botao_inscrever_campeonato = tk.Button(janela2, text='INSCREVER JOGADOR EM CAMPEONATO', font = label_font ,command=cadastrar_jogador_no_campeonato,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_inscrever_campeonato.grid(row = 4, column=2)
    botao_cadastrar_gol = tk.Button(janela2, text='ATUALIZAR ESTATÍSTICAS', font = label_font, command=atualizar_estatisticas,fg="white", bg='black',bd=0,highlightthickness=0)
    botao_cadastrar_gol.grid(row = 6, column=2, columnspan=2)
 
    botao_voltar = tk.Button(janela2, text='VOLTAR',font = label_font , command=janela2.destroy,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_voltar.grid(row=8, column=2, columnspan=2)

def update():

    def update_jogador():
        janela_update_jogador = tk.Toplevel()
        janela_update_jogador.title('Alteração de Jogador')
        janela_update_jogador.geometry('800x800')
        label_font = ("Bahnschrift SemiCondensed", 10)
        label_id = tk.Label(janela_update_jogador, text="Qual o ID do jogador?", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_update_jogador, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        def selecionar_coluna(coluna):
            label_valor = tk.Label(janela_update_jogador, text=f"Novo valor para {coluna}:", font=label_font)
            label_valor.grid(row=2, column=0, padx=10, pady=10)

            entry_valor = tk.Entry(janela_update_jogador, font=label_font)
            entry_valor.grid(row=2, column=1, padx=10, pady=10)

            def confirmar_alteracao():
                novo_valor = entry_valor.get()
                jogador_id = entry_id.get()

                if not jogador_id or not novo_valor:
                    tk.Label(janela_update_jogador, text="ID ou valor inválido!", font=label_font, fg="red").grid(row=4, column=0, columnspan=2, pady=10)
                    return

                try:
                    cursor = conexao_banco.cursor()
                    comando_sql = f"UPDATE jogadores SET {coluna} = %s WHERE id = %s"
                    cursor.execute(comando_sql, (novo_valor, jogador_id))
                    conexao_banco.commit()
                    cursor.close()

                    tk.Label(janela_update_jogador, text=f"{coluna} atualizado com sucesso!", font=label_font, fg="green").grid(row=3, column=0, columnspan=2, pady=10)
                except Exception as e:
                    tk.Label(janela_update_jogador, text=f"Erro: {e}", font=label_font, fg="red").grid(row=3, column=0, columnspan=2, pady=10)

            botao_confirmar = tk.Button(janela_update_jogador, text="Confirmar Alteração", command=confirmar_alteracao, font=label_font)
            botao_confirmar.grid(row=2, column=2, padx=10, pady=10)

        def confirmar_id():
            jogador_id = entry_id.get()

            if not jogador_id:
                tk.Label(janela_update_jogador, text="Por favor, insira um ID!", font=label_font, fg="red").grid(row=1, column=0, columnspan=2, pady=10)
                return

            colunas = ["nome", "cpf", "altura", "data_nascimento", "telefone", "endereco", "cidade", 
                       "estado", "nacionalidade", "salario", "numero_camisa", "dominancia", "posicao", 
                       "contrato", "condicao"]
            
            for i, coluna in enumerate(colunas):
                botao_coluna = tk.Button(janela_update_jogador, text=f"Alterar {coluna.capitalize()}", 
                                         command=lambda c=coluna: selecionar_coluna(c), font=label_font)
                botao_coluna.grid(row=i+2, column=0, padx=10, pady=5)

        botao_confirmar_id = tk.Button(janela_update_jogador, text="Confirmar ID", command=confirmar_id, font=label_font)
        botao_confirmar_id.grid(row=1, column=1, pady=20)


    def update_campeonato():
        janela_update_campeonato = tk.Toplevel()
        janela_update_campeonato.title('Alteração de comissao')
        janela_update_campeonato.geometry('800x800')
        label_font = ("Bahnschrift SemiCondensed", 10)

        label_id = tk.Label(janela_update_campeonato, text="Qual o ID do comissao?", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_update_campeonato, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        def selecionar_coluna(coluna):
            label_valor = tk.Label(janela_update_campeonato, text=f"Novo valor para {coluna}:", font=label_font)
            label_valor.grid(row=2, column=0, padx=10, pady=10)

            entry_valor = tk.Entry(janela_update_campeonato, font=label_font)
            entry_valor.grid(row=2, column=1, padx=10, pady=10)

            def confirmar_alteracao():
                novo_valor = entry_valor.get()
                caompeonato_id = entry_id.get()

                # Verificar se ID e novo valor foram fornecidos
                if not caompeonato_id or not novo_valor:
                    tk.Label(janela_update_campeonato, text="ID ou valor inválido!", font=label_font, fg="red").grid(row=4, column=0, columnspan=2, pady=10)
                    return

                try:
                    # Atualizar o banco de dados
                    cursor = conexao_banco.cursor()
                    comando_sql = f"UPDATE campeonatos SET {coluna} = %s WHERE id = %s"
                    cursor.execute(comando_sql, (novo_valor, caompeonato_id))
                    conexao_banco.commit()
                    cursor.close()

                    # Mensagem de sucesso
                    tk.Label(janela_update_campeonato, text=f"{coluna} atualizado com sucesso!", font=label_font, fg="green").grid(row=3, column=0, columnspan=2, pady=10)
                except Exception as e:
                    tk.Label(janela_update_campeonato, text=f"Erro: {e}", font=label_font, fg="red").grid(row=3, column=0, columnspan=2, pady=10)

            # Botão para confirmar a alteração
            botao_confirmar = tk.Button(janela_update_campeonato, text="Confirmar Alteração", command=confirmar_alteracao, font=label_font)
            botao_confirmar.grid(row=2, column=2, padx=10, pady=10)

        def confirmar_id():
            campeonato_id = entry_id.get()

            # Verificar se o ID foi fornecido
            if not campeonato_id:
                tk.Label(janela_update_campeonato, text="Por favor, insira um ID!", font=label_font, fg="red").grid(row=1, column=0, columnspan=2, pady=10)
                return

            # Exibir botões para cada coluna a ser alterada
            colunas = ["nome", "qnt_jogo", "inicio_camp", "fim_camp"]
            
            for i, coluna in enumerate(colunas):
                botao_coluna = tk.Button(janela_update_campeonato, text=f"Alterar {coluna.capitalize()}", 
                                         command=lambda c=coluna: selecionar_coluna(c), font=label_font)
                botao_coluna.grid(row=i+2, column=0, padx=10, pady=5)

        # Botão para confirmar o ID e exibir opções de alteração
        botao_confirmar_id = tk.Button(janela_update_campeonato, text="Confirmar ID", command=confirmar_id, font=label_font)
        botao_confirmar_id.grid(row=1, column=1, pady=20)


    def update_comissao():
       # Configuração inicial da janela
        janela_update_comissao = tk.Toplevel()
        janela_update_comissao.title('Alteração de comissao')
        janela_update_comissao.geometry('800x800')
        label_font = ("Bahnschrift SemiCondensed", 10)

        # Entrada para o ID da comissao
        label_id = tk.Label(janela_update_comissao, text="Qual o ID da comissao?", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_update_comissao, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        def selecionar_coluna(coluna):
            # Pergunta para o novo valor da coluna selecionada
            label_valor = tk.Label(janela_update_comissao, text=f"Novo valor para {coluna}:", font=label_font)
            label_valor.grid(row=2, column=0, padx=10, pady=10)

            entry_valor = tk.Entry(janela_update_comissao, font=label_font)
            entry_valor.grid(row=2, column=1, padx=10, pady=10)

            def confirmar_alteracao():
                novo_valor = entry_valor.get()
                caompeonato_id = entry_id.get()

                # Verificar se ID e novo valor foram fornecidos
                if not caompeonato_id or not novo_valor:
                    tk.Label(janela_update_comissao, text="ID ou valor inválido!", font=label_font, fg="red").grid(row=4, column=0, columnspan=2, pady=10)
                    return

                try:
                    # Atualizar o banco de dados
                    cursor = conexao_banco.cursor()
                    comando_sql = f"UPDATE comissao_tecnica SET {coluna} = %s WHERE id = %s"
                    cursor.execute(comando_sql, (novo_valor, caompeonato_id))
                    conexao_banco.commit()
                    cursor.close()

                    # Mensagem de sucesso
                    tk.Label(janela_update_comissao, text=f"{coluna} atualizado com sucesso!", font=label_font, fg="green").grid(row=3, column=0, columnspan=2, pady=10)
                except Exception as e:
                    tk.Label(janela_update_comissao, text=f"Erro: {e}", font=label_font, fg="red").grid(row=3, column=0, columnspan=2, pady=10)

            # Botão para confirmar a alteração
            botao_confirmar = tk.Button(janela_update_comissao, text="Confirmar Alteração", command=confirmar_alteracao, font=label_font)
            botao_confirmar.grid(row=2, column=2, padx=10, pady=10)

        def confirmar_id():
            comissao_id = entry_id.get()

            # Verificar se o ID foi fornecido
            if not comissao_id:
                tk.Label(janela_update_comissao, text="Por favor, insira um ID!", font=label_font, fg="red").grid(row=1, column=0, columnspan=2, pady=10)
                return

            # Exibir botões para cada coluna a ser alterada
            colunas = ["nome", "cpf", "data_nascimento", "telefone", "endereco", "cidade", "estado", "nacionalidade", "ocupacao", "contrato"]
            
            for i, coluna in enumerate(colunas):
                botao_coluna = tk.Button(janela_update_comissao, text=f"Alterar {coluna.capitalize()}", 
                                         command=lambda c=coluna: selecionar_coluna(c), font=label_font)
                botao_coluna.grid(row=i+2, column=0, padx=10, pady=5)

        # Botão para confirmar o ID e exibir opções de alteração
        botao_confirmar_id = tk.Button(janela_update_comissao, text="Confirmar ID", command=confirmar_id, font=label_font)
        botao_confirmar_id.grid(row=1, column=1, pady=20)


    janela3 = tk.Toplevel()
    janela3.title('Cadastro')
    janela3.geometry('260x300')
    label_font = ("Bahnschrift SemiCondensed", 17)
    label_nome = tk.Label(janela3,bg="black")
    label_nome.grid(row=0, column=0)
    janela3.configure(bg="black")

    jogador_update = tk.Button(janela3, text='ALTERAR JOGADOR',font = label_font , command=update_jogador,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    jogador_update.grid(row=1, column=3, columnspan=2)
    campeonato_update = tk.Button(janela3, text='ALTERAR CAMPEONATO',font = label_font , command=update_campeonato,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    campeonato_update.grid(row = 2, column = 3, columnspan=2)
    comissao_update = tk.Button(janela3, text = 'ALTERAR COMISSÃO',font = label_font , command=update_comissao,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    comissao_update.grid(row = 3, column = 3, columnspan=2)
    botao_voltar = tk.Button(janela3, text='VOLTAR',font = label_font , command=janela3.destroy,fg="white", bg='black',bd=0,highlightthickness=0,pady=10)
    botao_voltar.grid(row=4, column=3, columnspan=2)


def excluir():

    def excluir_jogador():
        # Cria uma nova janela para exclusão
        janela_excluir_jogador = tk.Toplevel()
        janela_excluir_jogador.title('Excluir Jogador')
        janela_excluir_jogador.geometry('400x200')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para entrada do ID
        label_id = tk.Label(janela_excluir_jogador, text="Digite o ID do jogador a ser excluído:", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_excluir_jogador, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Função para confirmar exclusão
        def confirmar_exclusao():
            jogador_id = entry_id.get()  # Obtém o ID fornecido pelo usuário

            if not jogador_id.isdigit():
                # Valida se o ID é um número
                tk.Label(janela_excluir_jogador, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Executa o comando SQL para excluir o jogador
                cursor = conexao_banco.cursor()
                comando_sql = "DELETE FROM jogadores WHERE id = %s"
                cursor.execute(comando_sql, (jogador_id,))
                conexao_banco.commit()
                cursor.close()

                # Mensagem de sucesso
                tk.Label(janela_excluir_jogador, text="Jogador excluído com sucesso!", fg="green", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
            except Exception as e:
                # Exibe uma mensagem de erro
                tk.Label(janela_excluir_jogador, text=f"Erro ao excluir: {e}", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)

        # Botão para confirmar exclusão
        botao_confirmar = tk.Button(janela_excluir_jogador, text="Excluir", command=confirmar_exclusao, font=label_font, bg="red", fg="white")
        botao_confirmar.grid(row=1, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_excluir_jogador, text="Voltar", command=janela_excluir_jogador.destroy, font=label_font)
        botao_voltar.grid(row=3, column=0, columnspan=2, pady=10)

    def excluir_campeonato():
        # Cria uma nova janela para exclusão
        janela_excluir_campeonato = tk.Toplevel()
        janela_excluir_campeonato.title('Excluir campeonato')
        janela_excluir_campeonato.geometry('400x200')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para entrada do ID
        label_id = tk.Label(janela_excluir_campeonato, text="Digite o ID do campeonato a ser excluído:", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_excluir_campeonato, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Função para confirmar exclusão
        def confirmar_exclusao():
            campeonato_id = entry_id.get()  # Obtém o ID fornecido pelo usuário

            if not campeonato_id.isdigit():
                # Valida se o ID é um número
                tk.Label(janela_excluir_campeonato, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Executa o comando SQL para excluir o campeonato
                cursor = conexao_banco.cursor()
                comando_sql = "DELETE FROM campeonatos WHERE id = %s"
                cursor.execute(comando_sql, (campeonato_id,))
                conexao_banco.commit()
                cursor.close()

                # Mensagem de sucesso
                tk.Label(janela_excluir_campeonato, text="campeonato excluído com sucesso!", fg="green", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
            except Exception as e:
                # Exibe uma mensagem de erro
                tk.Label(janela_excluir_campeonato, text=f"Erro ao excluir: {e}", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)

        # Botão para confirmar exclusão
        botao_confirmar = tk.Button(janela_excluir_campeonato, text="Excluir", command=confirmar_exclusao, font=label_font, bg="red", fg="white")
        botao_confirmar.grid(row=1, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_excluir_campeonato, text="Voltar", command=janela_excluir_campeonato.destroy, font=label_font)
        botao_voltar.grid(row=3, column=0, columnspan=2, pady=10)

    def excluir_comissao():

        # Cria uma nova janela para exclusão
        janela_excluir_comissao = tk.Toplevel()
        janela_excluir_comissao.title('Excluir comissao')
        janela_excluir_comissao.geometry('400x200')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para entrada do ID
        label_id = tk.Label(janela_excluir_comissao, text="Digite o ID do comissao a ser excluído:", font=label_font)
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(janela_excluir_comissao, font=label_font)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Função para confirmar exclusão
        def confirmar_exclusao():
            comissao_id = entry_id.get()  # Obtém o ID fornecido pelo usuário

            if not comissao_id.isdigit():
                # Valida se o ID é um número
                tk.Label(janela_excluir_comissao, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Executa o comando SQL para excluir o comissao
                cursor = conexao_banco.cursor()
                comando_sql = "DELETE FROM comissao_tecnica WHERE id = %s"
                cursor.execute(comando_sql, (comissao_id,))
                conexao_banco.commit()
                cursor.close()

                # Mensagem de sucesso
                tk.Label(janela_excluir_comissao, text="comissao excluído com sucesso!", fg="green", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)
            except Exception as e:
                # Exibe uma mensagem de erro
                tk.Label(janela_excluir_comissao, text=f"Erro ao excluir: {e}", fg="red", font=label_font).grid(
                    row=2, column=0, columnspan=2, pady=10)

        # Botão para confirmar exclusão
        botao_confirmar = tk.Button(janela_excluir_comissao, text="Excluir", command=confirmar_exclusao, font=label_font, bg="red", fg="white")
        botao_confirmar.grid(row=1, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_excluir_comissao, text="Voltar", command=janela_excluir_comissao.destroy, font=label_font)
        botao_voltar.grid(row=3, column=0, columnspan=2, pady=10)
    
    janela4 = tk.Toplevel()
    janela4.title('Excluir')
    janela4.geometry('250x220')
    label_nome = tk.Label(janela4,bg="black")
    label_nome.grid(row=0, column=0)
    label_font = ("Bahnschrift SemiCondensed", 18)
    janela4.configure(bg="black")
    botao_excluir = tk.Button(janela4, text = 'EXCLUIR JOGADOR',font = label_font ,  command = excluir_jogador,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    botao_excluir.grid(row=1, column=2, columnspan=2)
    comissao_excluir = tk.Button(janela4, text = 'EXCLUIR COMISSÃO',font = label_font ,  command = excluir_comissao,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    comissao_excluir.grid(row=2, column=2, columnspan=2)
    campeonato_excluir = tk.Button(janela4, text = 'EXCLUIR CAMPEONATO',font = label_font ,  command = excluir_campeonato,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    campeonato_excluir.grid(row=3, column=2, columnspan=2)
    botao_voltar = tk.Button(janela4, text='VOLTAR', font = label_font ,command=janela4.destroy,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    botao_voltar.grid(row=4, column=2, columnspan=2)

def pesquisar():

    def pesquisar_jogador():
        # Cria uma nova janela para pesquisa
        janela_pesquisar_jogador = tk.Toplevel()
        janela_pesquisar_jogador.title('Pesquisar Jogador')
        janela_pesquisar_jogador.geometry('800x600')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para selecionar a coluna
        label_coluna = tk.Label(janela_pesquisar_jogador, text="Escolha a coluna para buscar:", font=label_font)
        label_coluna.grid(row=0, column=0, padx=10, pady=10)

        # Combobox para selecionar a coluna
        colunas = [
            "id", "nome", "cpf", "altura", "data_nascimento", "telefone", "endereco", 
            "cidade", "estado", "nacionalidade", "salario", "numero_camisa", 
            "dominancia", "posicao", "contrato", "condicao"
        ]
        coluna_selecionada = ttk.Combobox(janela_pesquisar_jogador, values=colunas, font=label_font)
        coluna_selecionada.grid(row=0, column=1, padx=10, pady=10)
        coluna_selecionada.set("nome")  # Define um valor padrão

        # Campo para entrada do valor a buscar
        label_valor = tk.Label(janela_pesquisar_jogador, text="Digite o valor a buscar:", font=label_font)
        label_valor.grid(row=1, column=0, padx=10, pady=10)

        entry_valor = tk.Entry(janela_pesquisar_jogador, font=label_font)
        entry_valor.grid(row=1, column=1, padx=10, pady=10)

        # Função para realizar a busca
        def realizar_pesquisa():
            coluna = coluna_selecionada.get()
            valor = entry_valor.get()

            if not coluna or not valor:
                # Verifica se ambos os campos foram preenchidos
                tk.Label(janela_pesquisar_jogador, text="Por favor, preencha todos os campos.", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)
                return

            try:
                cursor = conexao_banco.cursor()

                # Adiciona curingas para busca parcial
                comando_sql = f"SELECT * FROM jogadores WHERE {coluna} LIKE %s"
                cursor.execute(comando_sql, (f"%{valor}%",))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados em uma tabela
                tabela = ttk.Treeview(janela_pesquisar_jogador, columns=colunas, show="headings", height=15)
                tabela.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

                # Configura os cabeçalhos da tabela
                for col in colunas:
                    tabela.heading(col, text=col.capitalize())
                    tabela.column(col, width=100)

                # Insere os resultados na tabela
                for linha in resultados:
                    tabela.insert("", "end", values=linha)

                if not resultados:
                    tk.Label(janela_pesquisar_jogador, text="Nenhum resultado encontrado.", fg="red", font=label_font).grid(
                        row=5, column=0, columnspan=2, pady=10)

            except Exception as e:
                tk.Label(janela_pesquisar_jogador, text=f"Erro na busca: {e}", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)

        # Botão para realizar a busca
        botao_pesquisar = tk.Button(janela_pesquisar_jogador, text="Pesquisar", command=realizar_pesquisa, font=label_font, bg="blue", fg="white")
        botao_pesquisar.grid(row=2, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_pesquisar_jogador, text="Voltar", command=janela_pesquisar_jogador.destroy, font=label_font)
        botao_voltar.grid(row=5, column=0, columnspan=2, pady=10)

    def pesquisar_comissao():

        # Cria uma nova janela para pesquisa
        janela_pesquisar_comissao = tk.Toplevel()
        janela_pesquisar_comissao.title('Pesquisar comissao')
        janela_pesquisar_comissao.geometry('800x600')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para selecionar a coluna
        label_coluna = tk.Label(janela_pesquisar_comissao, text="Escolha a coluna para buscar:", font=label_font)
        label_coluna.grid(row=0, column=0, padx=10, pady=10)

        # Combobox para selecionar a coluna
        colunas = ["nome", "cpf", "data_nascimento", "telefone", "endereco", "cidade", "estado", "nacionalidade", "ocupacao", "contrato"]
        coluna_selecionada = ttk.Combobox(janela_pesquisar_comissao, values=colunas, font=label_font)
        coluna_selecionada.grid(row=0, column=1, padx=10, pady=10)
        coluna_selecionada.set("nome")  # Define um valor padrão

        # Campo para entrada do valor a buscar
        label_valor = tk.Label(janela_pesquisar_comissao, text="Digite o valor a buscar:", font=label_font)
        label_valor.grid(row=1, column=0, padx=10, pady=10)

        entry_valor = tk.Entry(janela_pesquisar_comissao, font=label_font)
        entry_valor.grid(row=1, column=1, padx=10, pady=10)

        # Função para realizar a busca
        def realizar_pesquisa():
            coluna = coluna_selecionada.get()
            valor = entry_valor.get()

            if not coluna or not valor:
                # Verifica se ambos os campos foram preenchidos
                tk.Label(janela_pesquisar_comissao, text="Por favor, preencha todos os campos.", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)
                return

            try:
                cursor = conexao_banco.cursor()

                # Adiciona curingas para busca parcial
                comando_sql = f"SELECT * FROM comissao_tecnica WHERE {coluna} LIKE %s"
                cursor.execute(comando_sql, (f"%{valor}%",))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados em uma tabela
                tabela = ttk.Treeview(janela_pesquisar_comissao, columns=colunas, show="headings", height=15)
                tabela.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

                # Configura os cabeçalhos da tabela
                for col in colunas:
                    tabela.heading(col, text=col.capitalize())
                    tabela.column(col, width=100)

                # Insere os resultados na tabela
                for linha in resultados:
                    tabela.insert("", "end", values=linha)

                if not resultados:
                    tk.Label(janela_pesquisar_comissao, text="Nenhum resultado encontrado.", fg="red", font=label_font).grid(
                        row=5, column=0, columnspan=2, pady=10)

            except Exception as e:
                tk.Label(janela_pesquisar_comissao, text=f"Erro na busca: {e}", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)

        # Botão para realizar a busca
        botao_pesquisar = tk.Button(janela_pesquisar_comissao, text="Pesquisar", command=realizar_pesquisa, font=label_font, bg="blue", fg="white")
        botao_pesquisar.grid(row=2, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_pesquisar_comissao, text="Voltar", command=janela_pesquisar_comissao.destroy, font=label_font)
        botao_voltar.grid(row=5, column=0, columnspan=2, pady=10)

    def pesquisar_campeonato():

        # Cria uma nova janela para pesquisa
        janela_pesquisar_campeonato = tk.Toplevel()
        janela_pesquisar_campeonato.title('Pesquisar campeonato')
        janela_pesquisar_campeonato.geometry('800x600')
        label_font = ("Bahnschrift SemiCondensed", 12)

        # Label e campo para selecionar a coluna
        label_coluna = tk.Label(janela_pesquisar_campeonato, text="Escolha a coluna para buscar:", font=label_font)
        label_coluna.grid(row=0, column=0, padx=10, pady=10)

        # Combobox para selecionar a coluna
        colunas = ["nome", "qnt_jogo", "inicio_camp", "fim_camp"]
        coluna_selecionada = ttk.Combobox(janela_pesquisar_campeonato, values=colunas, font=label_font)
        coluna_selecionada.grid(row=0, column=1, padx=10, pady=10)
        coluna_selecionada.set("nome")  # Define um valor padrão

        # Campo para entrada do valor a buscar
        label_valor = tk.Label(janela_pesquisar_campeonato, text="Digite o valor a buscar:", font=label_font)
        label_valor.grid(row=1, column=0, padx=10, pady=10)

        entry_valor = tk.Entry(janela_pesquisar_campeonato, font=label_font)
        entry_valor.grid(row=1, column=1, padx=10, pady=10)

        # Função para realizar a busca
        def realizar_pesquisa():
            coluna = coluna_selecionada.get()
            valor = entry_valor.get()

            if not coluna or not valor:
                # Verifica se ambos os campos foram preenchidos
                tk.Label(janela_pesquisar_campeonato, text="Por favor, preencha todos os campos.", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)
                return

            try:
                cursor = conexao_banco.cursor()

                # Adiciona curingas para busca parcial
                comando_sql = f"SELECT * FROM campeonatos WHERE {coluna} LIKE %s"
                cursor.execute(comando_sql, (f"%{valor}%",))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados em uma tabela
                tabela = ttk.Treeview(janela_pesquisar_campeonato, columns=colunas, show="headings", height=15)
                tabela.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

                # Configura os cabeçalhos da tabela
                for col in colunas:
                    tabela.heading(col, text=col.capitalize())
                    tabela.column(col, width=100)

                # Insere os resultados na tabela
                for linha in resultados:
                    tabela.insert("", "end", values=linha)

                if not resultados:
                    tk.Label(janela_pesquisar_campeonato, text="Nenhum resultado encontrado.", fg="red", font=label_font).grid(
                        row=5, column=0, columnspan=2, pady=10)

            except Exception as e:
                tk.Label(janela_pesquisar_campeonato, text=f"Erro na busca: {e}", fg="red", font=label_font).grid(
                    row=3, column=0, columnspan=2, pady=10)

        # Botão para realizar a busca
        botao_pesquisar = tk.Button(janela_pesquisar_campeonato, text="Pesquisar", command=realizar_pesquisa, font=label_font, bg="blue", fg="white")
        botao_pesquisar.grid(row=2, column=0, columnspan=2, pady=20)

        # Botão para fechar a janela
        botao_voltar = tk.Button(janela_pesquisar_campeonato, text="Voltar", command=janela_pesquisar_campeonato.destroy, font=label_font)
        botao_voltar.grid(row=5, column=0, columnspan=2, pady=10)

    def pesquisar_gols():
        janela_gols = tk.Toplevel()
        janela_gols.title("Pesquisar Gols")
        janela_gols.geometry("400x200")

        # Label e Entry para o ID do campeonato
        tk.Label(janela_gols, text="Digite o ID do Campeonato:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_id_campeonato = tk.Entry(janela_gols, font=label_font)
        entry_id_campeonato.grid(row=0, column=1, padx=10, pady=10)

        def mostrar_gols():
            id_campeonato = entry_id_campeonato.get()

            if not id_campeonato.isdigit():
                tk.Label(janela_gols, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Consulta SQL para obter os jogadores com mais gols
                cursor = conexao_banco.cursor()
                comando_sql = """
                SELECT j.nome, jc.gols 
                FROM jogador_campeonato jc
                JOIN jogadores j ON jc.id_jogador = j.id
                WHERE jc.id_campeonato = %s
                ORDER BY jc.gols DESC
                """
                cursor.execute(comando_sql, (id_campeonato,))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados
                janela_resultados = tk.Toplevel()
                janela_resultados.title("Jogadores com Mais Gols")
                janela_resultados.geometry("400x300")

                tk.Label(janela_resultados, text="Jogadores com Mais Gols", font=label_font, fg="blue").pack(pady=10)

                for i, (nome, gols) in enumerate(resultados):
                    tk.Label(janela_resultados, text=f"{i+1}. {nome}: {gols} gols", font=label_font).pack(anchor="w")

            except Exception as e:
                tk.Label(janela_gols, text=f"Erro: {e}", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para mostrar os resultados
        tk.Button(janela_gols, text="Pesquisar", command=mostrar_gols, font=label_font, bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=20)

    # Função para mostrar os resultados dos jogadores com mais cartões
    def pesquisar_cartoes_amarelos():
        janela_amarelos = tk.Toplevel()
        janela_amarelos.title("Pesquisar amarelos")
        janela_amarelos.geometry("400x200")

        # Label e Entry para o ID do campeonato
        tk.Label(janela_amarelos, text="Digite o ID do Campeonato:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_id_campeonato = tk.Entry(janela_amarelos, font=label_font)
        entry_id_campeonato.grid(row=0, column=1, padx=10, pady=10)

        def mostrar_amarelos():
            id_campeonato = entry_id_campeonato.get()

            if not id_campeonato.isdigit():
                tk.Label(janela_amarelos, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Consulta SQL para obter os jogadores com mais amarelos
                cursor = conexao_banco.cursor()
                comando_sql = """
                SELECT j.nome, jc.cartoes_amarelos 
                FROM jogador_campeonato jc
                JOIN jogadores j ON jc.id_jogador = j.id
                WHERE jc.id_campeonato = %s
                ORDER BY jc.cartoes_amarelos DESC
                """
                cursor.execute(comando_sql, (id_campeonato,))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados
                janela_resultados = tk.Toplevel()
                janela_resultados.title("Jogadores com Mais amarelos")
                janela_resultados.geometry("400x300")

                tk.Label(janela_resultados, text="Jogadores com Mais amarelos", font=label_font, fg="blue").pack(pady=10)

                for i, (nome, amarelos) in enumerate(resultados):
                    tk.Label(janela_resultados, text=f"{i+1}. {nome}: {amarelos} amarelos", font=label_font).pack(anchor="w")

            except Exception as e:
                tk.Label(janela_amarelos, text=f"Erro: {e}", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para mostrar os resultados
        tk.Button(janela_amarelos, text="Pesquisar", command=mostrar_amarelos, font=label_font, bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=20)

    def pesquisar_cartoes_vermelhos():
        janela_vermelho = tk.Toplevel()
        janela_vermelho.title("Pesquisar vermelho")
        janela_vermelho.geometry("400x200")

        # Label e Entry para o ID do campeonato
        tk.Label(janela_vermelho, text="Digite o ID do Campeonato:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_id_campeonato = tk.Entry(janela_vermelho, font=label_font)
        entry_id_campeonato.grid(row=0, column=1, padx=10, pady=10)

        def mostrar_vermelho():
            id_campeonato = entry_id_campeonato.get()

            if not id_campeonato.isdigit():
                tk.Label(janela_vermelho, text="ID inválido! Digite um número.", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)
                return

            try:
                # Consulta SQL para obter os jogadores com mais vermelho
                cursor = conexao_banco.cursor()
                comando_sql = """
                SELECT j.nome, jc.cartoes_vermelhos
                FROM jogador_campeonato jc
                JOIN jogadores j ON jc.id_jogador = j.id
                WHERE jc.id_campeonato = %s
                ORDER BY jc.cartoes_vermelhos DESC
                """
                cursor.execute(comando_sql, (id_campeonato,))
                resultados = cursor.fetchall()
                cursor.close()

                # Exibe os resultados
                janela_resultados = tk.Toplevel()
                janela_resultados.title("Jogadores com Mais vermelho")
                janela_resultados.geometry("400x300")

                tk.Label(janela_resultados, text="Jogadores com Mais vermelho", font=label_font, fg="blue").pack(pady=10)

                for i, (nome, vermelho) in enumerate(resultados):
                    tk.Label(janela_resultados, text=f"{i+1}. {nome}: {vermelho} vermelho", font=label_font).pack(anchor="w")

            except Exception as e:
                tk.Label(janela_vermelho, text=f"Erro: {e}", fg="red", font=label_font).grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para mostrar os resultados
        tk.Button(janela_vermelho, text="Pesquisar", command=mostrar_vermelho, font=label_font, bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=20)


    # Botões na janela principal


    janela5 = tk.Toplevel()
    janela5.title('Pesquisa')
    janela5.geometry('350x470')
    label_font = ("Bahnschrift SemiCondensed", 18)
    label_nome = tk.Label(janela5)
    label_nome.grid(row=0, column=0)
    janela5.configure(bg="black")
    jogador_pesquisar = tk.Button(janela5, text = 'PESQUISAR JOGADOR',font = label_font ,  command = pesquisar_jogador,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    jogador_pesquisar.grid(row=1, column=2, columnspan=2)
    comissao_pesquisar = tk.Button(janela5, text = 'PESQUISAR COMISSÃO',font = label_font ,  command = pesquisar_comissao,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    comissao_pesquisar.grid(row=2, column=2, columnspan=2)
    campeonato_pesquisar = tk.Button(janela5, text = 'PESQUISAR CAMPEONATO',font = label_font ,  command = pesquisar_campeonato,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    campeonato_pesquisar.grid(row=3, column=2, columnspan=2)
    gols_pesquisar = tk.Button(janela5, text = 'PESQUISAR GOLS',font = label_font ,  command = pesquisar_gols,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    gols_pesquisar.grid(row=4, column=2, columnspan=2)
    cartoes_amarelo_pesquisar = tk.Button(janela5, text = 'PESQUISAR CARTÕES AMARELOS',font = label_font ,  command = pesquisar_cartoes_amarelos,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    cartoes_amarelo_pesquisar.grid(row=5, column=2, columnspan=2)
    cartoes_vermelho_pesquisar =tk.Button(janela5, text= 'PESQUISAR CARTÕES VERMELHOS',font = label_font, command = pesquisar_cartoes_vermelhos,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    cartoes_vermelho_pesquisar.grid(row=6, column=2, columnspan=2)
    botao_voltar = tk.Button(janela5, text='VOLTAR', font = label_font ,command=janela5.destroy,fg="white",bg="black",bd=0,highlightthickness=0,pady=10)
    botao_voltar.grid(row=8, column=2, columnspan=2)


janela = tk.Tk()
janela.title("Gerenciador Times")
janela.geometry('1080x1080')
label_font = ("Bahnschrift SemiCondensed", 21)


imgpath = PhotoImage(file=r"Banco + Python/Imagens/imagem1.png")
bgimg = tk.Label(janela, image=imgpath)
bgimg.pack()


label_nome = tk.Label(janela,bg="black")
label_nome.place(x=0,y=0)
botao_cadastro = tk.Button(janela, text="CADASTRAR", font = label_font , width=15, height=1 ,command=cadastro,fg="white", bg='black',bd=0,highlightthickness=0)
botao_cadastro.pack()
botao_cadastro.place(x=440,y=510)
botao_update = tk.Button(janela,text = 'ALTERAR', font = label_font ,command = update,fg="white", bg='black',bd=0,highlightthickness=0)
botao_update.pack()
botao_update.place(x=400,y=620)
botao_delete = tk.Button(janela,text = 'EXCLUIR',font = label_font , command = excluir,fg="white", bg='black',bd=0,highlightthickness=0)
botao_delete.pack()
botao_delete.place(x=575,y=620)
botao_pesquisar = tk.Button(janela,text = 'PESQUISAR',font = label_font , command = pesquisar,fg="white", bg='black',bd=0,highlightthickness=0)
botao_pesquisar.pack()
botao_pesquisar.place(x=470,y=730)
botao_sair = tk.Button(janela,text = 'SAIR', font = label_font ,command = janela.destroy,fg="white", bg='black',bd=0,highlightthickness=0)
botao_sair.pack()
botao_sair.place(x=500,y=850)

janela.mainloop()