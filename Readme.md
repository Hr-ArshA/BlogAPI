Blog API

if you want ran the database 
`sudo docker run -p 5432:5432 --name postgres -e POSTGRES_HOST_AUTH_METHOD=trust -v ./database:/var/lib/postgresql/data -d postgres`