import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arxiv-downloader",
    version="1.0.0",
    author="Steven Braun",
    author_email="steven.braun.mz@gmail.com  ",
    description="A command line interface to download PDF files from https://arxiv.org.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/braun-steven/arxiv-downloader",
    project_urls={
        "Bug Tracker": "https://github.com/braun-steven/arxiv-downloader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["arxiv_downloader"],
    python_requires=">=3.6",
    scripts=["bin/arxiv-downloader"],
        install_requires="arxiv==2.1.0"
)
