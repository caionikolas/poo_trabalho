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
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo =tipo
        self.cursos = []

    def get_sigla(self):
        return self.__sigla
    
    def get_nome(self):
        return self.__nome
    
    def get_tipo(self):
        return self.__tipo

    def cadastrar_curso(self, curso):
        self.cursos.append(curso)

    def __repr__(self):
        return self.get_nome()

    def __str__(self):
        return f'{self.get_sigla()}, {self.get_nome()}, {self.get_tipo()}, {self.cursos}'



#----------------   Class Curso   ------------------------------
class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id   
        self.__nome = nome 
        self.__duracao = duracao 
        self.__vagas = vagas 
        self.__nota_corte = nota_corte
        self.alunos = []  


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

    def cadastrar_aluno(self):
        pass 

    def __str__(self):
        return f'{self.get_id()}, {self.get_nome()}, {self.get_duracao()}, {self.get_vagas()}, {self.get_nota_corte()}, {self.alunos}'
    
    def __repr__(self):
        return f'{self.get_id()}, {self.get_nome()}, {self.get_duracao()}, {self.get_vagas()}, {self.get_nota_corte()}, {self.alunos}'
    


#----------------   Class Aluno   ------------------------------
class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem):
        self.__cpf = cpf
        self.__nome = nome
        self.__dt_nasc = dt_nasc 
        self.__matricula_uni_publica = False
        self.__matricula_uni_priv = False
        self.__pont_enem = pont_enem

    def get_cpf(self):
        return self.__cpf
    
    def get_nome(self):
        return self.__nome
    
    def get_dt_nasc(self):
        return self.__dt_nasc
    
    def get_matricula_uni_publica(self):
        return self.__matricula_uni_publica

    def get_matricula_uni_priv(self):
        return self.__matricula_uni_priv
    
    def get_pont_enem(self):
        return self.__pont_enem
    

    def solicita_ingresso(self, curso, universidade):
        for i in range(len(universidade.cursos)):
            if universidade.cursos[i].nome == curso.nome:
                if self.pont_enem >= universidade.cursos[i].nota_corte:
                    self.efetiva_matricula(curso, universidade)
                    return True
                else:
                    return False 
                

    def efetiva_matricula(self, curso, universidade):
        for i in range(len(universidade.cursos)):
            if universidade.cursos[i].nome == curso.nome:
                if universidade.cursos[i].vagas == 0:
                    return False
                else:
                    universidade.cursos[i].vagas -= 1
                    return True
        
    def solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
        pass

    def __str__(self):
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

sisu = Sisu()
sisu.incluir_universidade(ifpi.get_nome())
sisu.incluir_universidade(ufpi.get_nome())
sisu.incluir_universidade(uespi.get_nome())



joao = Aluno("123456", "João", "01/01/2000", 500)

print(ifpi)


