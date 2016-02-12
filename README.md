Implementação de algoritmos de substituição de páginas de memória
==

Algoritmos implementados:

* First-in, Firts-out (FIFO)
* Algoritmo Otimo (OTM)
* Least Recently Used (LRU)

Formato do arquivo de entrada:

<pre>
  <code>
  4
  1
  2
  3
  4
  1
  2
  5
  1
  2
  3
  4
  5
  </code>
</pre>

A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória RAM e, em seguida, a sequência de referências à memória.


Formato da saída:

<pre>
  <code>
  FIFO 10
  OTM 6
  LRU 8
  </code>
</pre>

A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a utilização de cada um deles.
