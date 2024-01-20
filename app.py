
registroVeiculo = [
    ['r1', 'BEE4R22', 70.00, 60, 'comum'],
    ['r1', 'DKR5Y21', 67.00, 60, 'especial'],
    ['r1', 'ABX4I22', 60.00, 60, 'comum'],
    ['r1', 'ABT8I78', 67.01, 60, 'comum'],
    ['r2', 'VXX0f74', 56.90, 80, 'comum'],
    ['r2', 'AKR7T45', 87.00, 80, 'comum'],
    ['r2', 'ADD1G78', 89.90, 80, 'comum'],
    ['r2', 'CFG3J77', 73.89, 80, 'comum'],
    ['r3', 'ERR3J79', 73.89, 100, 'comum'],
    ['r3', 'ERP1J22', 65.89, 100, 'comum'],
    ['r3', 'BNG9J99', 110.89, 100, 'especial'],
    ['r3', 'ABT8I78', 110.98, 100, 'comum'],
    ['r3', 'ABT8I78', 106.98, 100, 'comum']
]

print("Tomou multa")

for elemento in registroVeiculo:
    # Calcula a porcentagem de excesso de velocidade
    pctExcesso = (float(elemento[2]) - float(elemento[3])) / float(elemento[3]) * 100
    
    #teste para ver se o radar é menor que 100 ou não se for adiciona uma tolerncia de 7 se sim não adiciona limite
    if elemento[2]<100:
        pas = (float(elemento[3]) + 7)
    else:
        pas = elemento[3]
        
    # Verifica se o veículo é especial e se a porcentagem de excesso é positiva
    if not elemento[4] == "especial" and pctExcesso > 0 and elemento[2] > pas:
        print(f"Placa: {elemento[1]} - Porcentagem: {pctExcesso:.2f}%  -  Numero do radar: {elemento[0]}")
  
        
   
#if not registroVeiculo[0][4] == "comom": #veiculoEspecial == False
#    print(f"{registroVeiculo[0][1]} - {pctExecesso:.2f}  -  {registroVeiculo[0][0]}")

# print(dir(registroVeiculo))
# print(type(registroVeiculo))
# print(registroVeiculo.__len__())
