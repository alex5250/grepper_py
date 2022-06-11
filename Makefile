
default:
	echo 'specify task (develop,build,install)'
develop:
	./develop.sh
build:
	./build.sh
install:
	sudo cp ./dist/main /usr/bin/grepper_py
	
