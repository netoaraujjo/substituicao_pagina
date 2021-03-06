#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FIFO:
    """Algoritmo First-in First-out (FIFO) para substituicao de paginas na memoria RAM"""

    def execute(self, qtd_quadros, referencias):
        """
        Executa o algoritmo de substituicao de paginas FIFO. Recebe como
        parametros a quantidade de quadros e a lista de paginas referenciadas.
        """
        # Inicializa os valores de miss
        miss = 0 # Quando a pagina referenciada nao esta na memoria

        quadros = [] # Quadros da memoria

        # Percorre a lista de paginas referenciadas
        for ref in referencias:
            if ref not in quadros:
                miss += 1 # incrementa o numero de paginas faltantes

                # Se todos os quadros estiverem ocupados remove a pagina mais antiga
                if len(quadros) == qtd_quadros:
                    quadros.pop(0)

                # Adiciona a nova pagina
                quadros.append(ref)

        # Retorna o numero de paginas nao encontradas na memoria RAM
        return miss
