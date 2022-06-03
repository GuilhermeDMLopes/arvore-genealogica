from helper.write_a_json import write_a_json
from pprintpp import pprint as pp
from db.database import Graph


class Pessoas(object):
    def __init__(self):
        self.db = Graph(uri='bolt://18.208.195.238:7687',
                        user='neo4j', password='countermeasures-cannon-chests')
    '''
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
            "(p:Person{name:'Guilherme'}),(p0:Person{name:'Giulia'}),"
            "(p:Person{name:'Guilherme'}),(p6:Person{name:'Sophia'}),"
            "(p0:Person{name:'Giulia'}),(p6:Person{name:'Sophia'}),"
            "(p:Person{name:'Guilherme'}),(p1:Person{name:'Thiago'}),"
            "(p2:Person{name:'Bel'}),(p:Person{name:'Guilherme'}),"
            "(p2:Person{name:'Bel'}),(p1:Person{name:'Thiago'}),"
            "(p2:Person{name:'Bel'}),(p7:Person{name:'Helio'}),"
            "(p3:Person{name:'Dinarte'}),(p:Person{name:'Guilherme'}),"
            "(p3:Person{name:'Dinarte'}),(p1:Person{name:'Thiago'}),"
            "(p2:Person{name:'Bel'}),(p8:Person{name:'Keth'}),"
            "(p8:Person{name:'Keth'}),(p9:Person{name:'Juju'}),"
            "(p4:Person{name:'Wilma'}),(p2:Person{name:'Bel'}),"
            "(p4:Person{name:'Wilma'}),(p8:Person{name:'Keth'}),"
            "(p4:Person{name:'Wilma'}),(p5:Person{name:'Mauro'}),"
            "(p5:Person{name:'Mauro'}),(p8:Person{name:'Keth'}),"
            "(p5:Person{name:'Mauro'}),(p2:Person{name:'Bel'})"
            "CREATE"
            "(p)-[:CASADO_COM{desde:2017}]->(p0),"
            "(p)-[:PAIS_DE]->(p6),"
            "(p0)-[:PAIS_DE]->(p6),"
            "(p)-[:IRMAO_DE]->(p1),"
            "(p2)-[:PAIS_DE]->(p),"
            "(p2)-[:PAIS_DE]->(p1),"
            "(p2)-[:CASADO_COM{desde:2018}]->(p7),"
            "(p3)-[:PAIS_DE]->(p),"
            "(p3)-[:PAIS_DE]->(p1),"
            "(p2)-[:IRMAO_DE]->(p8),"
            "(p8)-[:PAIS_DE]->(p9),"
            "(p4)-[:PAIS_DE]->(p2),"
            "(p4)-[:PAIS_DE]->(p8),"
            "(p4)-[:CASADO_COM{desde:1971}]->(p5),"
            "(p5)-[:PAIS_DE]->(p8),"
            "(p5)-[:PAIS_DE]->(p2)"
        )
    '''
    def pergunta1(self):
        data = self.db.execute_query(
            "MATCH"
            " r=()-[p:CASADO_COM]->() WHERE p.desde = 2017 "
            "RETURN r;"
        )
        write_a_json(data,"Pergunta 1")
        return data

    def pergunta2(self):
        data =  self.db.execute_query(
            "MATCH"
            " (p:Person:Desenvolvedor) "
            "RETURN p;"
        )
        write_a_json(data,"Pergunta 2")
        return data

    def pergunta3(self):
        data = self.db.execute_query(
            "MATCH"
            " (p:Person)-[:IRMAO_DE]->(p1:Person{name:'Thiago'}) "
            "RETURN p;"
        )
        write_a_json(data,"Pergunta 3")
        return data

    def delete(self):
        self.db.execute_query("MATCH(n) DETACH DELETE n;")

def divider():
    print('\n' + '-' * 80 + '\n')

p = Pessoas()
#p.delete()
#p.createArvoreGenealogicaNaruto()
#p.createRelacionamento()

while 1:    
    option = input('Escolha uma pergunta!\n1. Quem esta casado desde 2017?\n2. Quem da familia é dev?\n3. Quem é o irmao de Thiago?\n4. sair\n\n')

    if option == '1':        
        pp(p.pergunta1())
        divider()

    elif option == '2':        
        pp(p.pergunta2())
        divider()

    elif option == '3':
        
        pp(p.pergunta3())
        divider()

    elif option == '4':        
        p.delete()
        divider()
        break

    else:
        print("Opção Inválida!")

p.db.close()
