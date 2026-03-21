from pessoa_fisica import Pessoa_fisica

from pessoa_juridica import Pessoa_juridica

cliente_fisico = Pessoa_fisica("Brasil", "10/11/2022", "João","da Silva", "111-222-333-44")

cliente_juridco = Pessoa_juridica("Brasil","10/11/2022","Juninho GamePlays","JG games", "JG", "99.999.999/9999-99")


print(cliente_fisico.__str__())
print("_______________________________")
print(cliente_juridco.__str__())