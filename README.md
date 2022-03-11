<p align="center">
    <h1 align="center"> Artesanato de dados (0.9α)</h3>
</p> 

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)





<img src="./.img/etl_arch.png" alt="classic ETL template">

> O intuito principal desse repositório é desenvolver, demonstrar e documentar parte do conhecimento que adquiri através de estudos sobre a área da Ciência/Engenharia de dados. Durante o decorrer desse projeto vamos passar por todas as etapas do fluxo do Big Data, da sua ingestão inicial de dados até a produção dos insights e propostas de intervenção.



----





- [Introdução](#introduction)

- [Objetivo](#objective)

- [Projeto](#projeto)
  
  - 1.[Stack](#stack)
    
  -   2.[pch](#pch)
  -   3.[pch](#pch)
  -   4.[pch](#pch)

  

- [Trabalho futuro](#future_works)



-







## Introdução <a name="introduction"></a>
Foi definido como objeto de estudo a **MANUFATURA**. Apesar de ser um tema bastante amplo, conseguir bases de dados se mostrou um desafio, já que dificilmente uma empresa abriria mão de bases de dados a um terceiro. Tendo em vista o desafio que encontramos ao procurar fontes de dados mais voltadas a *players* do mercado, passamos a buscar, então, dados públicos e governamentais, dentre eles dados históricos da **CNI** (Confederação Nacional da Indústria) e dados de reclamações disponibilizados pelo **PROCON** a nível nacional.



###### 

<img src="./.img/manu_asset.png" alt="our stack of technology used">



​	



## Objetivo <a name ="objective">

Com o processamento e análise desses dados buscamos: 

1. Qualificar a persona que mais abre reclamação.
2. Identificar quais os problemas no pós-venda 
3. Propor *insights* .



## Projeto <a name ="projeto">

Só agora com a definição mais precisa do escopo de projeto fica mais fácil definir o  *stack* de ferramentas que utilizaremos.







### 		1.Stack <a name ="stack">

<img src="./.img/stack.png" alt="our stack of technology used">

  - **Hadoop(HDFS/YARN) -** 

    > Sistema de arquivos distribuído com alta tolerância a falha, além de alta disponibilidade e baixo custo de implementação. Apesar de ter entrado em desuso muito por conta da mudança de paradigma da Engenharia de Dados ter se voltado ao PaaS (Plataform as a Service), o **HDFS** ainda vê os seus dias de gloria como um Data Lake de baixo custo no cenário on-premise e é ele que usaremos como nosso **Data Lake**.

    
    
    > **YARN** é simplesmente o gerenciador de recursos e jobs, componente essencial do ecossistema Hadoop para processamento distribuído.



  - **PySpark(Spark) -**

    > Nada mais é que uma **API python** para trabalhar sobre o Spark. O **Spark**, por sua vez, é uma *engine* de processamento de dados em larga escala, sendo muito mais veloz que o Hadoop M/R. Parte da sua velocidade advém principalmente do fato que o Spark faz uso de armazenamento em **memória** o que lhe garante ampla vantagem sobre seu irmão mais novo. 
    
    
    
    

  - **Jupyter Notebook -**

    > Ferramenta principal do Cientista de Dados. O **Jupyter** pode ser configurado para realizar *queries* e *tratamentos* fazendo uso da engine Spark e se integra muito bem ao ecossistema Apache/Hadoop/Spark.





  - **Oracle -**

    > SGBD número 1 a nível mundial. Famoso pela sua confiabilidade, velocidade e suporte é o  queridinho no eco sistema empresarial em todo mundo. É o destino final de nossos dados.



  - **NiFi** -

    > Uma ferramenta para automação e roteamento de forma gráfica, escalonável e simples para movimentação e transformação de dados pouco complexos. É uma excelente ferramenta para iniciar pelo baixa curva de aprendizado.

    



## Trabalhos futuros <a name ="future_works">



















