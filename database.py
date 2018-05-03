import sqlite3
#Criando o banco
connection = sqlite3.connect('en-words.db')
#Criando variável referente ao banco
db = connection.cursor()

#Esse método cria uma tabela
def createTable():
    sql = "CREATE TABLE IF NOT EXISTS palavras ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, palavra text, traducao text, exemplo text )"
    #Cria a tabela no banco
    db.execute(sql)

def wordExists(palavra):
    sqlSelectOne = "SELECT * FROM palavras WHERE palavra = ?"
    
    #for rodando a cada linha do banco de dados
    for row in db.execute(sqlSelectOne, (palavra.upper(),)):
        return row

#Esse método insere os dados no banco
def insert():
    palavra = str(input("Palavra: "))

    response = wordExists(palavra)
    #Verifica se algum resultado foi retornado
    #Senão, avisa ao usuário que a palavra não existe no DataBase
    if (response):
        print("********************\n\nPALAVRA JÁ EXISTENTE\n\nPalavra: {} \nTradução: {} \nExemplo: {} \n".format(response[1], response[2], response[3])) 
    else:
        sqlInsert = "INSERT INTO palavras (palavra, traducao, exemplo) VALUES(?,?,?)"

        traducao = str(input("Tradução: "))
        exemplo = str(input("Exemplo: "))
        print("\nInserindo {} na tabela\n".format(palavra.upper()))   

        #Adicionando os dados no banco
        db.execute(sqlInsert, (palavra.upper(), traducao.upper(), exemplo.upper()))
        connection.commit()

#Esse método busca todas as palavras e imprime na tela
def getWords():
    sqlSelect = "SELECT * FROM palavras"
    print("*********************\nBuscando todas as palavras...\n")
    #for rodando a cada linha do banco de dados
    for row in db.execute(sqlSelect):
        print("********************\nPalavra: {} \nTradução: {} \nExemplo: {} \n".format(row[1], row[2], row[3]))

#Esse método busca a palavra informada imprime na tela
def findOne():
    palavra = str(input("Palavra: "))
    response = wordExists(palavra)
    #Verifica se algum resultado foi retornado
    #Senão, avisa ao usuário que a palavra não existe no DataBase
    if (response):
        print("********************\nPalavra: {} \nTradução: {} \nExemplo: {} \n".format(response[1], response[2], response[3])) 
    else:
        print("********************\nPalavra não cadastrada\n")
        
def menuUpdate(id):
    loop = 0
    while(loop == 0):
        print("*********************\nO que deseja alterar?\n[1] - Palavra\n[2] - Tradução\n[3] - Exemplo\n[0] - Sair\n")
        opcao = int(input(" --> "))
        if (opcao == 1):
            palavra = str(input("Nova palavra: "))
            db.execute("UPDATE palavras SET palavra = ? WHERE id = ?", (palavra.upper(), id,))
            print("\nPalavra alterada com sucesso!\n")
        elif (opcao == 2):
            traducao = str(input("Nova tradução: "))
            db.execute("UPDATE palavras SET traducao = ? WHERE id = ?", (traducao.upper(), id,))
            print("\nTradução alterada com sucesso!\n")
        elif (opcao == 3):
            exemplo = str(input("Novo exemplo: "))
            db.execute("UPDATE palavras SET exemplo = ? WHERE id = ?", (exemplo.upper(), id,))
            print("\nExemplo alterado com sucesso!\n")
        elif (opcao == 0):
            loop = 1
        else:
            print("OPÇÃO INVÁLIDA, ESCOLHE OUTRA!")
        
        connection.commit()

#Esse método busca uma palavra e altera
def update():
    palavra = str(input("Palavra: "))
    response = wordExists(palavra)
    #Verifica se algum resultado foi retornado
    #Senão, avisa ao usuário que a palavra não existe no DataBase
    if (response):
        menuUpdate(response[0])
    else:
        print("********************\nPalavra não cadastrada\n")

#Esse método busca uma palavra e deleta
def delete():
    palavra = str(input("Palavra: "))
    response = wordExists(palavra)
    #Verifica se algum resultado foi retornado
    #Senão, avisa ao usuário que a palavra não existe no DataBase
    if (response):
        print("PALAVRA ENCONTRADA\n")
        opcao = str(input("Tem certeza que deseja deletar? (S/N)\n --> "))
        #Caso o usuário tenha digitado S, deleta a palavra encontrada
        if (opcao.upper() == "S"):
            print("\nPalavra {} deletada com sucesso!\n".format(response[1]))
            db.execute("DELETE FROM palavras WHERE id = ?", (response[0],))
    else:
        print("********************\nPalavra não cadastrada\n")

def main():
    loop = 0
    while(loop == 0):
        print("*********************\n\n  ESCOLHA UMA OPÇÃO\n\n*********************\n[1] - Inserir nova palavra\n[2] - Listar palavras\n[3] - Buscar palavra\n[4] - Alterar palavra\n[5] - Deletar palavra\n[0] - Sair\n")
        opcao = int(input(" --> "))
        if (opcao == 1):
            insert()
        elif (opcao == 2):
            getWords()
        elif (opcao == 3):
            findOne()
        elif (opcao == 4):
            update()
        elif (opcao == 5):
            delete()
        elif (opcao == 0):
            print("********************\nSaindo. Obrigado por me usar\nBy: Parzival.AD")
            loop = 1
        else:
            print("\nOPÇÃO INVÁLIDA, ESCOLHE OUTRA!\n")


#Apenas deixe esse método na primeira vez que executar
createTable() 
#Rodando a aplicação com a chamada do main
main()

