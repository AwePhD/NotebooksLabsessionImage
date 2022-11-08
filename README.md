[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/LICENSE)

# Notebooks Labsession Image

This repo is a set of Notebooks for the lab session of 2021-2022 in the context of module "Automatique et Traitement du signal et des images" in [SICOM equivalent M1 first semester](https://phelma.grenoble-inp.fr/fr/formation/fili-egrave-re-signal-image-communication-et-multim-eacute-dia-sicom-semestre-7) program in [PHELMA](https://phelma.grenoble-inp.fr/) and [ENSE3](https://ense3.grenoble-inp.fr/) engineering schools. These notebooks are not the solutions of the lab sessions. They are a set of code examples to process data. 

These code examples are meant to be used and adapted for SICOM internships / future lab session in Image processing and other fields. The students are highly encouraged to follow / to question these code examples as soon as possible, namely for their future lab sessions. **The grading of lab sessions are not based on the following of these code recommendations.**

## How to use

### Google Collab 

Each notebook has a collab link that can be clicked on (see below). The code runs on Google Server for free, without installation. All you need is a google account to log on their platform. 

### Local

You can also clone the repo on your local computer. Just install the local NLI package and it will install the depencies. You will need a local Jupyter server (installed with conda for example) and a code editor (Jupyter Lab, Visual Studio Code). 

## Quick Notebooks' descriptions

These notebooks are based on the [Kaggle Pokemon Dataset](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types). Credits go to the original owners.

### Image processing

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/image_processing.ipynb)

The notebook is about the processing of images with scikit-image. The images are treated as numpy ndarray. Also, there is some presentations about  list and dictionnary comprehensions. Manipulations of numpy arrays are extremely important for any data processing in Python. Numpy has a natural way to interact with multiple dimensional data, the MATLAB easy-to-use syntax for algebra can be [simply translated](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) into numpy syntax.

To go further, this is a good start to process image. Another good way is to build a class for interacting with image. Namely, why images are numpy ndarrays ? numpy ndarrays can be anything: images, videos, spectograms, various signals ... An Image class **specific** could operate processing based on the image directly. For example the library PIL have an [Image class](https://pillow.readthedocs.io/en/stable/reference/Image.html) that implements this idea. In data processing, the standard way is to build a class specific to the data. This [video](https://www.youtube.com/watch?v=vBH6GRJ1REM) is a good introduction, programming object oriented knowledge is required to understand this video. 

### Path management

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/manage_path.ipynb)

Managing the path in Python is a pain. The [pathlib](https://docs.python.org/fr/3/library/pathlib.html) is a built-in python library that does the work for you. This is easy to use and OS independent. This short notebooks show up basic operations to save a lot of times for the rest of your Python journey. **HIGHLY RECOMMENDED**

### CSV processing with Pandas

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AwePhD/NotebooksLabsessionImage/blob/main/notebooks/pandas_intro.ipynb)

`.csv` files are commonly used to process dataset. A lot of data might be represent from few features. [Pandas](https://pandas.pydata.org/docs/getting_started/overview.html#:~:text=pandas%20is%20a,toward%20this%20goal.) is a package that implements a lot of easy ways to represent and to "get-to-know" the data. This package is widely used among data analysts.

## How to contribute

This repo is an invitation for students to participate in the notebooks development. The [issues](https://github.com/AwePhD/Notebooks_Labsession_Image/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) and the [pull requests](https://github.com/AwePhD/Notebooks_Labsession_Image/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc) might be used to enhance the quality of the code examples or ask questions about it. **Solutions or corrections of the lab sessions are stricly forbidden in the repo! If you have a problem related to the notebooks, you must provide [minimal working examples](https://en.wikipedia.org/wiki/Minimal_working_example#:~:text=In%20computing%2C%20a%20minimal%20working,to%20be%20demonstrated%20and%20reproduced.&text=A%20minimal%20working%20example%20may,short%20self%2Dcontained%20correct%20example.) to reproduce this error with a non-related lab session code.**

## What is NLI ?

This package has few - 3 - functions that are useful for the notebooks' explanations. Actually, these functions could have been defined in notebooks. This NLI python package is made to show how to make package in python. Also there are the python files [`pyproject.toml`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/pyproject.toml), [`setup.cfg`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/setup.cfg), [`setup.py`](https://github.com/AwePhD/NotebooksLabsessionImage/blob/main/setup.py) so the package can be installed with `pip`. It can be installed directly from this repo with the line ```pip install git+https://github.com/AwePhD/NotebooksLabsessionImage.git ```.

Thanks for you reading. Once again, do not hesitate to raise issues for any questions and a pull requests for any potential improvements.
