# This script integrates with Trivy to scan container images for vulnerabilities.

import subprocess

def scan_images(images):
    for image in images:
        print(f"Scanning image: {image}")
        subprocess.run(["trivy", "image", image])

if __name__ == "__main__":
    images_to_scan = ["nginx:latest", "alpine:3.17"]  # Replace with your images
    scan_images(images_to_scan)
