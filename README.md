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
Foi definido como objeto de estudo a **MANUFATURA**. Apesar de ser um tema bastante amplo conseguir bases de dados se mostrou um desafio, já que dificilmente uma empresa abriria mão de bases de dados a um terceiro. Buscamos então dados publicos e governamentais dentre eles dados históricos da **CNI**(Confederação Nacional da Indústria) e dados de reclamação disponibilizados pelo **PROCON** a nível nacional.



​	



## Objetivo <a name ="objective">

Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos





## Projeto <a name ="projeto">

Só agora com a definição mais precisa do escopo de projeto fica mais fácil definir o  *stack* de ferramentas que vai nos ajudar...{}



### 		1.Stack <a name ="stack">

<img src="./.img/stack.png" alt="our stack of technology used">

  - Hadoop(HDFS/YARN) - 

    > Sistema de arquivos distribuído com alta tolerância a falha com alta disponibilidade e baixo custo de implementação. Apesar de ter entrado em desuso muito por conta da mudança de paradigma da Engenharia de Dados ter se voltado ao PaaS(Plataform as a Service), o **HDFS** ainda vê os seus dias de gloria como um Data Lake de baixo no cenário on-premise e é ele que usaremos como nosso **Data Lake**.

    > **YARN** é simplesmente o gerenciador de recursos e jobs, componente essencial do ecossistema Hadoop para processamento distribuído.



  - PySpark(Spark) -

    > Nada mais é que uma **API python** para trabalhar sobre o Spark. O **Spark** por sua vez é uma *engine* de processamento de dados em larga escala que muito mais rápida que o Haddop. Parte da sua velocidade advém principalmente do fato que o Spark faz uso de armazenamento em **memória ram** o que por si só já lhe garante ampla vantagem sobre seu irmão mais novo. 
    
    

- Jupyter Notebook -

  > Ferramenta preferida na análise mais refinada de dados. O **Jupyter** pode ser configurado para realizar queries e tratamentos em cima da engine Spark se integrando muito bem ao ecossistema Apache/Hadoop/Spark e com uma infinidade de bancos SQL/NoSQL.



- 



## Trabalhos futuros <a name ="future_works">



















