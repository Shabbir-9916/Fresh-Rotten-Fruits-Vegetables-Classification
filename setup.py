import setuptools



__version__ = "0.0.0"

REPO_NAME = "Fresh-Rotten-Fruits-Vegetables-Classification"
AUTHOR_USER_NAME = "Shabbir Hussain"
SRC_REPO = "FreshRottenClassifier"
AUTHOR_EMAIL = "shabbir.hussain1699@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A package for Fresh Rotten Fruits Vegetable Classification",
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src"),


)



