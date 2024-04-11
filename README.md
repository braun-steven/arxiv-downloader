# arxiv-downloader: The arXiv PDF Command-Line Interface Downloader

![](https://img.shields.io/pypi/v/arxiv-downloader)
![](https://img.shields.io/pypi/pyversions/arxiv-downloader)

![](./featured.svg)


## Installation

arxiv-downloader is available via PyPi:

``` sh
pip install arxiv-downloader
```

## Examples

Download a PDF using a URL:
``` sh
arxiv-downloader https://arxiv.org/pdf/2302.06544.pdf
```

Download a PDF using an ID:
``` sh
arxiv-downloader 2302.06544
```

Download a PDF into a directory:
``` sh
arxiv-downloader https://arxiv.org/pdf/2302.06544.pdf -d ./pdfs
```

Download a PDF and its source files (as `.tar.gz` archive):
``` sh
arxiv-downloader https://arxiv.org/pdf/2302.06544.pdf -s
```

## Usage

To see all available options, use the help command:

``` sh
arxiv-downloader -h
```

This will display usage information similar to the following:

```plaintext
usage: arxiv-downloader [-h] [-d DIRECTORY] [-s] [url_or_id]

Download articles from arXiv.

positional arguments:
  url_or_id             The URL or ID of the arXiv article. (default: None)

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        The directory where the article will be downloaded. (default: ./)
  -s, --source          Also download the source files of the article. (default: False)
```
