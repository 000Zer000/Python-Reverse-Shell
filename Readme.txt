You can compile this code with pyinstaller (I recommend) because it allows usage of upx and byte-code encryption.

To make this harder to detect you can do below, (not limited to):

1. You can use encryption in pyinstaller

2. You can use droppers, (some of mine are available)

3. Also you may use UPX to compress the original executable to avoid detection

4. You can include it in a completely legit executable to make people feel less nervous ;)

5. You can also change the communication way (by default sends and receives with help of base85)

To connect to this reverse shell, You can use the handler.py file in this directory. Netcat won't work
