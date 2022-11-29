=========
Typocheck
=========

**WARNING: This README is a lie.** This is a project that I never finished or really started in earnest, even. The README is not a description, but a plan, and a plan that will most likely never be implemented. **End warning**

Command-line utility for quickly typo-checking a large number of files in a manner that minimizes false positives and deals nicely with novel spellings.

Unlike a typical spellchecker, Typocheck doesn't rely on having a predefined dictionary of correctly spelled words (although having one does help). When Typocheck encounters a word it can't find in the dictionary, it checks whether there is a similar word in the dictionary already. If there is, Typocheck assumes the least frequently-occurring of the two words is a typo of the other. Otherwise, it adds the word to the dictionary. The idea is that if an unfamiliar word is a minor alteration of a familiar word that occurs few times, then it's probably a typo, while if an unfamiliar word is spelled consistently across multiple occurrences, it's probably not a typo.

Installation
============

Typocheck is on PyPI_, so you can use pip:

.. _PyPI: https://pypi.org/project/typocheck/

.. code:: console

    pip install typocheck

Usage
=====

To recursively check every file in the current directory and its subdirectories:

.. code:: console

    typocheck

To check non-recursively (only including files directly including in the current directory):

.. code:: console

    typocheck -n

To check a particular file or directory:

.. code:: console

    typocheck <path>

Typocheck will write a "plan" to standard output, which looks like this:

.. code:: console

    1 appliaction -> application
    2 lst, lsit -> list
    ...

This means it thinks "appliacation" is a typo of "application" and both "lst" and "lsit" are typos of "list". Typocheck will then ask for your thoughts on its plan. If you type a line number, you'll be brought to an interface where you can alter everything about Typocheck's plan for the particular replacement described on that line; you can cancel it, or cancel replacement of just one of the words, or see where in the targeted the words listed occur, etc.

.. code:: console

    Type a line number for more info, or Enter to proceed.
    typocheck> 

Once you press Enter, Typocheck will carry out the replacements according to its amended plan.

Configuration
=============

Typocheck is highly configurable. You can customize things like where it draws word boundaries, or how similar is "similar" for the purpose of deciding whether a word might be a typo of another word. As well as passing options on the command line, you can write a file called "typocheck-settings.py" in the current directory.
