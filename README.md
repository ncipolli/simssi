## SIMSSI
### SIMULAÇÃO DE IMPLEMETAÇÃO DE SISTEMAS SEMAFÓRICOS INTELIGENTES

-----------------------------------------
### Autora
O presente projeto foi desenvolvido como trabalho de graduação em Engenharia da Computação pela aluna Natália Cipolli de Freitas no ano de 2021.
<br><br>
Obs.: Por conta da pandemia, não foi possível realizar coleta de dados em campo, por esse motivo todos os dados utilizados foram gerados artificialmente com base em informações recolhidas nos sites da DETRAN e CETSP.

-----------------------------------------

## FUNCIONAMENTO

### Geração de Dados
Utilizando a função random, serão gerados duas listas, a primeira
para a geração de valores de volume de veículos nas vias e a segunda
para condições especiais como semáforo de pedestres, passagem de
veículos especiais ou situações de emergência.

### Atribuição de Valores
Cada avenida é uma lista que contém um valor de volume, condição, e valor de peso.

### Cálculo / Lógica
* Cada dupla de via deve conter o mesmo ciclo semafórico.
* O cálculo deve considerar os valores individuais das vias e depois considerá-las em conjunto.
