# Student Information Management System

This application is intended as a student and course management tool for an institution's academic advisors. It allows for all basic CRUD operations of Create, Read, Update, and Delete.

# Endpoints
| HTTP Method | URI |
| --- | --- |
| GET | /students |
| POST | /students/add |
| PATCH | /students/id/update |
| GET | /id |
| DELETE | /students/id/delete |

Additional endpoints for course, instructor, advisor, and textbook management functions are to be added in the near future. Also, although this version of the app has a very basic UI, I plan on building out a full front end UI in the future.
# Project Design
The project was designed as part of Nucamp's BackEnd w/DevOps bootcamp. The design follows a 2-tier architecture comprised of the main application and a PostgreSQL database. The database was conceived first with the tables and their relationships and constraints, were conceptualized, diagrammed, and implemented in Postgres for testing prior to building out the RESTful API.

## ER Diagram
An entity-relationship diagram, in which each entity and its associated attributes were defined, and relationships between each were mapped. Special care was taken to include one-to-many, many-to-many, and one-to-one relationships, as well as to enforce foreign key contstraints between them in the database design.

## Database Implementation
Originally, a PostgreSQL database was implemented using the Flask microframework, using its ORD, SqlAlchemy. Sample data was then manually added via SQL queries using pgadmin, the built-in GUI that comes with PostgreSQL. Subsequently, the entire project was refactored as a Django application with a Postgres database, in its current iteration. The application was then containerized using Docker, managed via Docker Compose, and deployed to Azure cloud service using Kubernetes.

## ORM vs. Raw SQL approach

I opted for the ORM approach for the project because I wanted to gain additional experience with object-oriented programming principles. Because of my solid understanding of SQL, it made sense to forgo writing raw SQL queries to get more practice in areas where my skills are weaker. The ORM approach presents more of challenge for me at this point in my development, an

# Further Development
In addition to adding more endopoints, the goal is to create front-end, graphical user interface (GUI) an deploy the application to a cloud-based server, such as AWS, Google Cloud, or Heroku. This allows the end user to avoid incurring the cost of server and application maintenance, and allows scalability, as needed.

# Technologies Used

* PostgreSQL
* Docker
* SQLAchemy
* Python 3
* Flask
* Django
* Psycopg2
* Insomnia (testing)
* Kubernetes

The application was built in Python 3 using the Django microframework. The PostgreSQL database runs inside a Docker container, and Insomnia was used to test API functionality.


