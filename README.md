# arxiv-downloader: The ArXiv PDF Command-Line Interface Downloader

![](https://img.shields.io/pypi/v/arxiv-downloader)
![](https://img.shields.io/pypi/pyversions/arxiv-downloader)


## Installation

Arxiv-downloader is available via PyPi:

``` sh
pip install arxiv-downloader
```

## Examples

Download PDF from URL:
``` sh
arxiv-downloader --url https://arxiv.org/pdf/2101.05084.pdf
```

Download PDF from ID:
``` sh
arxiv-downloader --id 2101.05084
```

Download PDF into existing directory:
``` sh
arxiv-downloader --url https://arxiv.org/pdf/2101.05084.pdf --directory ./pdfs
```

Download PDF and source files (as `.tar.gz` archive):
``` sh
arxiv-downloader --url https://arxiv.org/pdf/2101.05084.pdf --source
```


## Usage

``` sh
> arxiv-downloader -h

usage: arxiv-downloader [-h] [--url URL] [--id ID] [--directory DIRECTORY] [--source]

ArXiv Paper Downloader.

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     ArXiv article URL.
  --id ID, -i ID        ArXiv article ID (for https://arxiv.org/abs/2004.13316 this would be
                        2004.13316).
  --directory DIRECTORY, -d DIRECTORY
                        Output directory.
  --source, -s          Whether to download the source tar file.
```

