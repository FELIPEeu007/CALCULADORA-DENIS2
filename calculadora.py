#Calculadora de aprovação escolar

nome = input("digite o nome do estudante: ")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovacao = 180

#Coleta as notas dos 3 Períodos
for i in range(1, quantidade_trimestre + 1):
    nota = float(input("Informe a nota{i}º período: "))
    soma_notas +=nota
    
    print("-" * 30)
    print(f"Estudantes : {nome}")
    print(f"Pontuação Total : {soma_notas}")
    
    #Verificar os status de aprovação
    if soma_notas >= meta_aprovação:
        print("Status: APROVADÃO! Parabens!! Finalmente!!")
    else:
        pontos_faltantes = meta_aprovacao - soma_notas
        print("Status: TENTE OUTRA VEZ!!")
        print(f"Faltaram {potos_faltantes} pontos para atingir o mínimo de {meta_aprovacao}.")
        
    
    
    
    
    
    
    