import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    INSTALL_REQUIRES = [l.split('#')[0].strip() for l in fh if not l.strip().startswith('#')]

setuptools.setup(
    name="all_twitter_scraper",
    version="0.0.4",
    author="Abdallah Samir",
    author_email="eng.abdallahsamir@gmail.com",
    license='MIT',
    description="Get all tweets filtered by the parameters that are in twitter advanced search.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samirian/all_twitter_scraper",
    keywords="twitter tweets scraper",
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
    install_requires=INSTALL_REQUIRES
)
