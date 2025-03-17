# Einführung in Terminal und Git

## Das solltest du dir anschauen

- Terminal vs Shell
- Command Line Basics aneignen
- Git wiederholen

## Wichtig zu verstehen:

- Terminal Basics
- Git Basics

## Thema 1 - Command Line Basics

Ich denke, damit es dir leichter fällt, in der Uni und auch allgemein Programmier- und Computerthemen zu verstehen,
wäre es wichtig zu verstehen, wie:

- die grundlegende Terminologie ist (was ist ein **Command**, was ist eine **Shell**, was ist die **Eingabeaufforderung** etc.)
- man durch die Ordnerstruktur auf deinem Rechner navigiert und auch "Orte" auf deinem Rechner referenziert
- man Inhalte in Ordnern anzeigt
- die grundlegende Struktur eines Terminalcommands
- einige Shell-Befehle und CLIs kennenlernen :
  - ls
  - cd
  - mkdir
  - touch
  - man
  - cp
  - mv
  - cat
  - **rm (VORSICHT!!!!)**
  - **git**
  - python
    - und pip/conda

So könnte eine Beispielaufgabe aussehen:

**Q1:**
Du befindest dich in

```
~/Downloads
```

navigiere nach

```
~/Python-Projekte/uniAufgabeA
```

und zeige alle Inhalte des Ordners in Listenform an.

**A1:**

```
cd ../Python-Projekte/uniAufgabeA
ls -la
```

## Thema 2 - Git

Lerne auch die Grundlagenbefehle von Git auf der Kommandozeile, das hilft zu verstehen, was die Knöpfe in unterschiedlichen IDEs im Hintergrund ausführen:

- git push
- git pull
- git commit
- git fetch
- git merge
- git branch
- git checkout
- Bonus: git stash

Du solltest zumindest wissen, was die Befehle machen und wie du sie grundlegend verwendest.

So könnte eine Beispielaufgabe aussehen:

**Q1:**
"Wechsle auf den Branch mit dem Namen feature1"

**A1:**

```
git checkout feature1
```

**Q2:**
"Du hast Änderungen in 3 Dateien (a.txt, b.txt, c.txt). Committe alle Änderungen in Datei a.txt und setze alles andere zum Ursprungszustand, nach deinem letzten Commit"

**A2:**

```
git add a.txt
git commit -m "Änderungen in a.txt committen"
git checkout -- b.txt c.txt
# alternativ: git restore b.txt c.txt
```
