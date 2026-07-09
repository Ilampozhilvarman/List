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
