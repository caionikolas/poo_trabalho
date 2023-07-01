#----------------   Class Sisu   ------------------------------
class Sisu:
    universidades = []

    def incluir_universidade(self, universidade):
        self.universidades.append(universidade)
    
    def __str__(self):
        return f'{self.universidades}'
    

#----------------   Class Universidade   ------------------------------
class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo =tipo
        self.__cursos = []

    def get_sigla(self):
        return self.__sigla
    
    def get_nome(self):
        return self.__nome
    
    def get_tipo(self):
        return self.__tipo

    def cadastrar_curso(self, curso):
        self.__cursos.append(curso)

    def get_cursos(self):
        return self.__cursos

    def __repr__(self):
        return self.get_nome()

    def __str__(self):
        return f'{self.get_sigla()}, {self.get_nome()}, {self.get_tipo()}, {self.get_cursos()}'

#----------------   Class Curso   ------------------------------
class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id   
        self.__nome = nome 
        self.__duracao = duracao 
        self.__vagas = vagas 
        self.__nota_corte = nota_corte
        self.__alunos = []  


    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_duracao(self):
        return self.__duracao
    
    def set_duracao(self, valor):
        self.__duracao = valor 
    
    def get_vagas(self):
        return self.__vagas
    
    def set_vagas(self, valor):
        self.__vagas = valor

    def get_nota_corte(self):
        return self.__nota_corte
    
    def set_nota_corte(self, valor):
        self.__nota_corte = valor

    def get_alunos(self):
        return self.__alunos
    
    def set_alunos(self, aluno):
        for i in range(len(self.alunos)):
            if self.alunos[i].get_cpf() == aluno.get_cpf():
                del self.alunos[i]

    def cadastrar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def __str__(self):
        return f'{self.get_id()}, {self.get_nome()}, {self.get_duracao()}, {self.get_vagas()}, {self.get_nota_corte()}, {self.get_alunos()}'
    
    def __repr__(self):
        return f'{self.get_id()}, {self.get_nome()}, {self.get_duracao()}, {self.get_vagas()}, {self.get_nota_corte()}, {self.get_alunos()}'
    
#----------------   Class Aluno   ------------------------------
class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem, matricula_uni_publica = False, matricula_uni_priv = False):
        self.__cpf = cpf
        self.__nome = nome
        self.__dt_nasc = dt_nasc 
        self.__matricula_uni_publica = matricula_uni_publica
        self.__matricula_uni_priv = matricula_uni_priv
        self.__pont_enem = pont_enem

    def get_cpf(self):
        return self.__cpf
    
    def get_nome(self):
        return self.__nome
    
    def get_dt_nasc(self):
        return self.__dt_nasc
    
    def get_matricula_uni_publica(self):
        return self.__matricula_uni_publica
    
    def set_matricula_uni_publica(self, valor = True):
        self.__matricula_uni_publica = valor

    def get_matricula_uni_priv(self):
        return self.__matricula_uni_priv 
    
    def set_matricula_uni_priv(self, valor = True):
        self.__matricula_uni_publica = valor
    
    def get_pont_enem(self):
        return self.__pont_enem
    

    def solicita_ingresso(self, curso, universidade):
        for i in range(len(universidade.get_cursos())):
            if universidade.get_cursos()[i].get_nome() == curso.get_nome():
                if self.get_pont_enem() >= universidade.get_cursos()[i].get_nota_corte():
                    return True
                else:
                    return False 
                
    def efetiva_matricula(self, curso, universidade):
        if self.solicita_ingresso(curso, universidade) == True:
            for i in range(len(universidade.get_cursos())):
                if universidade.get_cursos()[i].get_nome() == curso.get_nome():
                    if universidade.get_cursos()[i].get_vagas() == 0:
                        return False
                    else:
                        valor = universidade.get_cursos()[i].get_vagas() - 1
                        universidade.get_cursos()[i].set_vagas(valor)

                        if universidade.get_tipo() == 'publica':
                            self.set_matricula_uni_publica()
                        else:
                            self.set_matricula_uni_priv()

                        universidade.get_cursos()[i].cadastrar_aluno(joao)
                        print("ok")
                        return True
        
    def solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
        for i in range(len(univ_origem.cursos)):
            if univ_origem.get_cursos()[i].get_nome() == curso_origem:
                valor = univ_destino.get_cursos()[i].get_vagas() - 1
                univ_destino.get_cursos()[i].set_vagas(valor)

                if univ_destino.get_tipo() == 'publica':
                    self.set_matricula_uni_publica()
                else:
                    self.set_matricula_uni_priv()

                univ_destino.get_cursos()[i].cadastrar_aluno(joao)
       
    def __str__(self):
        return f'{self.get_cpf()}, {self.get_nome()}, {self.get_dt_nasc()}, {self.get_matricula_uni_publica()}, {self.get_matricula_uni_priv()}, {self.get_pont_enem()}'
    
    def __repr__(self):
        return f'{self.get_cpf()}, {self.get_nome()}, {self.get_dt_nasc()}, {self.get_matricula_uni_publica()}, {self.get_matricula_uni_priv()}, {self.get_pont_enem()}'


TDS = Curso(266, "Técnico Desenvolvimento de Sistemas", "1,5 anos", 40, 600)
Administração = Curso(123, "Administração", "2 anos", 40, 500)
Biologia = Curso(266, "Biologia", "1,5 anos", 40, 400)



ifpi = Universidade("IFPI", "Instituto federal do Piaui", "Pública")
ufpi = Universidade("UFPI", "Universidade federal do Piaui", "Pública")
uespi = Universidade("UESPI", "Universidade Estadual do Piaui", "Pública")



ifpi.cadastrar_curso(TDS)
ifpi.cadastrar_curso(Administração)
ifpi.cadastrar_curso(Biologia)

uespi.cadastrar_curso(TDS)
uespi.cadastrar_curso(Administração)
uespi.cadastrar_curso(Biologia)

sisu = Sisu()
sisu.incluir_universidade(ifpi.get_nome())
sisu.incluir_universidade(ufpi.get_nome())
sisu.incluir_universidade(uespi.get_nome())



joao = Aluno("123456", "João", "01/01/2000", 500)


print(joao.efetiva_matricula(Biologia, ifpi))

#print(ifpi.cursos[2].get_nome())

#print(joao.solicita_transferencia(ifpi, 'Biologia', uespi))

#print(ifpi.cursos[2].get_alunos())
#print(Biologia.alunos)

