import requests
print('____________________')
print('')
print('    Consulta CEP    ')
print('____________________')
print('')
cep = input('Digite seu CEP: ')
# print (cep)

if len(cep)!= 8:
    print('Digite um CEP válido!')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep) )

print(request.json())