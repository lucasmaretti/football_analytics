## <img src="https://imageio.forbes.com/specials-images/imageserve/5faffd4438fefe6a79002260/0x0.png?format=png&width=1200" class="center" width="600"/>

## Repositório para estudo da aplicação de ciência de dados no futebol

Caso você seja novo neste tema da ciência de dados, recomendo ler os seguintes artigos: https://medium.com/zeroeum/footballanalytics/home


## Conteúdo

1. [Introdução](#introduction)
2. [Data description](#data)
3. [Objetivos e métricas](#statement)
4. [Análise Exploratória](#wrangling)
5. [Modelagem](#modelling)
6. [Conclusões](#conclusions)
7. [Licenciamento e Reconhecimentos](#licensing)

## Introdução <a name="introduction"></a>

Este projeto e repositório surgiu a partir do trabalho de conclusão da disciplina MAI5001 (Ciência de dados) dos alunos [Lucas Maretti](https://www.linkedin.com/in/lucas-maretti/) e [Gabriel Bortoli](https://www.linkedin.com/in/gbortoli/) do programa de mestrado profissional do MECAI (USP). 
A aplicação de técnicas de ciência de dados ao futebol é ainda um tema pouco explorado no Brasil. Com este projeto e disponibilização do código e do repositório esperamos fomentar mais desenvolvimentos nesse tema em português e no Brasil

## Descrição dos dados <a name="data"></a>

Este projeto utilizou dados da Wyscout disponibilizados em 2019 em artigo publicado na [revista Nature](https://www.nature.com/articles/s41597-019-0247-7) pelos pesquisadores Pappalardo, L., Cintia, P., Rossi, A. et al. e pode ser encontrado neste [link](https://figshare.com/collections/Soccer_match_event_dataset/4415000/5).

Especificamente para este projeto utilizamos dados de **eventos** (*events.json*), que referem-se à todas as ações que ocorreram na bola, bem como metadados de cada partida (*matches.json*) e dos jogadores (*players.json*). Outro tipo de análise importante nesse campo de Football Analytics é utilizar os dados de **tracking**.

## Objetivos e métricas <a name="statement"></a>

**Objetivo**

O objetivo ao final do processo de modelagem dos dados foi obter um modelo de Expected Goals (xG)

A definição de xG é a probabilidade de que em um dia típico de futebol um chute particular de uma determinada localização resultar em um gol. Costuma ser baseado em medidas tomadas de muitos chutes dentro de uma mesma liga e temporada, ou agregando-se dados de diferentes ligas (estratégia usada neste projeto).
Para mais informações sobre este tema recomendo assistir a este [video](https://www.youtube.com/watch?v=Xc6IG9-Dt18). Se quiser entrar em maiores detalhes no tema, recomendo assistir a este [vídeo](https://www.youtube.com/watch?v=310_eW0hUqQ) na sequência

**Métricas**

Para algoritmos de classificação, a função de custo padrão usada é a perda logarítmica. Para modelos com output binário, como é o caso do modelo de expected goals, a função log loss é dada por:

$$\mathcal{L}(\hat{y}, y) = - \frac{1}{n}\sum_{i=1}^{n} y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)$$

em que $\hat{y}$ é probabilidade prevista da classe positiva, , $y$ é o valor real (0 ou 1), e $n$ é o número de amostras no dataset.

Embora a maioria das métricas de avaliação para problemas de classificação envolva a análise da capacidade preditiva do modelo em várias situações usando métricas tradicionais como precisão e recall, essa abordagem não é ideal ao problema de modelagem de xG. Isso ocorre porque resultado desejado do modelo é a probabilidade de que um chute específico seja gol, e não uma previsão de se um chute é um gol (ou seja, uma saída binária). Por este motivo, este trabalho usa como principal métrica comparativa de modelos a própria perda logarítmica , em que quanto menor essa pontuação, melhor o algoritmo de classificação estima com precisão a probabilidade de gol.

### Análise Exploratória e hipóteses levantadas <a name="wrangling"></a>
A partir das análises gráficas iniciais, em que se avaliou a distribuição da frequência de chutes ao gol, estratificando entre gols/não-gols, duas hipóteses principais foram levantadas: qual era a relação entre distância e ângulo do chute e a probabilidade de se marcar um gol?

### Modelagem <a name="modelling"></a>
Foi escolhida uma divisão dos dados de treinamento e teste em uma proporção de 75\% e 25\%, respectivamente. O *scaling* das features foi feito usando valores mínimos e máximos e a validação cruzada no treinamento dos modelos usando-se 5 *folds* em todos os treinamentos realizados, incluindo-se o processo de otimização de hiperparâmetros, em que se utilizou a técnica de *grid search*.

A título de referência como baseline para a métrica de perda logarítmica para comparar performance entre os modelos, um modelo usando apenas o valor médio esperado de gols (10.17\%) foi usado e obteve um resultado de 0.333 de log-loss (perda logarítmica). Depois foi testado um modelo de Regressão Logística apenas com as features de distância e ângulo em relação ao gol, com resultado de log-loss de 0.288. Em seguida testou-se um modelo de Regressão Logística usando-se todas as features com otimização de hiperparâmetros, com resultado de log-loss de 0.281. E por fim um de Random Forest Classifier, cujo melhor resultado foi de 0.280. 

## Conclusões <a name="conclusions"></a>
Os principais objetivos deste projeto foram adicionar ao conjunto limitado de pesquisas sobre expected goals em língua portuguesa, ainda mais tendo o futebol influência em diversos aspectos socio-econômicos da sociedade brasileira, além de comparar o desempenho de modelos frente a pesquisas anteriormente realizadas sobre o tema em outros países com dados da Wyscout, que tornou a referência para este tipo de análise.
O modelo ótimo construído neste projeto mostrou-se competitivo quando comparado com resultados de outros estudos dentro da literatura existente. As variáveis mais importantes foram ângulo e distância do chute, porém foi possível obter insights interessantes sobre como jogadas de bola parada e contra ataque tendem a levar a situações em que a probabilidade de um chute resultar em gol aumentam. 

Embora este estudo tenha produzido resultados interessantes, ele tem algumas limitações que podem ser abordadas em trabalhos futuros. A principal está relacionada a feature engineering. Há uma elevada gama de variáveis que podem ser criadas e calculadas para complementar o dataset, além das que já foram feitas. Por exemplo, Mead et al [1] cita o valor do jogador de acordo com o site TransferMarket como a feature com maior impacto em seus modelos. Este resultado é bastante interessante e pode explicar por que times com grande poder aquisitivo tendem a ter melhores resultados na métria de xG e serem mais competitivos.

Além disso não foi utilizado dados posicionais na modelagem, devido à sua inexistência para o dataset em questão. Caso contrário poderíamos criar features como posição do goleiro na hora do chute e avaliar se haviam defensores na trajetória do chute, enriquecendo a análise. Apesar dessas limitações, os resultados produzidos neste estudo comprovam que a expectativa de gols pode trazer grande valor para analistas, comissões técnicas e torcedores ao proporcionar uma nova forma de ver um jogo sujeito a elevadas incertezas e aleatoriedades. E os principais motivos para isso são: capacidade preditiva do desempenho de equipes melhor do que simplesmente olhar número de gols marcados, principalmente devido ao fato de que o modelo de xG baseia-se em chutes, que ocorrem em número muito maior do que gols durante as partidas. Além disso, um bom modelo de xG pode ajudar aos jogadores em sua tomada de decisão sobre quando arriscar um chute ao saber as localizações do campo em que a probabilidade de marcar aumentam.


## Licenciamento e Reconhecimentos <a name="licensing"></a>

Dados fornecidos pela Wyscout
[Soccermatics](https://soccermatics.readthedocs.io/en/latest/) e [Friends of Tracking Data](https://www.youtube.com/@friendsoftracking755) pelos excelentes materiais introdutórios sobre o tema de football analytics

[1] Mead, J., O’Hare, A., and McMenemy, P. (2023). Expected goals in football: Improving model performance and demonstrating value. PLoS ONE, 18(4).

