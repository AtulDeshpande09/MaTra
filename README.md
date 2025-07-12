
# Marathi FST-Based English-to-Marathi Translator

A rule-based system that performs syntactic and morphological translation from English to Marathi using a finite-state-like architecture. This system focuses on SVO (subject-verb-object) structures and demonstrates verb inflection via morphosyntactic features.

---

## Project Goals

- Demonstrate a lightweight rule-based NLP pipeline for English-to-Marathi translation.
- Handle morphological inflection of verbs using machine learning-based suffix prediction.
- Explore the potential of language technology for low-resource Indic languages.

---

## Features

- Subject-verb-object structure parsing via SpaCy
- Morphological inflection of Marathi verbs using person, number, gender, tense
- Dictionary-based mapping (lexicon) for subject/object terms
- Extendable to other syntactic structures

---

## Example

**Input:** `She eats apple.`  
**Output:** `ती सफरचंद खाते`

---

## Requirements

```bash
pip install -r requirements.txt
````

Key packages:

* `spaCy`
* `scikit-learn`
* `numpy`, `pickle`

---

## References
* [SpaCy Dependency Parsing](https://spacy.io/usage/linguistic-features#dependency-parse)

