# Final Project Inovação Afro CÉSAR

This project was made by final avaliation from teacher and CESAR institute, using the material learned about the formation at bootcamp 2021.
## Data'Source
https://datahub.io/five-thirty-eight/comic-characters

## End points

|      Endpoint       |       Method        |       Action        |
| ------------------- | ------------------- | ------------------- |
| /list               |   GET               |  Retorna lista de todos os herois da DC Comics paginadas de 50 em 50 |
| /details/{id}       |   GET               |  GET	 Retorna os detalhes de um heroi por id 
| /create	          |   POST              |Adiciona um novo héroi  à base de dado |   
| /partial/{id}       |   PATCH             | Atualização parcial de um heroi|  
| /update/{id}        |   UPDATE            | Atualização completa de um heroi|  
| /delete/{id}        |   DELETE            |Remove um herói da base de dados |   

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## Setup Docker
Garanta que o Docker e o Docker Compose estão instalados em seu ambiente
Na raiz do projeto, execute os seguintes comandos
#### docker-compose run --rm app python manage.py createsuperuser # Para criar um superusuário
#### docker-compose run --rm app python manage.py populate_db # Para pré-popular o banco de dados com dados iniciais de todos os heróis da Dc Comics
## Features
* Documentations
* Logs
* Error handling



## License
[MIT](https://choosealicense.com/licenses/mit/)