# Reverse Shell
A reverse shell written in python, With encryption. 

A reverse shell is a kind of malware which allows you to bypass the firewall (reverse part does this trick) and get a shell from user's computer!

## Features

1. Using encryption talks are more secure

2. Ready to use handler

3. Customizable reverse shell

2. Interactive and non-interactive modes for the handler

3. Captures both STDOUT and STDERR

## Installing

Simply clone the repo:

```shell
git clone https://github.com/000Zer000/Python-Reverse-Shell
```

**Done**!

## Usage
At first, change the `HOST` to your IP in the script, Then you may want to also change the port, Then:

You can pass this script to your client (Hmm...Victim) and make him suffer (don't do that),
But to avoid AV detection, I recommend compiling it with pyinstaller (and using the byte encryption method)
Then compressing it with UPX, And finally you can use a dropper, or you can attach it to a trojan to do the transfer
Or even using several droppers, You know better then me to how to transfer it if you are here ;)

## handler.py
You cannot talk to this reverse shell with netcat unless you can decode base85 on your brain (which I'm sure you can't), 
This script is the handler which does:

1. Encodes and decodes base85 so don't worry

2. Non-interactive mode (`-x argument makes it execute a command then exit`)

3. Highly customizable. You can play with arguments to make it listen for UDP connections or even IPv6

4. Easy to use

5. Very stable

6. Also got help banner (try `--help`)

## Contacting me

You can reach me by emailing me (`000Zer000@protonmail.com`)

## Disclaimer
These scripts (`handler.py` and `reverse_shell.py`) were written only for educational purpose

## License

This repo is licensed under Apache 2.0, 
Read [COPYING](https://github.com/000Zer000/Python-Reverse-Shell/blob/main/COPYING) file for more info