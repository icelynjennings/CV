# Results
1. Written in Go
2. Uses concurrency
3. Listens 17873 TCP
4. Must connect with a receiving client socket
5. Says "Hello world!" on `/` to all request types on RFC 202 Accepted
6. Says "Well done!" on `/` to all request types on RFC 200 OK
7. Returns status code only on `/health` to all requests types.
8. I have no idea what the string argument does. I guessed it is supposed to be the path to a filesystem UDS socket, but that doesn't seem to be the case...?
9. Repository: https://github.com/trayio/syseng-test
# Steps taken:
### Run the binary
```
wget https://s3.amazonaws.com/cdn.tray.io/static/hr/hiring/tests/legacy
chmod +x legacy
./legacy x # Timeout.
./legacy xxxx # Executed for longer, eventually timeout.
./legacy xxxx yyyy # Same behaviour.
```
For convenient testing, I started re-running the binary automatically:
```
watch -t -n 3 ./legacy xxxx
```
### Is it listening on any ports?
```
sudo netstat -tulpn | grep legacy
# tcp6       0      0 :::17873                :::*                    LISTEN      13916/./legacy
```
Checking the endpoints:
```
watch -t -n 0.1 curl -s localhost:17873 | head -n 1 # Hello world!
watch -t -n 0.1 curl -s localhost:17873/health | head -n 1 #
watch -t -n 0.1 curl -s -I localhost:17873 | head -n 1 # HTTP/1.1 202 Accepted
watch -t -n 0.1 curl -s -I localhost:17873 | head -n 1 # HTTP/1.1 202 Accepted
```
Maybe it responds to OPTIONS?
```curl -s -X OPTIONS localhost:17873```
Nothing.

### Is it opening any files?
```
ls /var/log/ | grep legacy
```
No server logs.
```
watch -t -n 0.1 lsof -c legacy
# legacy  14937 administrator    3u     IPv6 2667385      0t0       TCP *:17873 (LISTEN)
```
So we have an IPv6 socket being opened.

### Socket 
```
# Maybe the string argument refers to a UDS socket?
python -c "import socket; s = socket.socket(s.AF_UNIX); s.bind('somesocket')"
./legacy somesocket
```
Let's try connecting with a client.
```
#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 17873))
s.send("somesocket".encode())
s.recv(1024)
s.close()
```
Result:
```
watch -t -n 0.1 curl -s localhost:17873 | head -n 1 # Well done!
watch -t -n 0.1 curl -s localhost:17873/health | head -n 1 #
watch -t -n 0.1 curl -s -I localhost:17873 | head -n 1 # HTTP/1.1 200 OK
watch -t -n 0.1 curl -s -I localhost:17873 | head -n 1 # HTTP/1.1 200 OK
```
Success! 

### Signals
Used `SIGKILL` `SIGTERM` `SIGINT`. 

`SIGINT` failed to properly close the process. I opened the binary again regardless. The output was:
```
panic: listen tcp :17873: bind: address already in use

goroutine 1 [running]:
main.main()
	/home/luka/projects/tray.io/syseng-test/src/github.com/trayio/syseng-test/main.go:110 +0x57d
```
1. The program is written in **Go**
2. It is using concurrency. 
3. The best way to proceed from this point onward would be to contact the owner of the presumably private repository https://github.com/trayio/syseng-test asking for the source code and documentation.

### Reverse engineering / memory analysis
1. Could not analyse memeory via `go tool pprof`, it seems the program doesn't use this library.
2. Maybe there are function signatures / linker references to libraries inside the binary. Send the output of `cat legacy` to a reverse engineering expert.
