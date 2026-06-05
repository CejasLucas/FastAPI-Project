## TEST

### 0. Puertos
``` bash
    sudo lsof -i 
    kill -9 <PID>
    //Mirar logs
    docker logs -f autoparts-api
    docker logs -f autoparts-db
    // Ejecutar bootstrap
    docker exec -it autoparts-api python -m app.scripts.seed
``` 

### 1. Elimina el contenedor y el volumen.
``` bash
    docker compose down
    docker volume ls
    docker volume rm "name_volume"
```

### 2.  Levanta las tablas (si estan creadas las deja como esta)
``` bash
    docker compose up -d --build
    docker logs -f autoparts-api
```

### 3. Swagger
``` bash
    http://localhost:8000/docs
```

### Execute PYTHONPATH.:
``` bash
    python -m app.infrastructure.bootstrap.seed
    python /app/app/infrastructure/bootstrap/seed.py
```
