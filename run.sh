#!/bin/bash
brew install ffmpeg
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py