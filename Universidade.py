#----------------   Class Sisu   ------------------------------
class Sisu:
    def __init__(self):
        self.universidade = []

    def incluir_universidade(self, universidade):
        self.universidade.append(universidade)
    
    def __str__(self):
        return f'{self.universidade}'



#----------------   Class Universidade   ------------------------------
class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.sigla = sigla
        self.nome = nome
        self.tipo =tipo
        self.cursos = []

    def cadastrar_curso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        return f'{self.sigla}, {self.nome}, {self.tipo}, {self.cursos}'



#----------------   Class Curso   ------------------------------
class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.id = id   
        self.nome = nome 
        self.duracao = duracao 
        self.vagas = vagas 
        self.nota_corte = nota_corte
        self.alunos = []
    
    def cadastrar_aluno(self):
        pass

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.duracao}, {self.vagas}, {self.nota_corte}, {self.alunos}'
    


#----------------   Class Aluno   ------------------------------
class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem):
        self.cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.matricula_uni_publica = False
        self.matricula_uni_priv = False
        self.pont_enem = pont_enem

    def solicita_ingresso(self, curso, universidade):
        print(universidade.cursos)
        for i in range(universidade.cursos):
            if i == curso:
                return i
        
        return None

    def efetiva_matricula(self, curso, universidade):
        pass

    def solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
        pass

    def __str__(self):
        return f'{self.cpf}, {self.nome}, {self.dt_nasc}, {self.matricula_uni_publica}, {self.matricula_uni_priv}, {self.pont_enem}'




TDS = Curso(266, "Técnico Desenvolvimento de Sistemas", "1,5 anos", 40, 600)
Administração = Curso(123, "Administração", "2 anos", 40, 500)
Biologia = Curso(266, "Biologia", "1,5 anos", 40, 400)


ifpi = Universidade("IFPI", "Instituto federal do Piaui", "Pública")
ufpi = Universidade("UFPI", "Universidade federal do Piaui", "Pública")
uespi = Universidade("UESPI", "Universidade Estadual do Piaui", "Pública")



ifpi.cadastrar_curso(TDS)
ifpi.cadastrar_curso(Administração)
ifpi.cadastrar_curso(Biologia)

print(ifpi.cursos)

sisu = Sisu()
sisu.incluir_universidade(ifpi.nome)
sisu.incluir_universidade(ufpi.nome)
sisu.incluir_universidade(uespi.nome)



joao = Aluno("123456", "João", "01/01/2000", 500)
#print(TDS.nota_corte)
#print(joao.solicita_ingresso(TDS, ifpi))


