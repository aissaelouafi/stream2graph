# Stream2Graph 
**Stream2Graph : A Dockerized Data Pipeline for Stream-based Analytics over Knowledge Graph**
Authors, M. Barry, Aissa Elouafi, J. Montiel, A. Bifet, R. Chiky, V. Tran, A. Nobial.

## Features and Services to build an Automated Data Pipeline with Stream2Graph Components
![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Features_Stream2Graph_To_Build_DataPipeline.png)

## Architecture of Stream2Graph to adress streams-based and Graph-based online machine learninge use-cases
![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Architecture_Stream2Graph_Data_Pipelines.png)

## Services used 

The used dockerized service are :
- Liner and Graph Data Generators
- Kafka broker (Real-time Events & Streams ingestion)
- Flink for streams preprocessing and incremental feature engineering (sliding windows
- River (Online and Incremental Learning)
- Graph Data bases Neo4j and TigerGraph
- Zookeper 
- Logs generator image to generate logs 
- Fake Data generator (Graph and Logs)

## Repository Structure (Folders & File descriptions)

### Features optional 
- Graph and Linear Data generator
- Unstructured Data Parsing (Logstach)
- Streams generator (from multiple data sources)
- Strams ingestion (Apache Kafka)
- Graph storage (Apache AGE + PostgreSQL, Neo4j)
- Big graph storage (JanusGraph, TigerGraph)
- Graph Algorithms (Scikit-network, GraphTools, Neo4j, TigerGraph )
- Distributed Graph Processing (GraphFrames, Apache Gelly) 
- Online and Incremental Learning (River)

### How to run set up or run the data pipeline using Docker or Stream 2 Graph ?

To run the `stream2graph` pipeline, 
- copy the `logs` folder (Data) to the working directory 
- run : `docker-compose up -p` to build the `logs-generator` images install required services.

## Contributing 

## Docker structure

### References on Docker

**Docker is a tool designed to make it easier to create, deploy, and run applications by using containers**. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code. [More about docker for debveloppement](https://dev.to/amoniacou/what-is-docker-why-is-it-important-and-necessary-for-developers-part-i-39e5). Some applications of docker can be founed [here](https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html). 

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about [all the features of Compose, see the list of features.](https://docs.docker.com/compose/#features) 

Compose works in all environments: production, staging, development, testing, as well as CI workflows. You can learn more about each case in [Common Use Cases](https://docs.docker.com/compose/#common-use-cases).

Using Compose is basically a three-step process:

- Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
- Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
- Run docker compose up and the Docker compose command starts and runs your entire app. You can alternatively run docker-compose up using the docker-compose binary.
