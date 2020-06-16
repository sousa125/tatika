# Tatika
### Serviço utilizado para consultar informações sobre ações da bolsa de valores por meio da API Yahoo Finance

O serviço utiliza a API Yahoo Finance para obter dados sobre as ações, para então analisar elas utilizando a biblioteca pandas.
Uma das principais análises feita pelo serviço é a taxa de variação de uma ação por dia, que exibe de forma estatística a a taxa de ocorrência de uma determinada variação nos dias análisados.

#### Exemplo de análise com a ação BKBR3

DATA          | ABERTURA | MÍNIMO | MÁXIMO 
------------  | -------- | --------- | ----- 
26/05/2020	  | 10.70	| 10.70 | 11.94
25/05/2020	  | 9.88	| 9.47	| 10.29
22/05/2020	  | 9.81  | 9.17  | 10.03	 
21/05/2020	  | 9.89	| 9.71  | 10.24 
20/05/2020	  | 9.95	| 9.59  | 9.95 
19/05/2020	  | 9.47	| 9.36  | 9.97
18/05/2020	  | 9.07	| 8.82  | 9.84	
15/05/2020	  | 8.20	| 8.19  | 8.93
14/05/2020	  | 8.15	| 8.03	| 8.61
13/05/2020	  | 8.90	| 8.17	| 9.08	


Nesse exemplo temos dados de 10 dias da ação BKBR3. <br>
Após algumas manipulações utilizando o pandas, temos o seguinte resultado:

Em 75% dos dias analisados a ação chega a valorizar 2.07% e/ou desvalorizar 1.56% <br>
Em 50% dos dias analisados a ação chega a valorizar 3.94% e/ou desvalorizar 3.25% <br>
Em 25% dos dias analisados a ação chega a valorizar 7.51% e/ou desvalorizar 6.30% <br>

Com isso o investidor tem uma noção de como costuma ser o comportamento da ação em análise.


