from array import array

# Tuples:
    # Armazenar mais de uma informação em variáveis;
    # Manter a sequência dos dados em uma variável;
    # Não podem ser alteradas;
    # listas começam com [], tuples com ();

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

cores_list.append('roxo')

print(cores_list)

# Arrays:
    # Melhor do que lista para muitos itens;
    # Problemas de performance na lista;
    # Não está, por padrão, no python, deve ser importada;

letras = ['a', 'b', 'c', 'd']
numero_i = [10, 20, 30 , 40]
numero_f = [1.2, 3.4, 4.3, 3.6]

print(letras)
print(numero_i)
print(numero_f)

# Ter cuidado com o tipo de array, procurar no 'google'...

letras = array('u', ['a', 'b', 'c', 'd'])
numero_i = array('i',[10, 20, 30 , 40])
numero_f = array('f', [1.2, 3.4, 4.3, 3.6])

print(letras)
print(numero_i)
print(numero_f)


