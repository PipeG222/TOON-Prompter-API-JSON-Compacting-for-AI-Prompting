🧾 README.md (versión completa actualizada)
TOON Prompter API

API built with FastAPI to convert large JSON into a compact TOON-style format optimized for AI prompts. It receives standard JSON and outputs a shorter, semantically preserved version to reduce tokens and improve LLM understanding. Includes REST endpoints, schema shortening, key reduction and reversible decoding.

🚀 Features

Compact JSON (remove whitespace/indentation)

LLM-oriented optimization (shorter keys + simplified structure)

TOON format (compression + semantic optimization)

Fully reversible

REST interface

Easy deployment

Ready for Docker + Terraform + CI/CD

📁 Project Structure
toon-prompter-api/
  app/
    main.py
    converters/
      compression.py
      optimizer.py
      toon.py
      reverse.py
    routers/
      rest.py
    schemas/
      request.py
      response.py
    utils/
      cleaner.py
  requirements.txt
  README.md

🧠 Processing Modes

Your API supports three transformation modes that solve different needs when transporting JSON or sending prompts to LLMs.

1️⃣ Mode 1: Compression Only
Description

Converts JSON into its shortest possible version without changing the structure.

Purpose

Reduce data size for:

messaging

sockets

networks

queues

microservices

Example

Request:

POST /convert/json?mode=1


Payload:

{"username": "felip", "role": "developer"}


Result:

{"username":"felip","role":"developer"}


✔ Reversible
✔ Valid JSON
✔ Shorter

2️⃣ Mode 2: Optimization for LLM
Description

Shortens and simplifies the structure for AI models:

shorter keys

less noise

semantic preservation

Example

Request:

POST /convert/json?mode=2


Payload:

{"username": "felip", "country": "CO"}


Result:

{"u": "felip", "c": "CO"}


✔ Best for prompt engineering
✔ Reduces tokens

3️⃣ Mode 3: TOON (Both)
Description

Combines mode 1 and 2:

key shrinking

compact string output

best for LLM + transport

Request:

POST /convert/json?mode=3


Payload:

{
  "username": "felip",
  "role": "developer",
  "country": "CO",
  "age": 22
}


Response:

{
  "mode": "toon",
  "original": {
    "username": "felip",
    "role": "developer",
    "country": "CO",
    "age": 22
  },
  "result": "{\"u\":\"felip\",\"r\":\"developer\",\"c\":\"CO\",\"a\":22}"
}


✔ Minimizes size
✔ Optimized for LLM
✔ Final TOON format

🧪 API Usage
Endpoint
POST /convert/json?mode={1|2|3}

Example cURL
curl --location 'http://127.0.0.1:8000/convert/json?mode=3' \
--header 'Content-Type: application/json' \
--data '{
    "username": "felip",
    "role": "developer",
    "country": "CO",
    "age": 22
}'

▶️ Running the API
Create virtual env
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

Install dependencies
pip install -r requirements.txt

Start server
uvicorn app.main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs

📌 Roadmap

GraphQL endpoint

TOON → JSON decoding

EC2 deployment

HTTPS + Load balancer

Docker + CI/CD

🧑‍💻 Author

Felip – Fullstack & Cloud Developer