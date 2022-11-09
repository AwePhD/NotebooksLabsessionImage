[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/LICENSE)

# Notebooks Labsession Image

This repo is a set of Notebooks for the lab session of 2022-2023 in the context of module "Automatique et Traitement du signal et des images" in [SICOM equivalent M1 first semester](https://phelma.grenoble-inp.fr/fr/formation/fili-egrave-re-signal-image-communication-et-multim-eacute-dia-sicom-semestre-7) program in [PHELMA](https://phelma.grenoble-inp.fr/) and [ENSE3](https://ense3.grenoble-inp.fr/) engineering schools. These notebooks are not the solutions of the lab sessions. They are a set of code examples to process data.

These code examples are meant to be used and adapted for SICOM internships / future lab session in Image processing and other fields. The students are highly encouraged to follow / to question these code examples as soon as possible, namely for their future lab sessions. These notebooks aim to give good code practice and are used to illustrate some explanation during the Lab sessions. **The grading of lab sessions are not based on the following of these code recommendations.**

## How to use

- **Google Collab**: Each notebook has a collab link that can be clicked on (see below). The code runs on Google Server for free, without installation. All you need is a google account to log on their platform.
- **Local**: You can also clone the repo on your local computer. Just install the local NLI package and it will install the depencies. You will need a local Jupyter server (installed with conda for example) and a code editor (Jupyter Lab, Visual Studio Code). *Do not run the first cells of notebooks in local, they are meant to be used on google collab.*

## Quick Notebooks' descriptions

These notebooks are based on the [Kaggle Pokemon Dataset](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types). Credits go to the original owners.

### A quick introduction to `ndarray`

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/numpy_starter_pack.ipynb)

This short notebook aims to introduce `ndarray`. The core elements needed for the lab sessions and other notebooks are presented here.

### Image processing

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/image_processing.ipynb)

The notebook is about the processing of images with scikit-image. The images are treated as numpy ndarray.

### Path management

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/manage_path.ipynb)

Managing the path in Python is a pain. The [pathlib](https://docs.python.org/fr/3/library/pathlib.html) is a built-in python library that does the work for you. This is easy to use and OS independent. This short notebooks show up basic operations to save a lot of times for the rest of your Python journey.

### Pythonic comprehension

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/comprehension_illustrated.ipynb)

List and dictionary comprehensions are often seen in Python code, there are representative of clean and efficient code. This notebooks present them.

### CSV processing with Pandas

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/pandas_intro.ipynb)

`.csv` files are commonly used to process dataset. A lot of data might be represent from few features. [Pandas](https://pandas.pydata.org/docs/getting_started/overview.html#:~:text=pandas%20is%20a,toward%20this%20goal.) is a package that implements a lot of easy ways to represent and to "get-to-know" the data. This package is widely used among data analysts.

## How to contribute

This repo is an invitation for students to participate in the notebooks development. The [issues](https://github.com/AwePhD/Notebooks_Labsession_Image/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) and the [pull requests](https://github.com/AwePhD/Notebooks_Labsession_Image/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc) might be used to enhance the quality of the code examples or ask questions about it. **Solutions or corrections of the lab sessions are stricly forbidden in the repo! If you have a problem related to the notebooks, you must provide [minimal working examples](https://en.wikipedia.org/wiki/Minimal_working_example#:~:text=In%20computing%2C%20a%20minimal%20working,to%20be%20demonstrated%20and%20reproduced.&text=A%20minimal%20working%20example%20may,short%20self%2Dcontained%20correct%20example.) to reproduce this error with a non-related lab session code.**

## What is NLI ?

This package has few functions that are useful for the notebooks' explanations. Actually, these functions could have been defined in notebooks. This NLI python package is made to show how to make package in python. Also there are the python files [`pyproject.toml`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/pyproject.toml), [`setup.cfg`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/setup.cfg), [`setup.py`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/setup.py) so the package can be installed with `pip`. It can be installed directly from this repo with the line ```pip install git+https://github.com/AwePhD/NotebooksLabsessionImage.git```.

### External ressources

There are many references of the [Python DataScience Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html) in the notebooks.This is a great **reference** book for newcomer in data science in Python. It gives all the handy features of the most wildly used library. Plus the content of the book is composed by notebooks, only!

![PDSH-cover](./img_md/PDSH-cover.png)

## Credits

Mathias Réus - PhD Student, Gipsa-Lab
