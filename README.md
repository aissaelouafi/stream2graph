# Stream2Graph
Stream2Graph 

## Overview of materials

### Data pipeline architecture 

How to process streams events from Kafka and update a knowledge graph data based stored in NEO4J ?
![alt text](https://neo4j.com/labs/kafka/4.0/_images/unwind-consume.png)

Overall of Stream2Graph approach to enhance Streams and Graph-based Online (machine) Learning 

![alt text](https://github.com/aissaelouafi/stream2graph/blob/master/Stream2Graph_overview.png)

### Services used 
The used dockerized service are :
- Neo4j database
- Kafka broker
- Zookeper 
- Logs generator image to generate logs 

### How to run the the data pipeline with Docker ?

To run the `stream2graph` pipeline, you need to copy the `logs` folder (Data) to the working directory and run : `docker-compose up -p` to build the `logs-generator` images and install required services.

## Docker Installation and Configuration Requirements

### Docker Desktop for Mac
Go to the Docker Desktop for Mac page https://store.docker.com/editions/community/docker-ce-desktop-mac and follow the instructions to download, install, and run Docker.

### Adjusting Docker Resources
After installing Docker, you must increase the available resources so that Docker is able to launch the Strea2Graph system. The system requires at least 2 GB of available disk space and 2 GiB of available RAM.
To adjust the available resources, click the Docker icon in the menu bar and select Preferences. On the Settings screen, select Resources.

