# FindFirstFollowSetsOfGrammar

A tool that automatically generates the FIRST and FOLLOW sets for a given grammar. It's ideal for studying compiler principles and practical applications in syntax analysis.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This tool computes the FIRST and FOLLOW sets from a specified grammar file. It's particularly useful for learning about compiler principles and for practical applications in syntax analysis.

## Installation

1. Ensure you have Python 3.x installed.
2. Download or clone this project to your local machine.

## Usage

1. Create a text file named `grammar.txt` and define the grammar in the following format:
    ```
    A → { M N }
    M → Ɛ | P M
    P → D i ;
    D → t | f
    N → Ɛ | Q N
    Q → i = E ;
    E → T E'
    E' → + T E' | - T E' | Ɛ
    T → F T'
    T' → * F T' | / F T' | Ɛ
    F → ( E ) | i | d
    ```
2. Run the program.
