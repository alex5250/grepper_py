pip3 install virtualenv
virtualenv main
source ./main/bin/activate
pip3 install -r install.txt

echo 'all ready to build code.'

pyinstaller -F ./src/main.py --console 

