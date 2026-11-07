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

# Mostrar a lista completa

print(notas)

# Mostrar a primeira nota

print(notas[0])

# Mostrar a última nota

print(notas[4]) ou print(notas[-1])

soma = sum(notas)

media = soma/len(notas)

lista = ["maçã", "banana", "laranja"]

# Acrescentar "pêra" com .append()

lista.append("pêra")

# Retira "banana" com .remove()

lista.remove("banana")

- Tuple

# tuples são ordenada e imutáveis

coordenadas = (38.65, -27.22)

print(coordenadas)

latitude = coordenadas[0]

longitude = coordenadas[1]

- Set

E.g.:
# sets não há repetidos

notas = [1,2,2,3,4,4,5]

print(notas)

notas_set = set(notas)

print(notas_set)

conjunto.add("")

conjunto.remove("")
- Dictionary

# Dicionários

# Chave -> valor: dados associados

#criar a ficha de um aluno com nome, idade e média

aluno = {"nome": "Ana", "idade": 17, "media": 18}

print(aluno)

print(aluno["nome"])
print(aluno["idade"])
print(aluno["media"])

aluno["media"] = 15

print(aluno["media"])

# As chasves mantém-se

#usar = e não ==

```

# Ciclos

### While(`while`)

### For(`for`)

### funções usadas com ciclos

- break: termina o ciclo
- continue: salta para a própria iteração
- pass: não executa nenhuma ação


