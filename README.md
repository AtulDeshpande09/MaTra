# MaTra: Marathi Translator – A Hybrid Machine Translation System

**MaTra** is a lightweight hybrid machine translation system designed for translating simple English sentences into grammatically correct Marathi. It combines rule-based syntactic transformation with a machine-learned morphological inflector to ensure accurate subject-verb agreement, tense handling, and pronoun generation.

## Features

- Rule-based SVO-to-SOV sentence restructuring
- Tense detection using spaCy-based POS tagging
- Decision Tree–based morphological inflector for Marathi verbs and pronouns
- Modular and interpretable design
- Clean dataset for training and evaluating inflection rules

## Motivation

Marathi is a morphologically rich and low-resource language. Most neural MT systems struggle with accurate agreement handling in such languages, especially without large corpora. MaTra aims to provide a transparent, controllable translation pipeline that prioritizes grammatical accuracy over black-box fluency.

## System Architecture

1. **Input Parsing**: English sentence is parsed using spaCy to extract subject, verb, object, and tense.
2. **Syntactic Reordering**: Converts the sentence to Marathi structure (Subject–Object–Verb).
3. **Morphological Inflection**: Applies a trained Decision Tree model to inflect the verb root and generate the correct pronoun.
4. **Output Generation**: Final sentence is assembled from the components.

## Example

**Input:**  
`She eats apples.`

**Output:**  
`ती सफरचंद खाते`

## Getting Started

### Requirements

- Python 3.8+
- scikit-learn
- pandas
- spaCy (`en_core_web_sm` model)

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
````

### Running the System

```bash
python main.py
```

## Dataset

The morphological inflection model is trained on a manually curated CSV dataset with features:

* Person (0/1/2)
* Number (Singular/Plural)
* Gender (Masc/Fem/Neut)
* Tense (Present/Past/Future)

Each row maps these features to the correct Marathi pronoun and verb suffix.


## Future Work

* Extend tense support (progressive, perfect, perfect-progressive)
* Handle compound and complex sentences
* Add support for postpositions and determiners
* Build a web interface or CLI tool for public use
* Inflection based on Intransitive verbs

## License

This project is released under the MIT License.
