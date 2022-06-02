from helper.write_a_json import write_a_json
from pprintpp import pprint as pp
from db.database import Graph


class Pessoas(object):
    def __init__(self):
        self.db = Graph(uri='bolt://34.239.104.135:7687',
                        user='neo4j', password='countermeasures-cannon-chests')

    def createArvoreGenealogicaPessoas(self):
        self.db.execute_query(
            "CREATE"
            "(p:Person:Desenvolvedor {name:'Guilherme',genre:'M', age:26}),"
            "(p0:Person:Execuiva {name:'Giulia',genre:'F', age:23}),"
            "(p1:Person:Estudante {name:'Thiago',genre:'M', age:23}),"
            "(p2:Person:Empreendedora {name:'Bel',genre:'F', age:49}),"
            "(p3:Person:Jornalista {name:'Dinarte',genre:'M', age:58}),"
            "(p4:Person:DonaCasa {name:'Wilma',genre:'F', age:65}),"
            "(p5:Person:Mecanico {name:'Mauro',genre:'M', age:64}),"
            "(p6:Person:Estudante {name:'Sophia',genre:'F', age:7}),"
            "(p7:Person:Medico {name:'Helio',genre:'M', age:55}),"
            "(p8:Person:Engenheira {name:'Keth',genre:'F', age:46}),"
            "(p9:Person:Estudante {name:'Juju',genre:'F', age:11})"            
            )

    def createRelacionamento(self):
        self.db.execute_query(
            "MATCH"
            "(k:Alien:ProjenitoraDoChakra{nome:'Kaguya Otsutsuki'}),"
            "(h1:Alien:SabioDosSeisCaminhos{nome:'Hagoromo Otsutsuki'}),"
            "(h2:Alien:AncestralClanHyuga{nome:'Hamura Otsutsuki'}),"
            "(i:Ninja:AncestralClanUchiha{nome:'Indra Otsutsuki'}),"
            "(a:Ninja:AncestralClanSenju{nome:'Ashura Otsutsuki'}),"
            "(s1:Ninja:Medica{nome:'Sakura Haruno'}),"
            "(s2:Ninja:HokageDasSombras{nome:'Sasuke Uchiha'}),"
            "(s3:Ninja:Kunoichi{nome:'Sarada Uchiha'}),"
            "(h3:Ninja:PrincesaDoByakugan{nome:'Hinata Hyuga'}),"
            "(n:Ninja:Hokage{nome:'Naruto Uzumaki'}),"
            "(h4:Ninja:Kunoichi{nome:'Himawari Uzumaki'}),"
            "(b:Ninja:Shinobi{nome:'Boruto Uzumaki'})"
            "CREATE"
            "(k)-[:MAE_DE]->(h1),(k)-[:MAE_DE]->(h2),"
            "(h1)-[:PAI_DE]->(i),(h1)-[:PAI_DE]->(a),"
            "(s1)-[:MAE_DE]->(s3),(s2)-[:PAI_DE]->(s3),"
            "(h3)-[:MAE_DE]->(h4),(h3)-[:MAE_DE]->(b),(n)-[:PAI_DE]->(h4),(n)-[:PAI_DE]->(b),"
            "(s1)-[:CASADA_COM]->(s2),(h3)-[:CASADA_COM]->(n),"
            "(h1)-[:IRMAO_DE{tipo:'Gemeo'}]->(h2),(i)-[:IRMAO_DE]->(a),(h4)-[:IRMA_DE]->(b),"
            "(n)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s2),(n)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s1),(s2)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s1),"
            "(s3)-[:AMIGA_DE]->(b),"
            "(n)-[:DESCENDENTE_DE]->(a),(s2)-[:DESCENDENTE_DE]->(i),(h3)-[:DESCENDENTE_DE]->(h2)"
        )

    def pergunta1(self):
        return self.db.execute_query(
            "MATCH"
            "(n:Alien)"
            "RETURN n.nome"
        )

    def pergunta2(self):
        return self.db.execute_query(
            "MATCH"
            "(:Ninja:HokageDasSombras{nome:'Sasuke Uchiha'})-[:DESCENDENTE_DE]->(n)"
            "RETURN n.nome"
        )

    def pergunta3(self):
        return self.db.execute_query(
            "MATCH"
            "(:Ninja:Hokage{nome:'Naruto Uzumaki'})-[:PAI_DE]->(n)"
            "RETURN n.nome"
        )

    def delete(self):
        self.db.execute_query("MATCH(n) DETACH DELETE n;")

def divider():
    print('\n' + '-' * 80 + '\n')

p = Pessoas()
p.delete()
p.createArvoreGenealogicaNaruto()
p.createRelacionamento()

while 1:    
    option = input('Escolha uma pergunta!\n1. Quem esta casado desde 2017?\n2. Quem da familia é dev?\n3. Quem é o irmao de Thiago?\n4. sair\n\n')

    if option == '1':
        write_a_json(p.pergunta1(), "Perguta 1")
        pp(p.pergunta1())
        divider()

    elif option == '2':
        write_a_json(p.pergunta2(), "Perguta 2")
        pp(p.pergunta2())
        divider()

    elif option == '3':
        write_a_json(p.pergunta3(), "Perguta 3")
        pp(p.pergunta3())
        divider()

    elif option == '4':        
        p.delete()
        divider()
        break

    else:
        print("Opção Inválida!")

p.db.close()
