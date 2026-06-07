![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-testing-blue?logo=pytest)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-blue?logo=fastapi)
![Architecture](https://img.shields.io/badge/architecture-modular-lightgreen)


## Step-by-step explanation via console
``` properties
    # 00. Configure the Python virtual environment and install the dependencies
    python3 -m venv .venv
    
    source .venv/bin/activate
    
    pip install -r requirements.txt
    
    pip freeze > requirements.txt
    
    
    # 01. Release the ports you're going to use (if they're in use) and run the project
    sudo lsof -i 

    sudo kill -9 <PID>

    docker compose up -d --build
    
    
    # 02. Verify with Swagger that everything is working correctly. 
    # Check the logs. If this is the first time, run Bootstrap.
    http://localhost:8000/docs
    
    docker logs -f autoparts-api
    
    docker logs -f autoparts-db

    docker exec -it autoparts-api python -m app.scripts.seed

    
    # 03. If we have an error in the previous step, 
    # we must delete the container and its associated volume.
    docker compose down
    
    docker volume ls
    
    docker volume rm <NAME_VOLUME>
``` 

## Project Architecture
```
    PastAPI-Project
    │
    ├── .venv/
    ├── app/
    │   ├── api/
    │   │   ├── dtos/
    │   │   ├── routes/
    │   │   └── __init__.py
    │   │
    │   ├── core/
    │   │   ├── config.py
    │   │   └── __init__.py
    │   │
    │   ├── domain/
    │   │   ├── entities/
    │   │   ├── enum/
    │   │   ├── repositories/
    │   │   ├── services/
    │   │   └── __init__.py
    │   │
    │   ├── infrastructure/
    │   │   ├── database/
    │   │   │   ├── models/
    │   │   │   ├── base.py    
    │   │   │   ├── session.py
    │   │   │   └── __init__.py
    │   │   ├── mappers/
    │   │   ├── repositories/
    │   │   └── __init__.py
    │   │
    │   ├── __main__.py
    │   └── __init__.py
    │   
    ├── test/
    │   ├── test_services/
    │   └── __init__.py
    │   
    ├── docker-compose.yml
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt
    └── .gitignore
```