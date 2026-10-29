# ap-inf-B

## Notas das aulas

### Identificadores e constantes

- Um identificador é o nome atribuído a uma variável, função ou outro elemento.
- Não pode começar por um número. Pode começar por uma letra ou `_` e pode conter números depois do primeiro carácter.
- Em Python, uma constante é uma variável que, por convenção, não deve ser alterada. O nome escreve-se em maiúsculas, por exemplo `TAXA = 0.23`.

## Estruturas de dados

As estruturas abaixo permitem guardar e organizar vários valores. A escolha depende, entre outras coisas, de ser necessário manter uma ordem, permitir alterações ou evitar valores repetidos.

### Lista (`list`)

- **Ordenada:** mantém a ordem dos elementos; permite aceder por índice (a partir de `0`).
- **Mutável:** pode ser alterada depois de criada.
- **Repetidos:** são permitidos; pode conter valores de tipos diferentes.

```python
notas = [15, 18, 12, 17, 14]

print(notas)       # Lista completa
print(notas[0])    # Primeiro elemento
print(notas[-1])   # Último elemento

soma = sum(notas)
media = soma / len(notas)

frutas = ["maçã", "banana", "laranja"]
frutas.append("pêra")       # Acrescenta no fim
frutas.remove("banana")     # Remove a primeira ocorrência
```

### Tuplo (`tuple`)

- **Ordenado:** mantém a ordem e permite acesso por índice.
- **Imutável:** não se podem substituir, acrescentar ou remover elementos depois da criação.
- **Repetidos:** são permitidos.
- Útil para agrupar valores que não devem ser alterados.

```python
coordenadas = (38.65, -27.22)

latitude = coordenadas[0]
longitude = coordenadas[1]
print(coordenadas)
```

### Conjunto (`set`)

- **Sem ordem definida:** não se acede aos elementos por índice; a ordem de apresentação pode variar.
- **Mutável:** é possível acrescentar e remover elementos.
- **Sem repetidos:** cada elemento é único. Os elementos têm de ser imutáveis (por exemplo, números ou texto).
- Útil para eliminar duplicados e testar pertença a um conjunto.

```python
notas = [1, 2, 2, 3, 4, 4, 5]
notas_set = set(notas)
print(notas_set)  # {1, 2, 3, 4, 5} (a ordem pode variar)

notas_set.add(6)       # Acrescenta um elemento
notas_set.discard(10)  # Remove se existir; não dá erro se não existir
notas_set.remove(5)    # Remove; dá erro se não existir
```

### Dicionário (`dict`)

- Guarda pares **chave: valor**; cada chave identifica o valor associado.
- **Mutável:** é possível acrescentar, alterar ou remover pares.
- **Ordem:** mantém a ordem de inserção em Python moderno (Python 3.7+).
- **Chaves únicas:** não podem repetir-se e têm de ser de um tipo imutável, como texto, números ou tuplos de valores imutáveis. Os valores podem repetir-se e podem ser de qualquer tipo.
- Acedemos ao valor através da chave, não de um índice numérico.

```python
# Ficha de uma aluna: nome, idade e média
aluno = {"nome": "Ana", "idade": 17, "media": 18}

print(aluno["nome"])
print(aluno["idade"])
print(aluno["media"])

aluno["media"] = 15                 # Altera um valor existente
aluno["turma"] = "12.º B"           # Acrescenta uma chave e um valor
print(aluno["media"])
```

> Para atribuir um valor, usa-se `=`. `==` serve para comparar se dois valores são iguais.

