# FastAPI Backend

## Futtatás

1. fastapi uvicorn telepítés:
```
pip install fastapi uvicorn
```


2. Szerver indítás:
```
uvicorn main:app --reload
```


3. Teszt:
- Böngészőben vagy terminálból:  
  ```
  curl "http://127.0.0.1:8000/greeting?name=Tamás"
  ```
- Válasz:
  ```json
  {"message": "Hello Tamás!"}
  ```
