# awesome-scripts

> Note down some useful scripts in the daily practice.

---

## ToC
- [code2text](#code2text): Turn your code snippets into text instruction in natural language.

---

## code2text

> Sometimes you code on your own, but sometimes you just ask others (e.g. agents) to code.

Turn your code snippets into text instruction in natural language.

### Sample input
```python
import os

print(os.environ)
```

### Sample output
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

### How to use

Details refer to \[[Link](./scripts/code2text/README.md)\].

---

## pdf_cropping

> The figure in the paper has tooooooooo much blank spaces! ~~And I'll write your name~~

Crop all the blank space in your .pdf file.

---

[TBC]