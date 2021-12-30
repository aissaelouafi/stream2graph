# Stream2Graph 

**Stream2Graph: Automated Data Pipeline for Streams-based Learning from Knowledge Graphs**
Authors, M. Barry, A. El Ouafi, J. Montiel, A. Bifet, R. Chiky, V. Tran, A. Nobial.

**Abstract**
Machine learning from industrial data is a challenging task since 1) input data is high-dimensional, 2) heterogeneous data is continuously generated from Information Systems (IS), and 3) data is continuously evolving (users activity, transaction, IT operation or network traffic). To tackle these challenges, we apply a knowledge graph and data stream approach, motivated by an industrial application in large-scale telecommunication network within a major banking group serving millions of customers (BNP Paribas). In this paper, we propose Stream2Graph, a new system based on a domain-agnostic approach to build and update an Enterprise Knowledge Graph (EKG).
 We provide the new Stream2Graph framework as a set of automated services, that can be combined to set up a specific Dockerized data pipeline (based on Apache Kafka and Flink) for use-cases data engineering environment. The build-in functionalities can be used for incremental learning and processing of multi-modality data streams within a dynamic knowledge graph database for further graph-based and AI analytics. Stream2Graph design is suited to easily run and deploy graph-based applications on streaming data. We demonstrate the viability and effectiveness of our solution through an industrial application on a large-scale telecommunication system.
 
## Features and Services to build an Automated Data Pipeline with Stream2Graph Components
![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Features_Stream2Graph_To_Build_DataPipeline.png)

## Architecture of Stream2Graph to adress streams-based and Graph-based online machine learninge use-cases
![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Architecture_Stream2Graph_Data_Pipelines.png)

## Industrial Challenges for Data Engineering and How Stream2Graph Address them ?
![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Industrial_Challenges_Stream2Graph_Features.PNG)


## Services used 

The used dockerized service are :
- Streams **Data Generators (Linear and Graph)** : Python object to generate raw data, many data sources can be used to simulate the heterogeneous aspect of data used in production.
- **Kafka broker (Real-time Events & Streams ingestion)** : Apache kafka broker for data transport in real time, the kafka topic is created by default and can handle many hundred thousand of events by minute. In this docker environment, the kafka is installed in standalone mode. We can setup a kafka cluster to scale up the application. 
- **Flink for streams preprocessing and incremental feature engineering** (sliding windows) : Apache flink is used for data preprocessing and incremental feature engineering in real time, the logs aggregations flink application cconsume data in real time from a Kafka topic and produce structured / aggregated data in a another kafka topic. The main advantage of using flink is his capacity to scale up easily, many parameters can be modified on docker file to add workers and scale up the application, the Flink docker image can be modified : `Dockerfile.flink`
- **River (Online and Incremental Learning)** : Python framework for online and incremental learning, we consume structured data from a kafka topic and we train an online machine learning model for anomalies detection. Data are structured / aggregated using Apache Flink, the output results can be stored on a structured / semi-structured database like PostgreSQL or Elasticsearch, the River docker image can be modified : `Dockerfile.river`
- **Graph Data bases** Neo4j and TigerGraph
- Zookeper 
- Logs generator image to generate logs 
- Fake Data generator (Graph and Logs)


### How to run set up or run the data pipeline using Stream2Graph ?

To run the `stream2graph` pipeline, 
- copy the `logs` folder (Data) to the working directory 
- run : `docker-compose up -p` to build the `logs-generator` images install required services.
- For specific needs, you can modify the aggregation strategy flink script `events_aggregation/events_aggregation.py`, the environment variable used are setted in the `docker-compose.yml` file.
- The online learning model can be also modified in the file `online_learning/online_classification.py`, the input and output topic are setted in the `docker-compose.yml` file. 

The `neo4j` browser is exposed on : `localhost:7474`, The `taskmanager` is exposed on : `localhost:8088`


### References on Docker

**Docker is a tool designed to make it easier to create, deploy, and run applications by using containers**. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code. [More about docker for debveloppement](https://dev.to/amoniacou/what-is-docker-why-is-it-important-and-necessary-for-developers-part-i-39e5). Some applications of docker can be founed [here](https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html). 

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about [all the features of Compose, see the list of features.](https://docs.docker.com/compose/#features) 

Compose works in all environments: production, staging, development, testing, as well as CI workflows. You can learn more about each case in [Common Use Cases](https://docs.docker.com/compose/#common-use-cases).

Using Compose is basically a three-step process:

- Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
- Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
- Run docker compose up and the Docker compose command starts and runs your entire app. You can alternatively run docker-compose up using the docker-compose binary.

###  Optional features (services) to add or activate to set up a specific data engineering pipeline to adress use-cases 
- Graph and Linear Data generator
- Unstructured Data Parsing (Logstach)
- Streams generator (from multiple data sources)
- Strams ingestion (Apache Kafka)
- Graph storage (Apache AGE + PostgreSQL, Neo4j)
- Big graph storage (JanusGraph, TigerGraph)
- Graph Algorithms (Scikit-network, GraphTools, Neo4j, TigerGraph )
- Distributed Graph Processing (GraphFrames, Apache Gelly) 
- Online and Incremental Learning (River)
- Results visualization, Analytics & Monitoring (Kibana)
