import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arxiv-downloader",
    version="0.0.1",
    author="Steven Lang",
    author_email="steven.lang.mz@gmail.com  ",
    description="A command line interface to download PDF files from https://arxiv.org.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/steven-lang/arxiv-downloader",
    project_urls={
        "Bug Tracker": "https://github.com/steven-lang/arxiv-downloader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=["arxiv_downloader"],
    python_requires=">=3.6",
    scripts=["bin/arxiv-downloader"],
        install_requires="arxiv==1.2.0"
)
