import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()#we are reading readme.md file

__version__ = "0.0.0"

REPO_NAME = "DeepCNN_Classifier"
AUTHOR_USER_NAME = "jaiswalpartha"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "parthajaiswal111@gmail.com"

setuptools.setup(name=SRC_REPO,
                version=__version__,
                author=AUTHOR_USER_NAME,
                author_email=AUTHOR_EMAIL,
                description="a small python package for CNN application",
                long_description=long_description,
                url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
                project_urls = {
                    "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
                },
                package_dir={"":"src"},
                packages= setuptools.find_packages(where ="src"))
                    