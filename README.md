# text-to-sql-backend-pt-br-deploy

installl libs
pip install fastapi uvicorn pydantic transformers tensorflow

run no docker
uvicorn main:app --reload --port 8080

create image
docker build -t myimage .

run container
docker run -d --name mycontainer -p 8080:8080 myimage

delete stop container
docker stop id

delete remove container
docker rm id

delete remove container
docker image

delete remove image
docker rmi id

About
No description, website, or topics provided.
Topics
Resources
 Readme
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
Python
100.0%

