import pytest
from enum import Enum
from abc import ABCMeta,abstractmethod

class GradoNoEncontrado(BaseException):
    pass

class DepartamentoNoEncontrado(BaseException):
    pass

class DNINoEncontrado(BaseException):
    pass

class Area_InvestigacionNoValida(BaseException):
    pass

class AsignaturaNoValida(BaseException):
    pass

class SexoNoValido(BaseException):
    pass

class NombreNoValido(BaseException):
    pass

class DireccionNoValida(BaseException):
    pass

class DepartamentoNoValido(BaseException):
    pass

class Miembro_departamentoNoValido(BaseException):
    pass

class EstudianteNoValido(BaseException):
    pass

class NoLista(BaseException):
    pass


#Creamos la clase Sexo como una enumeración

class Sexo(Enum):
    MASCULINO=0
    FEMENINO=1
    OTRO=2

#Creamos la clase Grados, con los grados disponibles en la universidad 
#(esta enumeración se podría ampliar. En este caso añadimos 10 grados para comprobar el correcto funcionamiento del programa). 

class Grados(Enum):
    ADE = 1
    DERECHO = 2
    PSICOLOGIA = 3
    INGENIERIA_INDUSTRIAL = 4
    MEDICINA = 5
    EDUCACION_PRIMARIA = 6
    ARQUITECTURA = 7
    BIOLOGIA = 8
    CAFD = 9
    ENFERMERIA = 10

#A continuación creamos enumeraciones con las asignaturas correspondientes a cada grado
#(Al igual que con los grados estas enumeraciones se podrían ampliar añadiendo todas las asignaturas de cada grado.
#Pero con 10 asignaturas por grado nos sobra para comprobar el correcto funcionamiento del programa).

class Asignaturas_ADE(Enum):
    CONTABILIDAD_FINANCIERA = 1
    FINANZAS = 2
    MARKETING = 3
    DIRECCION_ESTRATEGICA = 4
    DERECHO_EMPRESARIAL = 5
    RECURSOS_HUMANOS = 6
    ECONOMIA = 7
    OPERACIONES_Y_LOGISTICA = 8
    SISTEMAS_DE_INFORMACION = 9
    ETICA_EMPRESARIAL = 10

class Asignaturas_Derecho(Enum):
    DERECHO_CONSTITUCIONAL = 1
    DERECHO_PENAL = 2
    DERECHO_CIVIL = 3
    DERECHO_MERCANTIL = 4
    DERECHO_TRABAJO_SEGURIDAD_SOCIAL = 5
    DERECHO_INTERNACIONAL = 6
    DERECHO_FISCAL = 7
    DERECHO_AMBIENTAL = 8
    DERECHO_ADMINISTRATIVO = 9
    DERECHO_DE_LA_UNION_EUROPEA = 10

class Asignaturas_Psicologia(Enum):
    PSICOLOGIA_CLINICA_SALUD = 1
    PSICOLOGIA_EDUCACION = 2
    PSICOLOGIA_TRABAJO_ORGANIZACIONES = 3
    PSICOLOGIA_INTERVENCION_SOCIAL = 4
    PSICOLOGIA_ACTIVIDAD_FISICA_DEPORTE = 5
    EVALUACION_PSICOLOGICA = 6
    PSICOLOGIA_EVOLUTIVA = 7
    TERAPIA_COGNITIVO_CONDUCTUAL = 8
    PSICOLOGIA_COMUNITARIA = 9
    PSICOLOGIA_DE_LOS_GRUPOS = 10

class Asignaturas_IngIndus(Enum):
    GESTION_PRODUCCION = 1
    DISENO_SISTEMAS_PRODUCCION = 2
    LOGISTICA_INDUSTRIAL = 3
    AUTOMATIZACION_INDUSTRIAL = 4
    SISTEMAS_CALIDAD = 5
    INGENIERIA_ELECTRICA = 6
    INGENIERIA_MECANICA = 7
    INGENIERIA_DE_MATERIALES = 8
    INGENIERIA_TERMICA = 9
    INGENIERIA_DE_PROCESOS = 10

class Asignaturas_Medicina(Enum):
    ANATOMIA_HUMANA = 1
    BIOQUIMICA_BIOLOGIA_MOLECULAR = 2
    FISIOLOGIA_HUMANA = 3
    PATOLOGIA_GENERAL = 4
    MEDICINA_PREVENTIVA_SALUD_PUBLICA = 5
    SEMIOLOGIA_MEDICA = 6
    CIRUGIA_GENERAL = 7
    PEDIATRIA = 8
    GINECOLOGIA_OBSTETRICIA = 9
    MEDICINA_INTERNA = 10

class Asignaturas_EducacionPrim(Enum):
    DIDACTICA_GENERAL = 1
    PSICOLOGIA_DESARROLLO_EDUCACION = 2
    DIDACTICA_CIENCIAS_EXPERIMENTALES = 3
    DIDACTICA_CIENCIAS_SOCIALES = 4
    DIDACTICA_LENGUA_CASTELLANA = 5
    MATEMATICAS_PARA_EDUCADORES = 6
    LITERATURA_INFANTIL = 7
    EDUCACION_MUSICAL = 8
    EDUCACION_PLASTICA_VISUAL = 9
    EDUCACION_FISICA = 10

class Asignaturas_Arquitectura(Enum):
    DIBUJO_ARQUITECTURA = 1
    GEOMETRIA_DESCRIPTIVA = 2
    MATEMATICAS_ARQUITECTURA = 3
    HISTORIA_ARTE = 4
    PROYECTOS_ARQUITECTURA = 5
    URBANISMO = 6
    ESTRUCTURAS_ARQUITECTONICAS = 7
    CONSTRUCCION = 8
    INSTALACIONES_ARQUITECTONICAS = 9
    DISENO_DIGITAL_ARQUITECTURA = 10

class Asignaturas_Biologia(Enum):
    MATERIAS_INSTRUMENTALES_BIOLOGIA = 1
    DESARROLLO_ESTRUCTURA_FUNCION_SERES_VIVOS = 2
    BASES_MOLECULARES_SERES_VIVOS = 3
    ORIGEN_EVOLUCION_DIVERSIDAD_SERES_VIVOS = 4
    GENETICA = 5
    BIOLOGIA_CELULAR = 6
    ECOLOGIA = 7
    BIOLOGIA_ANIMAL = 8
    BIOLOGIA_VEGETAL = 9
    MICROBIOLOGIA = 10

class Asignaturas_CAFD(Enum):
    ANATOMIA_FUNCIONAL = 1
    BIOMECANICA_MOVIMIENTO_HUMANO = 2
    BIOQUIMICA_EJERCICIO_FISICO = 3
    FUNDAMENTOS_HABILIDADES_MOTRICES = 4
    HISTORIA_DEPORTE = 5
    FISIOLOGIA_DEL_EJERCICIO = 6
    ENTRENAMIENTO_DEPORTIVO = 7
    GESTION_DEPORTIVA = 8
    PSICOLOGIA_DEL_DEPORTE = 9
    SOCIOLOGIA_DEL_DEPORTE = 10

class Asignaturas_Enfermeria(Enum):
    ANATOMIA_HUMANA = 1
    BIOQUIMICA_GENETICA_INMUNOLOGIA = 2
    FISIOLOGIA_HUMANA = 3
    FISIOPATOLOGIA = 4
    NUTRICION_CLINICA = 5
    ENFERMERIA_COMUNITARIA = 6
    ENFERMERIA_CLINICA = 7
    ENFERMERIA_QUIRURGICA = 8
    ENFERMERIA_GERIATRICA = 9
    ENFERMERIA_PEDIATRICA = 10

#La función TodasAsignaturas incluye todas las asignaturas de todos los grados.
#(La utilizaremos para comprobar si la asignatura añadida por el usuario es válida).

def TodasAsignaturas():
    L=[Asignaturas_Enfermeria._member_names_]
    for i in Asignaturas_CAFD._member_names_:
        L.append(i)
    for i in Asignaturas_Biologia._member_names_:
        L.append(i)
    for i in Asignaturas_Arquitectura._member_names_:
        L.append(i)
    for i in Asignaturas_EducacionPrim._member_names_:
        L.append(i)
    for i in Asignaturas_Medicina._member_names_:
        L.append(i)
    for i in Asignaturas_IngIndus._member_names_:
        L.append(i)
    for i in Asignaturas_Psicologia._member_names_:
        L.append(i)
    for i in Asignaturas_Derecho._member_names_:
        L.append(i)
    for i in Asignaturas_ADE._member_names_:
        L.append(i)
    
    return L

#A la función asignatura se le inserta el valor de una instancia de la clase Grados y devuelve una lista con el nombre de sus asignaturas
#(Se utlizará para comprobar si un alumno puede matricularse de una asignatura o no en función de si pertenece a su grado).

def Asignaturas(grado):
    if grado==Grados.ADE.value:
        asignaturas=Asignaturas_ADE
    elif grado==Grados.ARQUITECTURA.value:
        asignaturas=Asignaturas_Arquitectura
    elif grado==Grados.BIOLOGIA.value:
        asignaturas=Asignaturas_Biologia
    elif grado==Grados.CAFD.value:
        asignaturas=Asignaturas_CAFD
    elif grado==Grados.DERECHO.value:
        asignaturas=Asignaturas_Derecho
    elif grado==Grados.MEDICINA.value:
        asignaturas=Asignaturas_Medicina
    elif grado==Grados.INGENIERIA_INDUSTRIAL.value:
        asignaturas=Asignaturas_IngIndus
    elif grado==Grados.EDUCACION_PRIMARIA.value:
        asignaturas=Asignaturas_EducacionPrim
    elif grado==Grados.ENFERMERIA.value:
        asignaturas=Asignaturas_Enfermeria
    else:
        raise GradoNoEncontrado("Grado no encontrado")

    return (asignaturas._member_names_)

#La clase Departamentos es una enumeración con los diferentes departamentos de la universidad.

class Departamentos(Enum):
    DIS=0
    DITEC=1
    DIIC=2


#Creamos la clase abstracta persona.

class Persona(metaclass=ABCMeta):
    def __init__(self,nombre,DNI,direccion,sexo):
        #Comprobamos si se ha insertado un nombre de tipo str.
        if not isinstance(nombre,str):
            raise NombreNoValido("Nombre no válido (debe de ser un str)")
        self.nombre=nombre
        #Creamos el atributo apellido que nos servirá para ordenar las personas por orden alfabético
        partes=nombre.split()
        self.apellido = partes[1:]
        #Para el atributo DNI no añadimos ningún requisito ya que para cada país el documento de identificación es diferente.
        #Además este atributo lo usaremos para encontrar personas y mientras coincida con el insertado no importa que formato tenga.
        self.DNI=DNI
        #Comprobamos si se ha insertado una dirección de tipo str.
        if not isinstance(direccion,str):
            raise DireccionNoValida("Dirección no válida (debe de ser un str)")
        self.direccion=direccion
        #Comprobamos si se ha insertado una instancia de la clase Sexo para el atributo sexo.
        if not isinstance(sexo,Sexo):
            raise SexoNoValido(f"Sexo no válido (debes pasar una instancia de Sexo).")
        self.sexo=sexo
    #Definimos el método abstracto info. 
    @abstractmethod
    def info(self):

        print(f"{self.nombre}\n-------------------------------\nDNI: {self.DNI}\nDireccion: {self.direccion}\nSexo: {self.sexo.name.capitalize()}")
    
    #Como hemos dicho antes definimos el método lt para poder ordenar las personas por orden alfabético.
    def __lt__(self, otro):

        return self.apellido < otro.apellido

#Creamos la clase Estudiante que hereda de persona.
class Estudiante(Persona):
    
    def __init__(self, nombre, DNI, direccion, sexo,grado,asignaturas):
        super().__init__(nombre, DNI, direccion, sexo)
        #Atributo para llevar control de las asignaturas aprobadas por el estudiante.
        self.aprobadas=[]

        #Se comprueba si se ha insertado una lista de asignaturas.
        if not isinstance(asignaturas,list):
            raise AsignaturaNoValida(f"Asignaturas no válidas (debes pasar una lista de asignaturas).")
        
        #Se comprueba si se puede ejecutar la función .name en cada asignatura insertada, para más tarde comprobar si esa asignatura pertenece al grado del estudiante.
        for i in asignaturas:
            try:
                i.name
            except:
                raise AsignaturaNoValida(f"Asignatura no valida (recuerda introducir una istanciaa de Asignaturas)")
            
        #Se comprueba si el grado insertado es una instancia de Grado en el atributo grado.
        if not isinstance(grado,Grados):
            raise GradoNoEncontrado(f"Grado no encontrado (debe pasar una instancia de Grados)")
        self.grado=grado

        #Se comprueba si cada asignatura insertada pertenece al grado del estudiante.
        for asignatura in asignaturas:
            if asignatura.name not in Asignaturas(self.grado.value):
                raise AsignaturaNoValida(f"Asignatura {asignatura.name} no válida para el grado {self.grado.name}")

        self.asignaturas=asignaturas

    #Método para mostrar la información del estudiante.
    def info(self):
        print("Rol: Estudiante")
        super().info()
        print(f"Grado: {self.grado.name.capitalize()}\nAsignaturas matriculadas: {[i.name for i in self.asignaturas]}\nAsignaturas aprobadas {[a.name for a in self.aprobadas]}")
    
    #Método para que el estudiante se matricule de una asignaaatura.
    def matricularse(self,asignatura):

        #Como antes se comprueba si la asignatura insertada es válida.
        try:
            asignatura.name
        except:
            raise AsignaturaNoValida(f"Aignatura no valida (recuerda introducir una istancia de Asignaturas)")
        
        if asignatura.name not in Asignaturas(self.grado.value):
                raise AsignaturaNoValida(f"Asignatura {asignatura} no válida para el grado {self.grado}")
        
        self.asignaturas.append(asignatura)
    
    #Método para que el alumno apruebe una asignatura.
    def aprobar(self,asignatura):
        #Se comprueba si el alumno está matriculado de la asignatura.
        if asignatura in self.asignaturas:
            self.aprobadas.append(asignatura)
            self.asignaturas.remove(asignatura)
        else:
            raise AsignaturaNoValida(f"Aignatura no valida (recuerda introducir una istanciaa de Asignaturas)")
    
#Se crea la clase abstracta Miembro_Departamento que hereda de persona.
class Miembro_departamento(Persona,metaclass=ABCMeta):
    def __init__(self, nombre, DNI, direccion, sexo,departamento):
        super().__init__(nombre, DNI, direccion, sexo)

        #Se comprueba si el departamento insertado es una instancia de Departamentos.
        if not isinstance(departamento,Departamentos):
            raise DepartamentoNoValido("Departamento no válido (añade una instancia de Departamentos)")
        self.departamento=departamento
    
    #Se crea el método abstracto info para mostrar la información de los miembros de departamento. 
    @abstractmethod
    def info(self):
        super().info()
        print(f"Departamento: {self.departamento.name}")
    
    #Metodo para cambiar a alguien de departamento.
    def cambiar_departamento(self,departamento):
        #Se comprueba si el nuevo departamento es válido.
        if not isinstance(departamento,Departamentos):
            raise DepartamentoNoValido("Departamento no válido (añade una instancia de Departamentos).")
        self.departamento=departamento

#Creamos la clase investigador que hereda de Miembro_departamento.
class Investigador(Miembro_departamento):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, DNI, direccion, sexo, departamento)

        #Se comprueba si se ha insertado un área de investigacion de tipo str.
        if not isinstance(area_investigacion,str):
            raise Area_InvestigacionNoValida("Area de investigación no válida (debe de ser un str).")
        self.area_investigacion = area_investigacion

    #Se crea el método info para mostrar la información del investigador.
    def info(self):
        print(f"Puesto: Investigador")
        super().info()
        print(f"Área de investigación: {self.area_investigacion}")

    #Método para cambiar de área de investigación.
    def cambiar_area_investigacion(self,area_investigacion):
        #Se comprueba si la nueva área de investigación es válida
        if not isinstance(area_investigacion,str):
            raise Area_InvestigacionNoValida("Area de investigación no válida (debe de ser un str).")
        self.area_investigacion=area_investigacion
    
#Creamos la clase abstracta Profesor que también hereda de Miembro_departamento. 
class Profesor(Miembro_departamento,metaclass=ABCMeta):
    def __init__(self,nombre, DNI, direccion, sexo, departamento,asignaturas):
        Miembro_departamento.__init__(self, nombre, DNI, direccion, sexo, departamento)
        #Se comprueba si se ha insertado una lista de asignaturas.
        if not isinstance(asignaturas,list):
            raise AsignaturaNoValida(f"Asignaturas no válidas (debes pasar una lista de asignaturas).")
        
        #Se comprueba si las asignaturas insertadas son válidas.
        for a in asignaturas:
            try:
                a.name
            except:
                raise AsignaturaNoValida(f"Asignatura no válida debes pasar una instancia de Asignaturas.")
            
        #Se comprueba si las asignaturas insertadas pertenecen a las asignaturas disponibles por la universidad.
        for i in asignaturas:
            if i.name not in TodasAsignaturas():
                raise AsignaturaNoValida(f"Asignatura {i} no válida")
        self.asignaturas=asignaturas
    
    #Método para añadir una asignatura al profesor.
    def añadir_asignatura(self,asignatura):
        #Se comprueba si la asignaturas insertada es válida.
        try:
            asignatura.name
        except:
            raise AsignaturaNoValida(f"Asignatura no válida debes pasar una instancia de Asignaturas.")
            
        #Se comprueba si la asignatura insertada pertenece a las asignaturas disponibles por la universidad.
        if asignatura.name not in TodasAsignaturas():
            raise AsignaturaNoValida(f"Asignatura {asignatura} no válida")
        self.asignaturas.append(asignatura)
    
    #Método para quitar una asignatura al profesor.
    def quitar_asignatura(self,asignatura):
        #Se comprueba si el profesor imparte la asignatura insertada.
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            raise AsignaturaNoValida(f"El profesor {self.nombre} no imparte la asignatura indicada")

    #Metodo abstracto para mostrar la información del profesor.
    @abstractmethod
    def info(self):
        super().info()
        print(f"Asignaturas: {[i.name for i in self.asignaturas]}")

    
#Creamos la clase Profesor titular que hereda de Profesor y de Investigador.
class Profesor_Titular(Profesor, Investigador):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion, asignaturas):
        Profesor.__init__(self, nombre, DNI, direccion, sexo, departamento, asignaturas)
        Investigador.__init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion)

    #Método para mostrar la información del Profesor titular.
    def info(self):
        print(f"Puesto: Profesor titular")
        super().info()

#Creamos la clase Profesor_Asociado que hereda de profesor.
class Profesor_Asociado(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento,asignaturas):
        super().__init__(nombre, DNI, direccion, sexo, departamento,asignaturas)

    #Método para mostrar la información del profesor asociado.
    def info(self):
        print(f"Puesto: Profesor asociado")
        super().info()


#Creamos la clase Universidad para manejar todas las clases creadas anteriormente.
class Universidad:
    def __init__(self,miembros_departamento,estudiantes):
        #Comprobamos que se inserta una lista de miembros de departamento y de estudiantes.
        if not isinstance(miembros_departamento, list) or not isinstance(estudiantes,list):
            raise NoLista(f"Debes insertar una lista de miembros de departamento y de estudiantes")
        
        #Comprobamos que todos los miembros de departamento insertados son instancias de la clase Miembro_departamento.
        for md in  miembros_departamento:
            if not isinstance(md,Miembro_departamento):
                raise Miembro_departamentoNoValido(f"Miembro departamento no válido (inserte una instancia de Miembro_departamento).")
        self.miembros_departamento=miembros_departamento

        #Comprobamos que todos los estudiantes insertados son instancias de la clase Estudiante.
        for est in estudiantes:
            if not isinstance(est,Estudiante):
                raise EstudianteNoValido(f"Estudiante no válido (inserte una instancia de Estudiante).")
        self.estudiantess=estudiantes
    
    #Método para añadir un estudiante a la universidad.
    def añadir_estudiante(self,nombre,DNI,dirección,sexo,grado,asignaturas):
        self.estudiantess.append(Estudiante(nombre,DNI,dirección,sexo,grado,asignaturas))
    
    #Método para añadir un profesor titular a la universidad.
    def añadir_profesor_titular(self,nombre,DNI,direccion,sexo,departamento,area_investigacion,asignaturas):
        self.miembros_departamento.append(Profesor_Titular(nombre,DNI,direccion,sexo,departamento,area_investigacion,asignaturas))
    
    #Método para añadir un profesor asociado a la universidad.
    def añadir_profesor_asociado(self,nombre,DNI,direccion,sexo,departamento,asignaturas):
        self.miembros_departamento.append(Profesor_Asociado(nombre,DNI,direccion,sexo,departamento,asignaturas))
    
    #Método para añadir un investigador a la universidad.
    def añadir_investigador(self,nombre,DNI,direccion,sexo,departamento,area_investigacion):
        self.miembros_departamento.append(Investigador(nombre,DNI,direccion,sexo,departamento,area_investigacion))

    #Método para eliminar un estudiante de la universidad a través del DNI.  
    def eliminar_estudiante(self,DNI):
        encontrado=False
        for est in self.estudiantes():
            if DNI==est.DNI:
                encontrado=True
                self.estudiantess.remove(est)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún estudiante con DNI: {DNI}")
    
    #Método para eliminar un miembro de departamento de la universidad a través del DNI.
    def eliminar_miembro_departamento(self,DNI):
        encontrado=False
        for md in self.miembros_departamento:
            if DNI==md.DNI:
                encontrado=True
                self.miembros_departamento.remove(md)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún miembro de departamento con DNI: {DNI}")

    #Método que devuelve una lista de los estudiantes de la universidad por orden alfabético.
    def estudiantes(self):
        estudiantes=self.estudiantess
        estudiantes.sort()
        return estudiantes
    
    #Método que devuelve una lista de los profesores de la universidad por orden alfabético.
    def profesores(self):
        profesores=[]
        for md in self.miembros_departamento:
            if isinstance(md,Profesor):
                profesores.append(md)
        profesores.sort()
        return profesores

    #Método que devuelve una lista de los profesores titulares de la universidad por orden alfabético.
    def profesores_titulares(self):
        profesores_titulares=[]
        for i in self.profesores():
            if isinstance(i,Profesor_Titular):
                profesores_titulares.append(i)
        profesores_titulares.sort()
        return profesores_titulares
    
    #Método que devuelve una lista de los profesores asociados de la universidad por orden alfabético.
    def profesores_asociados(self):
        profesores_asociados=[]
        for i in self.profesores():
            if isinstance(i,Profesor_Asociado):
                profesores_asociados.append(i)
        profesores_asociados.sort()
        return profesores_asociados

    #Método que devuelve una lista de los investigadores de la universidad por orden alfabético.
    def investigadores(self):
        investigadores=[]
        for md in self.miembros_departamento:
            if isinstance(md,Investigador):
                investigadores.append(md)
        investigadores.sort()
        return investigadores
    
    #Método que devuelve una lista de los miembros que pertenecen al departamento DIIC.
    def departamentoDIIC(self):
        DICC=[]
        for md in self.miembros_departamento:
            if md.departamento==Departamentos.DIIC:
                DICC.append(md)
        return DICC
    
    #Método que devuelve una lista de los miembros que pertenecen al departamento DIS.
    def departamentoDIS(self):
        DIS=[]
        for md in self.miembros_departamento:
            if md.departamento==Departamentos.DIS:
                DIS.append(md)
        return DIS
    
    #Método que devuelve una lista de los miembros que pertenecen al departamento DITEC.
    def departamentoDITEC(self):
        DITEC=[]
        for md in self.miembros_departamento:
            if md.departamento==Departamentos.DITEC:
                DITEC.append(md)
        return DITEC
    
    #Método que muestra por pantalla el nombres y el DNI de todos profesores de la universidad.
    def mostrar_profesores(self):
        print(f"Profesores titulares:\n--------------------------------")
        for t in self.profesores_titulares():
            print (f"\n{t.nombre}\nDNI:{t.DNI}")
        print(f"\n\nProfesores asociados:\n--------------------------------")
        for a in self.profesores_asociados():
            print (f"\n{a.nombre}\nDNI:{a.DNI}")

    #Método que muestra por pantalla el nombre y el DNI de los miembros de cada departamento.
    def mostrar_miembros_departamento(self):
        print(f"DIIC:--------------------------")
        for diic in self.departamentoDIIC():
            print (f"\n{diic.nombre}\nDNI:{diic.DNI}")
        
        print(f"\nDIS:--------------------------")
        for dis in self.departamentoDIS():
            print (f"\n{dis.nombre}\nDNI:{dis.DNI}")
        
        print(f"\nDITEC:--------------------------")
        for ditec in self.departamentoDITEC():
            print (f"\n{ditec.nombre}\nDNI:{ditec.DNI}")
    
    #Método que muestra por pantalla el nombre, el DNI y el grado de todos los estudiantes de la universidad.
    def mostrar_estudiantes(self):
        print(f"Estudiantes\n-----------------------------------")
        for e in self.estudiantes():
            print (f"Nombre: {e.nombre}\nDNI: {e.DNI}\nGrado: {e.grado.name}\n---------------------------")

    #Método que muestra por pantalla el nombre, el DNI y el área de investigación de todos los investigadores de la universidad.
    def mostrar_investigadores(self):
        print(f"Investigadores\n-----------------------------------")
        for inv in self.investigadores():
            print (f"Nombre: {inv.nombre}\nDNI: {inv.DNI}\nArea de investigación: {inv.area_investigacion}\n---------------------------")

    #Método que cambia de departamento a una persona insertando su DNI y el nuevo departamento.
    def cambiar_departamento(self,DNI,departamento):
        encontrado=False
        for md in self.miembros_departamento:
            if md.DNI==DNI:
                encontrado=True
                md.cambiar_departamento(departamento)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún miembro de departamento con DNI: {DNI}")

    #Método que cambia de área de investigación a una persona insertando su DNI y la nueva área de investigación.
    def cambiar_area_investigacion(self,DNI,area_investigacion):
        encontrado=False
        for md in self.investigadores():
            if md.DNI==DNI:
                encontrado=True
                md.cambiar_area_investigacion(area_investigacion)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún investigador con DNI: {DNI}")

    #Método para matricular a un estudiante de una asignatura insertando su DNI y la nueva asignatura.    
    def matricular(self,DNI,asignatura):
        encontrado=False
        for estudiante in self.estudiantes():
            if estudiante.DNI==DNI:
                encontrado=True
                estudiante.matricularse(asignatura)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún estudiante con DNI: {DNI}")
        
    #Método para aprobar una asignatura de un estudiante insertando su DNI y la asignatura. 
    def aprobar_asignatura(self,DNI,asignatura):
        encontrado=False
        for estudiante in self.estudiantes():
            if estudiante.DNI==DNI:
                encontrado=True
                estudiante.aprobar(asignatura)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún estudiante con DNI: {DNI}")
        
    #Método para añadir una asignatura a un profesor insertando su DNI y la nueva asignatura.    
    def añadir_asignaturaProf(self,DNI,asignatura):
        encontrado=False
        for profesor in self.profesores():
            if profesor.DNI==DNI:
                encontrado=True
                profesor.añadir_asignatura(asignatura)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún profesor con DNI: {DNI}")
    
    #Método para quitar una asignatura a un profesor insertando su DNI y la asignatura.    
    def quitar_asignaturaProf(self,DNI,asignatura):
        encontrado=False
        for profesor in self.profesores():
            if profesor.DNI==DNI:
                encontrado=True
                profesor.quitar_asignatura(asignatura)
                break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún profesor con DNI: {DNI}")
    
    #Muestra por pantalla la información de un estudiante insertando su DNI.
    def info_estudiante(self,DNI):
        encontrado=False
        for estudiante in self.estudiantes():
            if estudiante.DNI==DNI:
                    encontrado=True
                    estudiante.info()
                    break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún estudiante con DNI: {DNI}")
        
    #Muestra por pantalla la información de un miembro de departamento insertando su DNI.
    def info_miembro_departamento(self,DNI):
        encontrado=False
        for md in self.miembros_departamento:
            if md.DNI==DNI:
                    encontrado=True
                    md.info()
                    break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún miembro de departamento con DNI: {DNI}")
        
    #Devuelve las asignaturas matriculadas de un estudiante de la universidad.
    def asignaturas_estudiantes(self,DNI):
        encontrado=False
        for estudiante in self.estudiantes():
            if estudiante.DNI==DNI:
                    encontrado=True
                    return estudiante.asignaturas
                    break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún estudiante con DNI: {DNI}")
        
    #Devuelve el departamento de un miembro de departamento de la universidad.
    def departamento_md(self,DNI):
        encontrado=False
        for md in self.miembros_departamento:
            if md.DNI==DNI:
                    encontrado=True
                    return md.departamento
                    break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún miembro de departamento con DNI: {DNI}")
    
    #Devuelve el area de investigacion un miembro de departamento de la universidad.
    def area_investigacion_md(self,DNI):
        encontrado=False
        for md in self.miembros_departamento:
            if md.DNI==DNI:
                    encontrado=True
                    return md.area_investigacion
                    break
        if not encontrado:
            raise DNINoEncontrado(f"No se ha encontrado ningún miembro de departamento con DNI: {DNI}")




#######ESTUDIANTES########

est1=Estudiante(nombre="Juan Pérez Calatraba",
                    DNI="799568L",
                    direccion="c/Calle de la Luna",
                    sexo=Sexo.MASCULINO,
                    grado=Grados.ADE,
                    asignaturas=[Asignaturas_ADE.CONTABILIDAD_FINANCIERA,Asignaturas_ADE.ETICA_EMPRESARIAL,Asignaturas_ADE.FINANZAS])
    
est2=Estudiante(nombre="Ernesto Gómez Sanchez",
                    DNI="21098765K",
                    direccion="c/Avenida del Sol",
                    sexo=Sexo.MASCULINO,
                    grado=Grados.ARQUITECTURA,
                    asignaturas=[Asignaturas_Arquitectura.DISENO_DIGITAL_ARQUITECTURA,Asignaturas_Arquitectura.GEOMETRIA_DESCRIPTIVA,Asignaturas_Arquitectura.HISTORIA_ARTE])
    
est3=Estudiante(nombre="Lucía Fernández Ruiz",
                    DNI="56789012J",
                    direccion="c/Callejón del Bosque",
                    sexo=Sexo.FEMENINO,
                    grado=Grados.BIOLOGIA,
                    asignaturas=[Asignaturas_Biologia.BIOLOGIA_ANIMAL,Asignaturas_Biologia.BASES_MOLECULARES_SERES_VIVOS,Asignaturas_Biologia.BIOLOGIA_VEGETAL])

est4=Estudiante(nombre="Carlos Martín López",
                    DNI="45678901G",
                    direccion="c/Ronda de la Montaña",
                    sexo=Sexo.MASCULINO,
                    grado=Grados.MEDICINA,
                    asignaturas=[Asignaturas_Medicina.ANATOMIA_HUMANA,Asignaturas_Medicina.BIOQUIMICA_BIOLOGIA_MOLECULAR,Asignaturas_Medicina.MEDICINA_INTERNA])

est5=Estudiante(nombre="Sofía Pérez Jiménez",
                DNI="09876543F",
                direccion="c/Bulevar del Mar",
                sexo=Sexo.FEMENINO,
                grado=Grados.DERECHO,
                asignaturas=[Asignaturas_Derecho.DERECHO_ADMINISTRATIVO,Asignaturas_Derecho.DERECHO_AMBIENTAL,Asignaturas_Derecho.DERECHO_FISCAL,Asignaturas_Derecho.DERECHO_TRABAJO_SEGURIDAD_SOCIAL])

estudiantes=[est1,est2,est3,est4,est5]

######Profesores Titulares#########

pt1=Profesor_Titular(nombre="Enrique Cueto Delgado",
                        DNI="12345678A",
                        direccion="c/Sendero de la Aurora",
                        sexo=Sexo.MASCULINO,
                        departamento=Departamentos.DIIC,
                        area_investigacion="Ingeniería y Tecnología",
                        asignaturas=[Asignaturas_Arquitectura.INSTALACIONES_ARQUITECTONICAS,Asignaturas_IngIndus.INGENIERIA_DE_MATERIALES])
                        
pt2=Profesor_Titular(nombre="Marta Vidal Torres",
                     DNI="87654321B",
                     direccion="c/Calle de la Luna",
                     sexo=Sexo.FEMENINO,
                     departamento=Departamentos.DITEC,
                     area_investigacion="Ciencias Sociales",
                     asignaturas=[Asignaturas_ADE.MARKETING, Asignaturas_ADE.DIRECCION_ESTRATEGICA])

pt3=Profesor_Titular(nombre="Javier Solís Ramírez",
                     DNI="23456789C",
                     direccion="c/Paseo de las Estrellas",
                     sexo=Sexo.MASCULINO,
                     departamento=Departamentos.DIS,
                     area_investigacion="Humanidades",
                     asignaturas=[Asignaturas_Derecho.DERECHO_CIVIL, Asignaturas_Derecho.DERECHO_MERCANTIL])

pt4=Profesor_Titular(nombre="Lucía Méndez Castro",
                     DNI="98765432D",
                     direccion="c/Camino del Río",
                     sexo=Sexo.FEMENINO,
                     departamento=Departamentos.DIIC,
                     area_investigacion="Ciencias de la Salud",
                     asignaturas=[Asignaturas_Medicina.ANATOMIA_HUMANA, Asignaturas_Medicina.BIOQUIMICA_BIOLOGIA_MOLECULAR])

pt5=Profesor_Titular(nombre="Carlos Ruiz Gómez",
                    DNI="34567890E",
                    direccion="c/Vía Láctea",
                    sexo=Sexo.MASCULINO,
                    departamento=Departamentos.DITEC,
                    area_investigacion="Ingeniería y Tecnología",
                    asignaturas=[Asignaturas_IngIndus.GESTION_PRODUCCION, Asignaturas_IngIndus.DISENO_SISTEMAS_PRODUCCION])

######Profesores Asociados#########

pa1=Profesor_Asociado(nombre="Ana Torres López",
                      DNI="76543210F",
                      direccion="c/Callejón del Bosque",
                      sexo=Sexo.FEMENINO,
                      departamento=Departamentos.DIS,
                      asignaturas=[Asignaturas_ADE.CONTABILIDAD_FINANCIERA, Asignaturas_ADE.FINANZAS])

pa2=Profesor_Asociado(nombre="Luis Navarro Méndez",
                      DNI="87654321J",
                      direccion="c/Ronda de la Montaña",
                      sexo=Sexo.MASCULINO,
                      departamento=Departamentos.DITEC,
                      asignaturas=[Asignaturas_Derecho.DERECHO_CIVIL, Asignaturas_Derecho.DERECHO_PENAL])

pa3=Profesor_Asociado(nombre="Sara Jiménez Ruiz",
                      DNI="98765432H",
                      direccion="c/Bulevar del Mar",
                      sexo=Sexo.FEMENINO,
                      departamento=Departamentos.DIIC,
                      asignaturas=[Asignaturas_Psicologia.PSICOLOGIA_CLINICA_SALUD, Asignaturas_Psicologia.PSICOLOGIA_EDUCACION])

pa4=Profesor_Asociado(nombre="Diego García Sánchez",
                      DNI="12345678L",
                      direccion="c/Vía Láctea",
                      sexo=Sexo.MASCULINO,
                      departamento=Departamentos.DIS,
                      asignaturas=[Asignaturas_IngIndus.GESTION_PRODUCCION, Asignaturas_IngIndus.LOGISTICA_INDUSTRIAL])

pa5=Profesor_Asociado(nombre="Irene Espinosa Castro",
                      DNI="23456789K",
                      direccion="c/Plaza del Futuro",
                      sexo=Sexo.FEMENINO,
                      departamento=Departamentos.DITEC,
                      asignaturas=[Asignaturas_Medicina.ANATOMIA_HUMANA, Asignaturas_Medicina.FISIOLOGIA_HUMANA])
######Investigadores#########

inv1=Investigador(nombre="Roberto Núñez Castro",
                  DNI="11223344A",
                  direccion="c/Avenida del Sol",
                  sexo=Sexo.MASCULINO,
                  departamento=Departamentos.DIIC,
                  area_investigacion="Ciencias Exactas y de la Tierra")

inv2=Investigador(nombre="Carmen López Ruiz",
                  DNI="22334455B",
                  direccion="c/Calle de la Luna",
                  sexo=Sexo.FEMENINO,
                  departamento=Departamentos.DITEC,
                  area_investigacion="Ciencias Ambientales")

inv3=Investigador(nombre="Francisco Gómez Jiménez",
                  DNI="33445566C",
                  direccion="c/Paseo de las Estrellas",
                  sexo=Sexo.MASCULINO,
                  departamento=Departamentos.DIS,
                  area_investigacion="Biotecnología")

inv4=Investigador(nombre="Laura Martín Pérez",
                  DNI="44556677D",
                  direccion="c/Camino del Río",
                  sexo=Sexo.FEMENINO,
                  departamento=Departamentos.DIIC,
                  area_investigacion="Energías Renovables y Sostenibilidad")

inv5=Investigador(nombre="José Antonio Sánchez Martínez",
                  DNI="55667788E",
                  direccion="c/Vía Láctea",
                  sexo=Sexo.MASCULINO,
                  departamento=Departamentos.DITEC,
                  area_investigacion="Informática y Ciencias de la Computación")

miembros_departamento = [
    pt1, pt2, pt3, pt4, pt5,
    pa1, pa2, pa3, pa4, pa5,
    inv1, inv2, inv3, inv4, inv5
]

######UNIVERSIDAD#########

umu=Universidad(miembros_departamento,estudiantes)

###Funcionamiento
if __name__ == "__main__":
    
    umu.mostrar_estudiantes()

    umu.info_estudiante("45678901G")

    umu.aprobar_asignatura("45678901G",Asignaturas_Medicina.ANATOMIA_HUMANA)

    umu.info_estudiante("45678901G")

    umu.mostrar_investigadores()

    umu.cambiar_area_investigacion("87654321B","Humanidades")

    umu.info_miembro_departamento("87654321B")

    umu.mostrar_miembros_departamento()

    umu.info_miembro_departamento("23456789K")

    umu.añadir_asignaturaProf("23456789K",Asignaturas_Medicina.GINECOLOGIA_OBSTETRICIA)

    umu.info_miembro_departamento("23456789K")

    umu.quitar_asignaturaProf("23456789K",Asignaturas_Medicina.GINECOLOGIA_OBSTETRICIA)

    umu.info_miembro_departamento("23456789K")

    umu.mostrar_profesores()

    umu.eliminar_miembro_departamento("87654321B")
    
    umu.mostrar_profesores()