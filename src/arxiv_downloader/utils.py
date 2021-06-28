#!/usr/bin/env python3

import os
import argparse
import arxiv


def url_to_id(url: str) -> str:
    """
    Parse the given URL of the form `https://arxiv.org/abs/1907.13625` to the id `1907.13625`.

    Args:
        url: Input arxiv URL.

    Returns:
        str: ArXiv article ID.
    """
    # Strip filetype
    if url.endswith(".pdf"):
        url = url[:-4]

    return url.split("/")[-1]


def check_out_dir(directory: str):
    """Check if the output directory exists. If not, ask the user to mkdir."""
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist. Create? [y/n] ", end="")
        ans = input().lower().strip()
        if ans == "y":
            os.makedirs(directory)
        elif ans == "n":
            print("Exiting now.")
            exit(1)
        else:
            print("Invalid input. Exiting now.")
            exit(1)



def download(article_id, directory: str, source:bool):

    # TODO: add checks for valid urls
    check_out_dir(directory)


    # Download
    result = arxiv.Search(id_list=[article_id])
    result = [res for res in result.get()]
    result = result[0]
    print(f'Starting download of article: "{result.title}" ({article_id})')
    path = result.download_pdf(dirpath=directory)

    print(f"Download finished! Result saved at:\n{path}")

    if source:
        print(f'Starting download of article source files: "{result.title}" ({article_id})')
        result.download_source(dirpath=directory)
