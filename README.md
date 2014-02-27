Jogo de Snake
=============

Regras
------

* A cobra não pode se colidir com ela mesma ou com a parede
* A cada vez que que ela 'come' ela cresce
* A cada dez comidas a cobra fica mais rápida e aumenta em uma unidade
  o número de comidas presentes no jogo
* A pontuação depende da velocidade da cobra

Como está divido
----------------

* Game(): classe responsável por gerenciar os objetos do jogo e renderizá-los
* Snake(): classe da cobrinha que o jogador controla na tela
* Food(): classe responsável pelas comidas
* Messages(): classes responsável pelas mensagens, como a de pontuação(atual
  e máxima) e o número de mortes(sempre da sessão atual)