# bn-ideas

## Background

The aim for this repo was to explore Bayesian networks (BNs) using [pgmpy](https://pgmpy.org/).

Some basic examples that cover creating, fitting, and describing BNs are given. These are based on the **pgmpy** docs.

## File Structure

|---earthquake<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---earthquake.py<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---...<br/>
|---fruit<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---fruit.py<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---...<br/>
|---structure<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---learn_structure.py<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|---...<br/>
|--- .gitignore
|--- LICENCE
|--- README.md

Examples are kept in separate files which relate to a particular BN. Taken together, these BN examples represent a quick tour of some functions available in **pgmpy**.

The earhquake alarm example covers creating a BN an outputting summaries and predictions from the model.

The fruit example explores fitting model probabilities to data.

The structure example explores BN structure learning from data.

## Key Tools

Python 3.10
pgmpy 0.1.20