# grepper_py
Simple project on Python that allow you to found solutions from codegrepper and display them in terminal.
# One video will show this better that 1000 words:
https://user-images.githubusercontent.com/20460747/173205065-2be53958-5e0d-4664-a297-5dc3808bf2c9.mp4




P.S Why [Youtube](https://www.youtube.com/watch?v=IFlNKX4cl18), everything is simple I am using music from there, so I should use this platform.


# Todo
Project is not finished:
- [x] Codegrepper parsing
- [x] Linux support
- [x] CI/CD on GitHub actions
- [ ] Linux .deb / .rpm packages
- [ ] Windows binaries
- [ ] Stackoverflow parsing.

# How is made:
The project uses selenium with Chrome driver this is because all content is generated by javascript , so there is hard to scrap website using only requests or bs4. As an cli part the argparse was choosen. The binary is build using pyinstaller and makefile. Enjoy how you like it.

# How to install: 
There are three ways todo it:   
1. download binary and copy it to /usr/bin and  install config 
```
mkdir tmp && cd tmp 
wget https://github.com/alex5250/grepper_py/releases/download/v0.01-Linux/grepper_py
sudo cp grepper_py /usr/bin/grepper_py
wget https://raw.githubusercontent.com/alex5250/grepper_py/main/config_sample.ini 
sudo mkdir /etc/grepper.py
sudo cp config_sample.ini  /etc/grepper.py/config.ini
sudo chmod 777 /etc/grepper.py
cd ..
rm -rf tmp
```
2. Clone this repo and just run:
```
git clone https://github.com/alex5250/grepper_py.git
cd grepper_py
make build
make install
```
3. Use .deb /.rpm package (comming soon) 
4. Windows users please compile from sourses (binary comming later)
5. Unstable and fresh binaries can be downloaded from your github actions.


# I am software developer (how to perpare env for debug/develop this project)
Just run correct make command:
```
git clone https://github.com/alex5250/grepper_py.git
make develop
```



