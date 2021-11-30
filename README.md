# Stream2Graph
A Docker-based Data Pipeline to Enhance Streams Learning and Graph Analytics Over Knowledge Graph. Authors, M. Barry, Aissa Elouafi, J. Montiel, A. Bifer, R. Chiky, V. Tran, A. Nobial.

### Data pipeline architecture 

How to process streams events from Kafka and update a knowledge graph data based stored in NEO4J ?
![alt text](https://neo4j.com/labs/kafka/4.0/_images/unwind-consume.png)

Overall of Stream2Graph approach to enhance Streams and Graph-based Online (machine) Learning.
Each block is an independant tool to allow flexibility of the data pipeline which can be extended for further analytics.

![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Stream2Graph_overview.png)

### Services used 
The used dockerized service are :
- Neo4j database
- Kafka broker
- Zookeper 
- Logs generator image to generate logs 

### How to run the the data pipeline with Docker ?

To run the `stream2graph` pipeline, you need to copy the `logs` folder (Data) to the working directory and run : `docker-compose up -p` to build the `logs-generator` images and install required services.


### References on Docker

**Docker is a tool designed to make it easier to create, deploy, and run applications by using containers**. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code. [More] (https://dev.to/amoniacou/what-is-docker-why-is-it-important-and-necessary-for-developers-part-i-39e5). Some applications of docker can be founed [here](https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html). 

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about [all the features of Compose, see the list of features.](https://docs.docker.com/compose/#features) 

Compose works in all environments: production, staging, development, testing, as well as CI workflows. You can learn more about each case in [Common Use Cases](https://docs.docker.com/compose/#common-use-cases).

Using Compose is basically a three-step process:

**Define your app’s environment with a Dockerfile so it can be reproduced anywhere.

**Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.

**Run docker compose up and the Docker compose command starts and runs your entire app. You can alternatively run docker-compose up using the docker-compose binary.
