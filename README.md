# text-to-sql-backend-pt-br-deploy

## instal libs

pip install torch===1.7.0 torchvision===0.8.1 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

pip install fastapi uvicorn pydantic transformers googletrans

## run no docker

uvicorn main:app --reload --port 8080

## create image

docker build -t myimage .

## run container

docker run -d --name mycontainer -p 8080:8080 myimage 

## delete stop container

docker stop id

## delete remove container

docker rm id

## delete remove container

docker image

## delete remove image

docker rmi id


