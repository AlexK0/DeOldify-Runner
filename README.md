# DeOldify-Runner

Prepare all required stuff:
```
sudo apt update
sudo apt install python3-pip wget git ffmpeg libsm6 libxext6
```

Prepare a working place
```
mkdir Projects
cd Projects
git clone https://github.com/AlexK0/DeOldify-Runner.git
cd DeOldify-Runner
```

Setup [DeOldify](https://github.com/jantic/DeOldify):
```
./setup.sh
```

And run it:
- `[input/dir/with/images]` - specify an input directory with images
- `[output/dir]` - specify an output directory for colorized images
```
./run.sh [input/dir/with/images] [output/dir]
```

Note. For Windows systems disk `C:\\` in WSL can be found at `/mnt/c`, e.g.:
```
ls /mnt/c
```
