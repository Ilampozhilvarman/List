# List project

## What it does:

This is a simple project used to make list dynamically. You can edit the data manually or use admin.py file and use it's commands to add/remove/edit data.
The backend reads the data and makes a front-end list dynamically without hard-coding the front-end for every list.

## How you can edit it:

You can manually change the data data.json. I just put some placeholder data there for fun.
You can also edit the style.css files to make it look like how you want your lists to look like.

## How to copy the repo:

```bash
git clone https://github.com/Ilampozhilvarman/List
```
## How to create a virtual environment:
## Setup and Installation

Follow these steps to set up the project locally:

### 1. Create a Virtual Environment
Create a local virtual environment to isolate project dependencies:

```bash
# Generate the virtual environment folder
python -m venv .venv
```

### 2. Activate the Environment
Activate the environment based on your operating system:

* **Windows (Command Prompt / PowerShell):**
  ```bash
  .\.venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Ensure your environment is active, then install the required packages:

```bash
pip install -r requirements.txt
```

---

*Note: The `.venv/` directory is platform-specific and should never be committed to version control. Ensure it is included in your `.gitignore` file.*

## How to run the lists:

```bash
cd List
python backend.py
```

# How to change the data using python:

```bash
cd List
python admin.py
```

### Libraries needed:
- **Language:** Python 3.10
- **Main Libraries:** flask, json
- **Niche Libraries:** os, subprocess (only used for clearing the screen) (optional)
- **Storage:** Local JSON file (data.json)
