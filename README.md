# arxiv-downloader: The ArXiv PDF Command Line Interface Downloader

## Installation

Arxiv-downloader is available via PyPi:

``` sh
pip install arxiv-downloader
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

