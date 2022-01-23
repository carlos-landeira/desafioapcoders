from enum import unique
from config import *
from sqlalchemy import String, Integer, Float, Boolean, Column

#Classe Inquilinos
class Inquilinos(db.Model):
    id_inquilino = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(55), nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(55))
    telefone = db.Column(db.String(55), unique=True, nullable=False)
    email = db.Column(db.String(55), unique=True, nullable=False)

#Classe Unidades
class Unidades(db.Model):
    id_unidade = db.Column(db.Integer, primary_key=True)
    proprietario = db.Column(db.String(55))
    condominio = db.Column(db.String(55))
    endereco = db.Column(db.String(55))


#Classe despesas das unidades
class Despesas(db.Model):
    id_despesa = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(55))
    tipo_despesa = db.Column(db.String(55))
    valor = db.Column(db.Float(55))
    vencimento_fatura = db.Column(db.String(55))
    status_pagamento= db.Column(db.String(55))

    unidade_despesa = db.Column(db.Integer, db.ForeignKey(Unidades.id_unidade), nullable= False)
    unidade = db.relationship("Unidades", foreign_keys =  unidade_despesa)


#Execução do programa
if __name__ == "__main__":  
     
    #Cria as tabelas
    db.create_all()

    menu=9
    while menu!=0:
        print("Bem-vindo(a) ao sistema de gerenciamento de inquilinos e unidades! Qual menu você gostaria de acessar?")
        print("1 - Inquilinos")
        print("2 - Unidades")
        print("3 - Despesas das unidades")
        print("0 - Sair do programa")
        menu = int(input("> "))
        print("")

        if menu == 1:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar inquilinos")
            print("2 - Visualizar inquilinos cadastrados")
            menu2 = int(input("> "))
            print("")

            if menu2 == 1:
                def cadastrar_inquilino():
                    name = str(input("Digite o nome do inquilino: "))
                    age = int(input("Digite a idade do inquilino: "))
                    sex = str(input("Digite o sexo do inquilino: "))
                    phone = str(input("Digite o telefone do inquilino: "))
                    mail = str(input("Digite o email do inquilino: "))
                    print("")

                    inquilino = Inquilinos(nome=name, idade=age, sexo=sex, telefone=phone, email=mail)
                    db.session.add(inquilino)
                    db.session.commit()
                    print("Inquilino cadastrado com sucesso!")
                    print("")
                    
                cadastrar_inquilino()
            
            elif menu2 == 2:
                def listar_inquilinos():
                    inquilino = db.session.query(Inquilinos)
                    print("Listando todos os inquilinos cadastrados:")
                    print("")
                    for inquilinos in inquilino:
                        print("Nome:",inquilinos.nome, "||Idade:",inquilinos.idade, "||Sexo:",inquilinos.sexo, "||Telefone",inquilinos.telefone, "||Email:",inquilinos.email)
                        print("")

                listar_inquilinos()

            else:
                print("Selecione uma operação válida.")


        elif menu == 2:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar unidades")
            print("2 - Visualizar unidades cadastradas")
            menu2 = int(input("> "))
            print("")

            if menu2 == 1:
                def cadastrar_unidade():
                    owner = str(input("Digite o nome do proprietário da unidade: "))
                    condominium = str(input("Digite o condomínio da unidade: "))
                    adress = str(input("Digite o endereço da unidade: "))
                    print("")

                    unidade = Unidades(proprietario=owner, condominio=condominium, endereco=adress)
                    db.session.add(unidade)
                    db.session.commit()
                    print("Unidade cadastrada com sucesso!")
                    print("")

                cadastrar_unidade()

            elif menu2 == 2:
                def listar_unidades():
                    unidade = db.session.query(Unidades)
                    print("Listando todas as unidades:")
                    print("")
                    for unidades in unidade:
                        print("Identificação:",unidades.id_unidade, "||Proprietário:",unidades.proprietario, "||Condomínio:",unidades.condominio, "||Endereço:",unidades.endereco)
                        print("")

                listar_unidades()
            
            else:
                print("Selecione uma operação válida.")
            

        elif menu == 3:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar despesas")
            print("2 - Editar despesas")
            print("3 - Visualizar despesas cadastradas")
            menu2 = int(input("> "))
            print("")

            if menu2 == 1:
                def cadastrar_despesa():
                    desc = str(input("Digite a descrição da despesa: "))
                    tipo = str(input("Digite o tipo da despesa: "))
                    v = float(input("Digite o valor da despesa: "))
                    vencimento = str(input("Digite a data de vencimento da fatura (DD-MM-YYYY): "))
                    status = str(input("Digite o status de pagamento da despesa: "))
                    unit = int(input("Digite a unidade da qual pertence a despesa: "))
                    print("")

                    despesa = Despesas(descricao=desc, tipo_despesa=tipo, valor=v, vencimento_fatura=vencimento, status_pagamento=status, unidade_despesa=unit)
                    db.session.add(despesa)
                    db.session.commit()
                    print("Despesa cadastrada com sucesso!")
                    print("")

                cadastrar_despesa()

            elif menu2 == 2:
                def editar_despesa():
                    print("Qual das seguintes despesas você gostaria de editar? (Selecione pelo ID)")
                    despesa = db.session.query(Despesas)
                    for despesas in despesa:
                        print("ID:",despesas.id_despesa, "||Descrição:",despesas.descricao, "||Tipo da despesa:",despesas.tipo_despesa, "||Valor: R$",despesas.valor, "||Data de vencimento da fatura:",despesas.vencimento_fatura, "||Status de pagamento:",despesas.status_pagamento, "||Unidade:",despesas.unidade_despesa)
                        print("")
                    x = int(input("> "))
                    print("")
                    atualizar = Despesas.query.filter_by(id_despesa=x).first()

                    print("Receita",x,"selecionada, qual informação você gostaria de editar?")
                    print("1 - Descrição")
                    print("2 - Tipo da despesa")
                    print("3 - Valor")
                    print("4 - Vencimento da fatura")
                    print("5 - Status de pagamento")
                    y = int(input("> "))
                    print("")

                    if y == 1:
                        z = str(input("Digite a nova descrição da despesa: "))
                        atualizar.descricao = z
                        db.session.commit()
                        print("Descrição da despesa atualizada com sucesso!")

                    elif y == 2:
                        z = str(input("Digite o novo tipo da despesa: "))
                        atualizar.tipo_despesa = z
                        db.session.commit()
                        print("Tipo da despesa atualizado com sucesso!")

                    elif y == 3:
                        z = float(input("Digite o novo valor da despesa: "))
                        atualizar.valor = z
                        db.session.commit()
                        print("Valor da despesa atualizado com sucesso!")

                    elif y == 4:
                        z = str(input("Digite a nova data de vencimento da fatura: "))
                        atualizar.vencimento_fatura = z
                        db.session.commit()
                        print("Data de vencimento da fatura atualizada com sucesso!")

                    elif y == 5:
                        z = str(input("Digite o novo status de pagamento da despesa: "))
                        atualizar.status_pagamento = z
                        db.session.commit()
                        print("Status de pagamento da despesa atualizado com sucesso!")

                    else:
                        print("Selecione uma operação válida.")

                editar_despesa()
                     
            elif menu2 == 3:
                def listar_despesas():
                    print("Como gostaria de visualizar as despesas?")
                    print("1 - Visualizar todas")
                    print("2 - Filtrar por unidade")
                    x = int(input("> "))
                    print("")

                    if x == 1:
                        despesa = db.session.query(Despesas)
                        for despesas in despesa:
                            print("ID:",despesas.id_despesa, "||Descrição:",despesas.descricao, "||Tipo da despesa:",despesas.tipo_despesa, "||Valor: R$",despesas.valor, "||Data de vencimento da fatura:",despesas.vencimento_fatura, "||Status de pagamento:",despesas.status_pagamento, "||Unidade:",despesas.unidade_despesa)
                            print("")
                    
                    elif x == 2:
                        print("De qual unidade você gostaria de visualizar as despesas?")
                        y = int(input("> "))
                        print("")

                        despesa = db.session.query(Despesas).filter(Despesas.unidade_despesa==y)
                        for despesas in despesa:
                            print("ID:",despesas.id_despesa, "||Descrição:",despesas.descricao, "||Tipo da despesa:",despesas.tipo_despesa, "||Valor: R$",despesas.valor, "||Data de vencimento da fatura:",despesas.vencimento_fatura, "||Status de pagamento:",despesas.status_pagamento, "||Unidade:",despesas.unidade_despesa)
                            print("")

                    else:
                        print("Selecione uma operação válida.")
                
                listar_despesas()

            else:
                print("Selecione uma operação válida.")