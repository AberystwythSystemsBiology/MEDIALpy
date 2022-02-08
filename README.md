# MEDIALpy: MEDIcal Abbreviations Lookup in Python

[![GitHub commits](https://badgen.net/github/commits/AberystwythSystemsBiology/MEDIALpy/main)](https://GitHub.com/AberystwythSystemsBiology/MEDIALpy/main/commit/)
![GitHub issues](https://img.shields.io/github/issues/AberystwythSystemsBiology/MEDIALpy)
![GitHub repo size](https://img.shields.io/github/repo-size/AberystwythSystemsBiology/MEDIALpy)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

A small python package that allows the user to look up common medical abbreviations.

> **Notice:** Huge thank you to [imantsm](https://github.com/imantsm) for his excellent [medical abbreviations repository](https://github.com/imantsm/medical_abbreviations). If you found utility in this little tool, please go star the [original project](https://github.com/imantsm/medical_abbreviations).

## Installation

You can install the development version directly from GitHub with:

```
pip install git+https://github.com/AberystwythSystemsBiology/MEDIALpy
```

## Common Usage

### Find an abbreviation:

```python
import medialpy

term = medialpy.find("T1DM") 
print(term.meaning) #['type 1 Diabetes Mellitus']
```

### Check if an abbreviation exists:

```python
import medialpy

if medialpy.exists("AD"):
    print("Exists")
```

### Check what version of imantsm's data dictonary is being used:

```python
import medialpy

print(medialpy.get_version()) # a62e91303c0966ab6803e765a752581f7d10fff9
```

## Bug reporting and feature suggestions

Please report all bugs or feature suggestions to the [issues tracker](https://www.github.com/AberystwythSystemsBiology/MEDIALpy/issues). Please do not email me directly as I'm struggling to keep track of what needs to be fixed.

We welcome all sorts of contribution, so please be as candid as you want.

## License

This project is proudly licensed under the terms of the [MIT License](https://raw.githubusercontent.com/AberystwythSystemsBiology/MEDIALpy/main/LICENSE).