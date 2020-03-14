docker build -t covid .

docker container ls -a

docker stop $1
docker_id=$(docker container ls -a | grep $1 | cut -d' ' -f1)

echo $docker_id
docker container rm $docker_id

docker run -d --name $1 -p 9090:9090 covid
