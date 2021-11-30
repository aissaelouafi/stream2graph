# stream2graph
Stream2Graph 

## Docker Installation and Configuration Requirements
### Docker Desktop for Mac
Go to the Docker Desktop for Mac page https://store.docker.com/editions/community/docker-ce-desktop-mac and follow the instructions to download, install, and run Docker.

### Adjusting Docker Resources
After installing Docker, you must increase the available resources so that Docker is able to launch the Strea2Graph system. The system requires at least 2 GB of available disk space and 2 GiB of available RAM.
To adjust the available resources, click the Docker icon in the menu bar and select Preferences. On the Settings screen, select Resources.

to run the `stream2graph` pipeline, you need to copy the `logs` folder to the working directory and run : `docker-compose up -p` to build the `logs-generator` images and install required services. 

The used dockerized service are :
- Neo4j database
- Kafka broker
- Zookeper 
- Logs genertor image to generate logs 
