# Introduction to Terminal and Git

## What you should explore
- Terminal vs Shell
- Learn Command Line Basics
- Review Git

## Important to understand:
- Terminal Basics
- Git Basics

## Topic 1 - Command Line Basics
I think to make it easier for you to understand programming and computer topics at university and in general, it would be important to understand how to:
- use the basic terminology (what is a **Command**, what is a **Shell**, what is the **Command Prompt**, etc.)
- navigate through the folder structure on your computer and reference "locations" on your computer
- display contents in folders
- understand the basic structure of a terminal command
- learn some Shell commands and CLIs:
  - ls
  - cd
  - mkdir
  - touch
  - man
  - cp
  - mv
  - cat
  - **rm (CAUTION!!!!)**
  - **git**
  - python
    - and pip/conda

Here's what a sample task might look like:
**Q1:**
You are in
```
~/Downloads
```
navigate to
```
~/Python-Projekte/uniAufgabeA
```
and display all contents of the folder in list form.

**A1:**
```
cd ../Python-Projekte/uniAufgabeA
ls -la
```

## Topic 2 - Git
Also learn the basic commands of Git on the command line, which helps to understand what the buttons in different IDEs execute in the background:
- git push
- git pull
- git commit
- git fetch
- git merge
- git branch
- git checkout
- Bonus: git stash

You should at least know what the commands do and how to use them basically.

Here's what a sample task might look like:
**Q1:**
"Switch to the branch named feature1"

**A1:**
```
git checkout feature1
```

**Q2:**
"You have changes in 3 files (a.txt, b.txt, c.txt). Commit all changes in file a.txt and reset everything else to the original state, after your last commit"

**A2:**
```
git add a.txt
git commit -m "Commit changes in a.txt"
git checkout -- b.txt c.txt
# alternatively: git restore b.txt c.txt
```
