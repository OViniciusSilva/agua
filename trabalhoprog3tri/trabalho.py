from peewee import *

arq = "Fazenda.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Plantas(BaseModel):
    nome = Charfield()
    tempo_crescimento = Floatflied()
    espécie_plantae = Charfield(Primary Key=True)

class Maquinario(BaseModel):
    codigo_chassi = Charfield(Primary Key= True)
    marca = Charfield()
    funcao = Charfield()
    cpf = ForeignKeyField(Funcionario)

class SiloDeVenda(BaseModel):
    codigo = Charfield(Primary Key= True)
    capacidade = Floatfield()
    especie = ForeignKeyField(planta)

class fornecedor(BaseModel):
    Cnpj = Charfield(Primary Key = True)
    nome_dono = Charfield()
    especie_animalia = ForeignKeyField(animal)

class comprador(BaseModel):
    loja = Charfield(Primary Key = True)
    Espécie = ForeignKeyField(planta)

class Funcionario(BaseModel):
    nome = Charfield()
    funcao = Charfield()
    cpf = Charfield(Primary Key = True)

class Animal(BaseModel):
    Espécie_animalia = Charfield(Primary Key = True)
    produção = Charfield()
    Tipo_Comida = Charfield()

class lote(BaseModel):
    Tamanho = floatfield()
    Codigo_lote = charfield(Primary Key = True)
    espécie_plantae = ForeignKeyField(Planta)

class venda(BaseModel):
    data = Charfield()
    comprador = ForeignKeyField(comprador)
    especie = ForeignKeyField(Plantas)

class estoque(BaseModel):
    quantidade = Floatflied()
    codigo_estoque = charfield(primary key = True)
    especie = ForeignKeyField(Plantas)

db.connect()
db.create_tables([Plantas,Maquinario,SiloDeVenda,fornecedor,comprador,Funcionario,animal,lote,venda,estoque])

soja = Plantas.create(nome = "soja", tempo tempo_crescimento = 5 , Espécie = "Glycine max")
plantalist = list(map(model_to_dict, Plantas.select()))

triturador = Maquinario.create([codigo_chassi = "4141", marca = "AGCO", funcao = "triturar", cpf = "4141456641"])
maquinalist = list(map(model_to_dict, Maquinario.select))

silo1 = SiloDeVenda.create(codigo = "1235", quantidade = 1451, especie = "soja")
silolist = list(map(model_to_dict, SiloDeVenda.select))

junior = fornecedor.create(Cnpj = "41515626", nome_dono ="kleber",especie_animalia = "vaca")
fornecedorlist = list(map(model_to_dict, fornecedor.select))

maiconcomprador = comprador.create(loja = "girassol" , especie = "soja")
compradorlist = list(map(model_to_dict, comprador.select))  

kotaka = Funcionario.create(nome = "kotaka", funcao = "arrar", cpf = "141512363")
Funcionariolist = list(map(model_to_dict, Funcionario.select))

vaca = Animal.create(Espécie_animalia = "vaca", producao = "leite" , tipo_comida = "grama")
animallist = list(map(model_to_dict, animal.select))

lote1 lotel.create(tamanho = "251", codigo = "4562", especie = "soja")
lotelist = list(map(model_to_dict, lote.select))

venda1 = venda.create(data = "12/12/2019", comprador = "maicon" , Espécie = "soja" )
vendalsit = list(map(model_to_dict, lote.select))

estoque1 = estoque.create(quantidade = 156 , codigo_estoque = "45532", espécie = "soja")
estoquelist = list(map(model_to_dict, estoque.select))

def teste():
    teste1 = [plantalist,maquinalist,silolist,fornecedorlist,compradorlist,Funcionariolist,animallist, lotelist,vendalsit,estoquelist]
    return teste1