### Case_covid
Este case foi desenvolvido com o intuito de utilizar as ferramentas do Google Cloud
Platform (GCP) para a sua solução. 

ETAPA 1 - Cloud Function e Cloud StorageFazer a ingestão dos dados no Storage e depois via Cloud Function adicionar
os dados a uma tabela no Bigquery.

### 1 - Crie um Bucket no Cloud Storage chamado upload_covid_data, este
### bucket será utilizado para receber os arquivos baixados anteriormente.

![image](https://github.com/jucafernando/case_covid/assets/21082881/25095b54-4c52-4d9f-9621-e4156b1eafc7)

Na imagem, podemos ver que foi criado o bucket conforme foi solicitado


### 2 - Crie uma Cloud Function que carregue o arquivo adicionado ao
bucket, criado no passo anterior, ao término do upload do arquivo (gatilho de
atualização/adição de um determinado arquivo no bucket), faça a carga dos
dados para uma tabela (conjunto de dados) com os respectivo nomes dos
arquivos (caso e obito_cartorio) dentro de um dataset chamado covid no
Bigquery.
NOTA: Os dados devem ser decodificados corretamente e a tabela deve ser sobre-escrita(não
pode haver duplicidade de dados) em caso de um novo arquivo para: caso.csv ou
obito_cartorio.csv ser adicionado ao bucket.
Disponibilizar o código da Cloud function e as saídas dos logs da função.

![image](https://github.com/jucafernando/case_covid/assets/21082881/a112538d-91e3-40d1-928a-87396cd57af0)
![image](https://github.com/jucafernando/case_covid/assets/21082881/09a6423d-ba55-4b31-966a-7ae6ea2b0b90)

![image](https://github.com/jucafernando/case_covid/assets/21082881/2d249188-e43e-48d2-a916-c8e920aefb63)

Explicação sobre o código:

Primeiramente, preparei o arquivo requeriment com as bibliotecas necessárias para o sucesso do código. 

Sobre as bibliotecas: 

pandas: biblioteca com muitas opções importantes para manipulação de dados e no caso desse código, precisei utuliza-lo para 
criar dataframes, que recebeu as bases de dados, passou por tratamento de nomes de colunas e foi importante para a exportação 
desses dados. 

gcsfs: Precisei dessa biblioteca para interagir com o Google Cloud Storage por meio do sistema de arquivos do Python, permitindo manipular arquivos como se estivessem em um sistema de arquivos local. Dessa forma, eu consegui enviar a base de dados para o bigquery. 

google-cloud-bigquery: A  biblioteca bigquery é fundamental pois sem ele, não seria possível informar ao cloud functions que eu preciso enviar os dados até o bigquery.

google-cloud-bigquery-storage>=2.4.0: Similar à anterior, esta biblioteca fornece acesso à API de armazenamento do BigQuery, otimizando a leitura de grandes conjuntos de dados.

google-cloud-storage: Como google-cloud-storage usada para interagir com o serviço de armazenamento de objetos em nuvem oferecido pela GCP, é uma biblioteca fundamnetal pois é por ela que eu consegui apontar pra onde eu queria que meus dados fossem armazenados. 

Essas foram as bibliotecas que precisei usar para realizar a função que busque os dados no storage e disponibilze no bigquery. 

## ETAPA 2 - Bigquery
Utilizando o ambiente do Bigquery e a linguagem SQL, responda os seguintes
questionamentos do cliente sobre os dados:
NOTA: Para cada uma das perguntas descritas abaixo apresentar o código SQL e o resultado
(dados) gerado pela consulta.

1 - Qual o total de Casos Confirmados?

![image](https://github.com/jucafernando/case_covid/assets/21082881/7d7dbe4f-4622-42c3-ac31-23c0d3f5682a)
![image](https://github.com/jucafernando/case_covid/assets/21082881/c9729cfd-b3b7-4a65-9f66-db8c7c6cedcf)
![image](https://github.com/jucafernando/case_covid/assets/21082881/bd8fcd63-7867-4191-8bfd-4a4e68b5303d)

2 - Qual a quantidade de Casos confirmados por Estado, classificando os 5
primeiros estados com mais casos?

![image](https://github.com/jucafernando/case_covid/assets/21082881/4bc18812-4433-44ec-b060-0a6d7960f241)

Essa query é semelhante a primeira com a diferença de que eu precisei ordenar os dados pela coluna agregada confirmed_cases.

3 - Qual a Letalidade em % (mortes/casos confirmados) por Estado,
classificando os 5 primeiros estados com maior letalidade ?

![image](https://github.com/jucafernando/case_covid/assets/21082881/33ad271c-324b-441d-ad00-047e051bad98)

Essa query me deu um pouco de trabalho, devido ao que expliquei na primeira query. Eu queria agrupar os dados apenas por uma 
coluna e fazer aparecer no resultado da query, mais duas colunas, totalizando três colunas. Tive fazer uma coluna de agragação
contendo o calculo de pocentagem de letalidade e somar as duas colunas(mortes/casos), agrupando pelo campo de estado e ordenando 
pela coluna de agregação letalidade_porcentagem.

4 - Qual a Taxa de Óbitos por cada mil habitantes, por estado , listar os 5
primeiros estados com maior concentração de óbitos por cada mil habitantes
(população) ?

![image](https://github.com/jucafernando/case_covid/assets/21082881/94809d0c-fecf-4192-97e7-53c0033ddf1f)

Por fim, eu realizei a query de busca pela taxa atual de de obtos por habitantes, utilizando a soma total 
da coluna de concentração de habitantes e agrupar separando por estado, fazendo o ranking dos cinco primeiros. 

A maioria das análises solicitavam um ranking dos 5 primeiros, de acordo com a informação solicitada.

Encerro por aqui as análises. Os códigos e querys estão disponpveis em arquivos nesse repositório. 
Em breve, continuarei mais duas análises e farei um dash no Google Studio, mas primeiro preciso de 
um novo pc, pois o meu infelizmente não aguentou. 
Nos vemos na próxima. 






