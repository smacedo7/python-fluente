# linguagem usada para conversar com banco de dados relacionais

# select -> buscar dados
# SELECT * FROM produtos;
# colunas especificas -> SELECT nome, preco
                        # FROM produtos;
# com filtro

# """

'''
SQL significa Structured Query Language.

É a linguagem usada para criar, consultar, atualizar e excluir dados
de bancos de dados relacionais, como:

* PostgreSQL
* MySQL
* SQLite
* SQL Server
* Oracle

Em bancos relacionais, os dados são organizados principalmente em tabelas.

Exemplo de tabela:

produtos

id | nome       | preco | estoque
1  | X-Bacon    | 30.00 | 10
2  | X-Salada   | 25.00 | 5
3  | Coca-Cola  | 8.00  | 20

========================================

1. CRUD
   ========================================

CRUD representa as quatro operações principais de um sistema:

C = Create  -> criar
R = Read    -> ler ou buscar
U = Update  -> atualizar
D = Delete  -> excluir

No SQL:

CREATE -> INSERT
READ   -> SELECT
UPDATE -> UPDATE
DELETE -> DELETE

========================================
2. SELECT
=========

SELECT é usado para buscar dados.

Buscar todas as colunas:

SELECT * FROM produtos;

O símbolo * significa todas as colunas.

Buscar apenas algumas colunas:

SELECT nome, preco
FROM produtos;

Buscar com condição:

SELECT *
FROM produtos
WHERE preco > 20;

Leitura:

Selecione todos os dados
da tabela produtos
onde o preço seja maior que 20.

========================================
3. WHERE
========

WHERE é usado para filtrar registros.

SELECT *
FROM produtos
WHERE estoque > 0;

Operadores de comparação:

=   igual
!=  diferente
<>  diferente

> maior que
> <   menor que
> =  maior ou igual
> <=  menor ou igual

Exemplos:

SELECT *
FROM produtos
WHERE preco = 30;

SELECT *
FROM produtos
WHERE estoque != 0;

No SQL, usamos apenas um sinal de igual para comparação:

WHERE preco = 30

Em Python, normalmente usamos dois:

preco == 30

========================================
4. INSERT
=========

INSERT é usado para adicionar registros.

INSERT INTO produtos (nome, preco, estoque)
VALUES ('X-Tudo', 38.00, 15);

Estrutura:

INSERT INTO nome_da_tabela (colunas)
VALUES (valores);

========================================
5. UPDATE
=========

UPDATE é usado para atualizar registros.

UPDATE produtos
SET preco = 35.00
WHERE id = 1;

Também é possível alterar mais de uma coluna:

UPDATE produtos
SET preco = 35.00,
estoque = 20
WHERE id = 1;

CUIDADO:

Sem WHERE, todos os registros podem ser alterados.

UPDATE produtos
SET preco = 35.00;

Esse comando altera o preço de todos os produtos.

========================================
6. DELETE
=========

DELETE é usado para excluir registros.

DELETE FROM produtos
WHERE id = 1;

CUIDADO:

Sem WHERE, todos os registros podem ser excluídos.

DELETE FROM produtos;

========================================
7. AND
======

AND exige que todas as condições sejam verdadeiras.

SELECT *
FROM produtos
WHERE preco > 20
AND estoque > 0;

O produto precisa:

* custar mais de 20
* possuir estoque maior que 0

========================================
8. OR
=====

OR exige que pelo menos uma condição seja verdadeira.

SELECT *
FROM produtos
WHERE preco < 10
OR estoque > 15;

========================================
9. NOT
======

NOT nega uma condição.

SELECT *
FROM produtos
WHERE NOT estoque = 0;

Também pode ser escrito como:

SELECT *
FROM produtos
WHERE estoque != 0;

========================================
10. LIKE
========

LIKE é usado para buscar padrões em textos.

SELECT *
FROM produtos
WHERE nome LIKE '%Bacon%';

O símbolo % representa qualquer quantidade de caracteres.

Exemplos:

LIKE 'X%'

Começa com X.

LIKE '%Bacon'

Termina com Bacon.

LIKE '%Bacon%'

Contém Bacon.

LIKE '_ola'

O símbolo _ representa exatamente um caractere.

Pode encontrar:

Bola
Cola
Mola

========================================
11. IN
======

IN verifica se um valor está dentro de uma lista.

SELECT *
FROM produtos
WHERE id IN (1, 2, 5);

É semelhante a:

SELECT *
FROM produtos
WHERE id = 1
OR id = 2
OR id = 5;

========================================
12. BETWEEN
===========

BETWEEN busca valores dentro de um intervalo.

SELECT *
FROM produtos
WHERE preco BETWEEN 20 AND 40;

Esse intervalo normalmente inclui os valores 20 e 40.

========================================
13. NULL
========

NULL representa ausência de valor.

Não significa:

* zero
* string vazia
* False

Verificar valores nulos:

SELECT *
FROM produtos
WHERE descricao IS NULL;

Verificar valores não nulos:

SELECT *
FROM produtos
WHERE descricao IS NOT NULL;

Não devemos usar:

WHERE descricao = NULL;

========================================
14. ORDER BY
============

ORDER BY ordena os resultados.

Ordem crescente:

SELECT *
FROM produtos
ORDER BY preco ASC;

ASC significa ascending.

Ordem decrescente:

SELECT *
FROM produtos
ORDER BY preco DESC;

DESC significa descending.

Também é possível ordenar por várias colunas:

SELECT *
FROM produtos
ORDER BY preco DESC, nome ASC;

========================================
15. LIMIT
=========

LIMIT limita a quantidade de resultados.

SELECT *
FROM produtos
LIMIT 5;

Buscar os cinco produtos mais caros:

SELECT *
FROM produtos
ORDER BY preco DESC
LIMIT 5;

========================================
16. DISTINCT
============

DISTINCT remove valores repetidos do resultado.

SELECT DISTINCT categoria
FROM produtos;

Exemplo:

Sem DISTINCT:

Hambúrguer
Hambúrguer
Bebida
Bebida

Com DISTINCT:

Hambúrguer
Bebida

========================================
17. COUNT
=========

COUNT conta registros.

SELECT COUNT(*)
FROM produtos;

Contar produtos disponíveis:

SELECT COUNT(*)
FROM produtos
WHERE estoque > 0;

========================================
18. SUM
=======

SUM soma valores.

SELECT SUM(estoque)
FROM produtos;

Pode ser usada para descobrir a quantidade total de itens em estoque.

========================================
19. AVG
=======

AVG calcula a média.

SELECT AVG(preco)
FROM produtos;

========================================
20. MAX E MIN
=============

MAX encontra o maior valor.

SELECT MAX(preco)
FROM produtos;

MIN encontra o menor valor.

SELECT MIN(preco)
FROM produtos;

========================================
21. GROUP BY
============

GROUP BY agrupa registros que possuem valores iguais.

Exemplo de tabela:

nome        | categoria
X-Bacon     | Hambúrguer
X-Salada    | Hambúrguer
Coca-Cola   | Bebida
Suco        | Bebida

Contar produtos por categoria:

SELECT categoria, COUNT(*)
FROM produtos
GROUP BY categoria;

Resultado:

Hambúrguer | 2
Bebida     | 2

Outro exemplo:

SELECT categoria, AVG(preco)
FROM produtos
GROUP BY categoria;

Calcula o preço médio de cada categoria.

========================================
22. HAVING
==========

HAVING filtra resultados depois do GROUP BY.

SELECT categoria, COUNT(*)
FROM produtos
GROUP BY categoria
HAVING COUNT(*) > 2;

Diferença:

WHERE filtra registros antes do agrupamento.

HAVING filtra os grupos depois do agrupamento.

========================================
23. CHAVE PRIMÁRIA
==================

PRIMARY KEY é uma coluna que identifica cada registro de forma única.

Exemplo:

CREATE TABLE produtos (
id INTEGER PRIMARY KEY,
nome VARCHAR(100),
preco DECIMAL(10, 2)
);

O id não deve se repetir.

========================================
24. CHAVE ESTRANGEIRA
=====================

FOREIGN KEY cria uma relação entre tabelas.

Exemplo:

Tabela categorias:

id | nome
1  | Hambúrguer
2  | Bebida

Tabela produtos:

id | nome       | categoria_id
1  | X-Bacon    | 1
2  | Coca-Cola  | 2

categoria_id aponta para o id da tabela categorias.

Exemplo de criação:

CREATE TABLE produtos (
id INTEGER PRIMARY KEY,
nome VARCHAR(100),
categoria_id INTEGER,
FOREIGN KEY (categoria_id)
REFERENCES categorias(id)
);

========================================
25. RELACIONAMENTOS
===================

Um para um:

Um usuário possui um perfil.

Um para muitos:

Uma categoria possui vários produtos.

Uma categoria:

* Hambúrguer

Vários produtos:

* X-Bacon
* X-Salada
* X-Tudo

Muitos para muitos:

Um produto pode aparecer em vários pedidos.

Um pedido pode possuir vários produtos.

Normalmente é criada uma tabela intermediária.

========================================
26. INNER JOIN
==============

JOIN é usado para juntar dados de tabelas relacionadas.

Exemplo:

categorias

id | nome
1  | Hambúrguer
2  | Bebida

produtos

id | nome       | categoria_id
1  | X-Bacon    | 1
2  | Coca-Cola  | 2

Consulta:

SELECT produtos.nome,
categorias.nome
FROM produtos
INNER JOIN categorias
ON produtos.categoria_id = categorias.id;

Resultado:

X-Bacon    | Hambúrguer
Coca-Cola  | Bebida

O INNER JOIN retorna apenas registros que possuem correspondência
nas duas tabelas.

========================================
27. LEFT JOIN
=============

LEFT JOIN retorna todos os registros da tabela da esquerda,
mesmo que não exista correspondência na tabela da direita.

SELECT categorias.nome,
produtos.nome
FROM categorias
LEFT JOIN produtos
ON produtos.categoria_id = categorias.id;

Isso permite mostrar categorias que ainda não possuem produtos.

========================================
28. ALIAS
=========

Alias é um apelido temporário dado a uma tabela ou coluna.

Alias de coluna:

SELECT nome AS produto,
preco AS valor
FROM produtos;

Alias de tabela:

SELECT p.nome,
c.nome
FROM produtos AS p
INNER JOIN categorias AS c
ON p.categoria_id = c.id;

Também pode ser escrito sem AS:

FROM produtos p

========================================
29. CREATE TABLE
================

CREATE TABLE cria uma tabela.

CREATE TABLE produtos (
id INTEGER PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
preco DECIMAL(10, 2) NOT NULL,
estoque INTEGER DEFAULT 0
);

Tipos comuns:

INTEGER
Número inteiro.

VARCHAR(100)
Texto com limite de caracteres.

TEXT
Texto maior.

DECIMAL(10, 2)
Número decimal com precisão.

BOOLEAN
Verdadeiro ou falso.

DATE
Data.

DATETIME ou TIMESTAMP
Data e horário.

========================================
30. RESTRIÇÕES
==============

NOT NULL:

O campo precisa receber um valor.

nome VARCHAR(100) NOT NULL

UNIQUE:

O valor não pode se repetir.

email VARCHAR(150) UNIQUE

DEFAULT:

Define um valor padrão.

estoque INTEGER DEFAULT 0

PRIMARY KEY:

Identifica o registro.

FOREIGN KEY:

Cria relacionamento entre tabelas.

========================================
31. ALTER TABLE
===============

ALTER TABLE modifica uma tabela existente.

Adicionar coluna:

ALTER TABLE produtos
ADD descricao TEXT;

Remover coluna:

ALTER TABLE produtos
DROP COLUMN descricao;

A sintaxe pode variar dependendo do banco utilizado.

========================================
32. DROP TABLE
==============

DROP TABLE remove uma tabela inteira.

DROP TABLE produtos;

Esse comando remove:

* a estrutura
* os registros

Deve ser usado com cuidado.

========================================
33. TRANSAÇÕES
==============

Uma transação agrupa várias operações.

Exemplo:

BEGIN;

UPDATE produtos
SET estoque = estoque - 1
WHERE id = 1;

INSERT INTO pedidos (usuario_id, total)
VALUES (5, 30.00);

COMMIT;

COMMIT confirma as alterações.

ROLLBACK desfaz as alterações.

Exemplo:

BEGIN;

UPDATE produtos
SET estoque = estoque - 1
WHERE id = 1;

ROLLBACK;

Isso é importante quando várias operações precisam funcionar juntas.

Exemplo:

* criar pedido
* criar itens
* diminuir estoque

Se alguma etapa falhar, o sistema pode desfazer tudo.

========================================
34. SQL INJECTION
=================

SQL Injection ocorre quando dados do usuário são colocados diretamente
dentro de uma consulta SQL.

Exemplo inseguro em Python:

cursor.execute(
f"SELECT * FROM usuarios WHERE email = '{email}'"
)

O usuário poderia inserir um código malicioso.

O correto é usar consultas parametrizadas:

cursor.execute(
"SELECT * FROM usuarios WHERE email = ?",
(email,)
)

Em alguns bancos, o marcador pode ser %s:

cursor.execute(
"SELECT * FROM usuarios WHERE email = %s",
(email,)
)

O driver do banco trata o valor separadamente da consulta.

========================================
35. PYTHON COM SQLITE
=====================

Exemplo básico:

import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute(
'''
CREATE TABLE IF NOT EXISTS produtos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL NOT NULL,
estoque INTEGER DEFAULT 0
)
'''
)

cursor.execute(
'''
INSERT INTO produtos (nome, preco, estoque)
VALUES (?, ?, ?)
''',
("X-Bacon", 30.00, 10)
)

conexao.commit()

cursor.execute(
'''
SELECT id, nome, preco, estoque
FROM produtos
'''
)

produtos = cursor.fetchall()

for produto in produtos:
print(produto)

conexao.close()

========================================
36. CURSOR
==========

O cursor é o objeto usado para executar comandos SQL.

cursor.execute(...)

Métodos comuns:

fetchone()

Retorna um registro.

fetchall()

Retorna todos os registros.

fetchmany(numero)

Retorna uma quantidade específica de registros.

========================================
37. COMMIT E ROLLBACK EM PYTHON
===============================

commit confirma alterações:

conexao.commit()

É necessário normalmente depois de:

* INSERT
* UPDATE
* DELETE

rollback desfaz alterações ainda não confirmadas:

conexao.rollback()

========================================
38. SQL E DJANGO ORM
====================

O Django possui um ORM.

ORM significa Object-Relational Mapping.

Ele permite trabalhar com o banco usando classes e objetos Python.

Model Django:

class Produto(models.Model):
nome = models.CharField(max_length=100)
preco = models.DecimalField(
max_digits=10,
decimal_places=2
)
estoque = models.IntegerField(default=0)

A classe representa uma tabela.

Os atributos representam colunas.

Os objetos representam registros.

========================================
39. SELECT NO DJANGO
====================

SQL:

SELECT * FROM produtos;

Django:

Produto.objects.all()

SQL:

SELECT *
FROM produtos
WHERE estoque > 0;

Django:

Produto.objects.filter(estoque__gt=0)

SQL:

SELECT *
FROM produtos
WHERE id = 1;

Django:

Produto.objects.get(id=1)

========================================
40. INSERT NO DJANGO
====================

SQL:

INSERT INTO produtos (nome, preco, estoque)
VALUES ('X-Bacon', 30.00, 10);

Django:

Produto.objects.create(
nome="X-Bacon",
preco=30,
estoque=10
)

Outra forma:

produto = Produto(
nome="X-Bacon",
preco=30,
estoque=10
)

produto.save()

========================================
41. UPDATE NO DJANGO
====================

SQL:

UPDATE produtos
SET preco = 35
WHERE id = 1;

Django:

produto = Produto.objects.get(id=1)

produto.preco = 35

produto.save()

Também pode ser feito diretamente:

Produto.objects.filter(id=1).update(preco=35)

========================================
42. DELETE NO DJANGO
====================

SQL:

DELETE FROM produtos
WHERE id = 1;

Django:

produto = Produto.objects.get(id=1)

produto.delete()

========================================
43. MÉTODOS IMPORTANTES DO ORM
==============================

all()

Retorna todos os objetos.

Produto.objects.all()

filter()

Retorna zero, um ou vários objetos.

Produto.objects.filter(estoque__gt=0)

get()

Espera encontrar exatamente um objeto.

Produto.objects.get(id=1)

create()

Cria e salva um objeto.

Produto.objects.create(
nome="X-Bacon",
preco=30
)

save()

Salva um objeto novo ou modificado.

produto.save()

delete()

Exclui um objeto.

produto.delete()

first()

Retorna o primeiro objeto ou None.

Produto.objects.first()

last()

Retorna o último objeto ou None.

Produto.objects.last()

exists()

Verifica se existe algum resultado.

Produto.objects.filter(
nome="X-Bacon"
).exists()

count()

Conta os resultados.

Produto.objects.filter(
estoque__gt=0
).count()

exclude()

Exclui resultados da consulta.

Produto.objects.exclude(
estoque=0
)

order_by()

Ordena os resultados.

Produto.objects.order_by("preco")

Ordem decrescente:

Produto.objects.order_by("-preco")

========================================
44. LOOKUPS DO DJANGO
=====================

Maior que:

preco__gt=20

Maior ou igual:

preco__gte=20

Menor que:

preco__lt=20

Menor ou igual:

preco__lte=20

Contém texto:

nome__contains="Bacon"

Contém texto ignorando maiúsculas e minúsculas:

nome__icontains="bacon"

Começa com:

nome__startswith="X"

Termina com:

nome__endswith="Bacon"

Está dentro de uma lista:

id__in=[1, 2, 3]

Está dentro de um intervalo:

preco__range=(20, 40)

Valor nulo:

descricao__isnull=True

========================================
45. DIFERENÇA ENTRE GET E FILTER
================================

get():

produto = Produto.objects.get(id=1)

Retorna diretamente um objeto.

Pode gerar erro se:

* nenhum objeto existir
* mais de um objeto existir

filter():

produtos = Produto.objects.filter(estoque__gt=0)

Retorna um QuerySet.

Pode conter:

* zero objetos
* um objeto
* vários objetos

========================================
46. QUERYSET
============

QuerySet é uma coleção de resultados do ORM do Django.

produtos = Produto.objects.filter(estoque__gt=0)

É possível continuar montando a consulta:

produtos = (
Produto.objects
.filter(estoque__gt=0)
.exclude(preco__lt=10)
.order_by("-preco")
)

O Django transforma essa consulta em SQL.

========================================
47. MIGRAÇÕES NO DJANGO
=======================

Quando um model é criado ou alterado:

python manage.py makemigrations

Cria os arquivos de migração.

python manage.py migrate

Aplica as alterações no banco.

Resumo:

models.py
↓
makemigrations
↓
arquivo de migração
↓
migrate
↓
banco atualizado

========================================
48. RESUMO PARA ENTREVISTA
==========================

SQL é a linguagem usada para trabalhar com bancos de dados relacionais.

As operações fundamentais são:

SELECT
Buscar dados.

INSERT
Adicionar dados.

UPDATE
Atualizar dados.

DELETE
Excluir dados.

WHERE filtra registros.

ORDER BY ordena resultados.

GROUP BY agrupa registros.

JOIN junta tabelas relacionadas.

PRIMARY KEY identifica um registro de forma única.

FOREIGN KEY cria um relacionamento entre tabelas.

No Django, o ORM permite realizar essas operações usando objetos Python.

Exemplo:

Produto.objects.all()

equivale aproximadamente a:

SELECT * FROM produtos;

Mesmo usando ORM, entender SQL é importante para:

* compreender o banco de dados
* criar boas consultas
* trabalhar com relacionamentos
* identificar problemas de desempenho
* entender o que o ORM faz internamente
  """
