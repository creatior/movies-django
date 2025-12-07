# **Movies Django**

## **Description**  
**Movies Django** is a Django REST Framework-based web application for managing and displaying movies. It serves as a starter template for building a more complex project — with features such as user accounts, REST API, categories, directors and movies.

## **Features**
- Movie list page
- Detailed movie page
- Authorization via JWT

## **Apps**
| **App**       | **Description**                                                                               |
| ------------- | --------------------------------------------------------------------------------------------- |
| **users**     | Handles registration, activation, JWT authentication, and profile management.                 |
| **movies**    | Manages movies, search, and caching.                                                          |
| **common**    | Shared utilities (JWT handling, Redis helpers, superuser registration).                       |

## Technologies  
| **Techology**    | **Purpose**                      |
| ---------------- | -------------------------------- |
| **Django + DRF** | REST API framework               |
| **PostgreSQL**   | Main relational database         |
| **Redis**        | Cache and temporary keys storage |
| **Docker**       | Launching                        |

## Services and ports
| Service          | Purpose | Default Port | URL |
| ---------------- | --------------------------------- | ---- | ---------------------------------------------- |
| **Web (Django)** | Main API, Admin panel, Swagger UI | 8000 | [http://localhost:8000](http://localhost:8000) |
| **PostgreSQL**   | Database                          | 5432 | `postgres:5432`                                |
| **Redis**        | Cache                             | 6379 | `redis:6379`                                   |

## **API Overview**

### **Users**
| **Method** | **Endpoint**           | **Description**       |
| ---------- | ---------------------- | --------------------- |
| `POST`     | `/api/users/register/` | Register new user     |
| `POST`     | `/api/users/login/`    | Login and receive JWT |

### **Movies**
| **Method**  | **Endpoint**              | **Description**                            |
| ----------- | ------------------------- | ------------------------------------------ |
| `GET`       | `/api/movies/movies/`     | List movies with pagination and filtration |
| `GET`       | `/api/movies/movies/{id}` | Get movie by ID                            |
| `POST` 🔒   | `/api/movies/movies/`     | Create movie                               |
| `PUT`  🔒   | `/api/movies/movies/{id}` | Update movie                               |
| `DELETE` 🔒 | `/api/movies/movies/{id}` | Delete movie                               |

### **Directors**
| **Method**  | **Endpoint**                 | **Description**  |
| ----------- | ---------------------------- | ---------------- |
| `GET`       | `/api/movies/directors/`     | List directors   |
| `POST` 🔒   | `/api/movies/directors/`     | Create director  |
| `PUT`  🔒   | `/api/movies/directors/{id}` | Update director  |
| `DELETE` 🔒 | `/api/movies/directors/{id}` | Delete director  |

### **Genres**
| **Method**  | **Endpoint**              | **Description**  |
| ----------- | ------------------------- | ---------------- |
| `GET`       | `/api/movies/genres/`     | List genres      |
| `POST` 🔒   | `/api/movies/genres/`     | Create genre     |
| `PUT`  🔒   | `/api/movies/genres/{id}` | Update genre     |
| `DELETE` 🔒 | `/api/movies/genres/{id}` | Delete genre     |

## 🚀 **Running the Application**

### 🐳 **Build and start all containers**

```
docker-compose up --build -d
```
