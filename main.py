import requests

def main():
    print('########################')
    print('##### Consulta CEP #####')
    print('########################')
    print()

    cep_input = input('Digite um CEP para consulta: ')

    if len(cep_input) != 8:
        print('CEP Invalido!!!')
        exit()


    request = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
    address_data = request.json()
    print('-----------------------------------------')
    if 'erro' not in address_data:
        
        print('CEP Encontrado')
        print(f"CEP: {address_data['cep']}")
        print(f"Endereço: {address_data['logradouro']}")
        print(f"Bairro: {address_data['bairro']}")
        print(f"Cidade: {address_data['localidade']}")
        print(f"Estado: {address_data['uf']}")
    else:
        print(f'{cep_input}: CEP Invalido')

    print()
    option = input('Deseja fazer uma nova consulta ?\n-----------------------------------------\nSIM : 1\nNÃO : 2\n')
    if option == '1':
        main()
    else:
        print('Saindo....')

if __name__ == '__main__':
    main()

