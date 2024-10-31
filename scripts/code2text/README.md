# code2text

Turn your code snippets into text instruction in natural language (while preventing any changes to the meaning).

## When you input
```python
import os

print(os.environ)
```

## What you will get
**Summary:**
```
Create and execute a Python script that prints the environment variables of the system using the os module.
```

**Details:**
``` 
Create and execute a Python script that retrieves and prints the current environment variables.

1. Import the `os` module, which provides a portable way of using operating system-dependent functionality.
2. Use the `os.environ` attribute to access the environment variables.
3. Print the dictionary-like object `os.environ` that contains the user's environment variables.
```

## How to use

Install some necessary packages first, including `openai`.

All you need to modify are two things:
1. `config.py` file: 
    1. line 3: Replace `<YOUR_API_KEY_HERE>` with your environment varible which stores the OpenAI key.
    2. line 4: `source_language` is the programming language of your source code, it could be `python`, `c++` or `java` (in the future). Currently it only supports `python`.
    4. line 5: `target_file` is the json file about the final results, containing the original code and transformed text. Initially it is `example_trans.json`.
2. `code_snippets` folder: It stores the code snippets you want to transform. Initially it has three demo Python snippets, and feel free to replace as you want.

## Results format
The output is a list in json format, which looks like
```json
[
    {
        "Source_file": "./code_snippets/os.py",
        "Code": "import os\n\nprint(os.environ)",
        "Text_summary": "Create and execute a Python script that prints the environment variables of the system using the os module.",
        "Text_details": "Create and execute a Python script that retrieves and prints the current environment variables.\n\n1. Import the `os` module to interact with the operating system.\n2. Use the `os.environ` attribute to access the environment variables.\n3. Print the environment variables to the console."
    }
]
```

---

[END]