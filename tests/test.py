import pytest
import shutil

import os
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

# Load the module
spec = spec_from_loader("arxiv-downloader", SourceFileLoader("arxiv-downloader", "bin/arxiv-downloader"))
arxiv_downloader = module_from_spec(spec)
spec.loader.exec_module(arxiv_downloader)

def test_parse_id_from_url():
    assert arxiv_downloader.parse_id("https://arxiv.org/abs/1234.5678") == "1234.5678", "Failed to extract ID from URL"
    assert arxiv_downloader.parse_id("https://arxiv.org/pdf/1234.5678") == "1234.5678", "Failed to extract ID from URL"
    assert arxiv_downloader.parse_id("https://arxiv.org/pdf/1234.5678.pdf") == "1234.5678", "Failed to extract ID from URL"

def test_parse_id_direct():
    assert arxiv_downloader.parse_id("1234.5678") == "1234.5678", "Failed to extract ID from direct input"

def test_invalid_input():
    with pytest.raises(SystemExit):
        arxiv_downloader.parse_id("invalid_input")
        arxiv_downloader.parse_id("123.5678")
        arxiv_downloader.parse_id("1234.678")
        arxiv_downloader.parse_id("12345.5678")
        arxiv_downloader.parse_id("1234.56788")


def test_download_article_integration():
    article_id = "2404.04349"  # An example article ID
    directory = "/tmp/arxiv-downloader-test/"
    try:
        # Attempt to download the article and its source
        arxiv_downloader.download_article(article_id, directory, download_source=True)

        # Verify the PDF was downloaded. List all files in directory and check if the PDF or the tar.gz file is present
        files = os.listdir(directory)
        assert any(file.endswith(".pdf") for file in files), "The PDF file was not downloaded."
        assert any(file.endswith(".tar.gz") for file in files), "The source file was not downloaded."
    finally:
        # Clean up: remove the directory and its contents
        shutil.rmtree(directory, ignore_errors=True)
