#!/bin/sh

git clone https://github.com/jantic/DeOldify.git

pip3 install --user -r DeOldify/requirements.txt
pip3 install --user -r DeOldify/requirements-colab.txt
pip3 install --user -r DeOldify/requirements-dev.txt

mkdir -p DeOldify/models
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O DeOldify/models/ColorizeArtistic_gen.pth

cp _runner.py DeOldify/_runner.py
