import os
import sys
import io
from bing_image_downloader import downloader

# Suppress all print statements by redefining print
class SilentPrinter:
    def __init__(self):
        self.original_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = open(os.devnull, 'w')  # Redirect to null

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self.original_stdout  # Restore original stdout

def download_images(query, num_images):
    with SilentPrinter():  # Use the context manager to silence output
        downloader.download(query, limit=num_images, output_dir=query, adult_filter_off=True, force_replace=False, timeout=60)

# Download images of Apple
download_images('Apple', 500)
