pip3 install virtualenv
virtualenv main
source ./main/bin/activate
pip3 install -r install.txt
echo 'all ready to debug code.'

echo 'create configs code.'
cat > /etc/grepper.py/config.ini << EOF
[URL]
base_url_suffix = https://www.codegrepper.com/search.php?q=
element_id = commando_selectable

[CLI]
chrome_installed_warring = off

EOF

echo 'ready'