<h1>Malware-ReverseShell</h1>
<p><b>This python malware-program is a presentation of how can reverse shell works.</b></p>
<p>Revershe shell is</p>
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
<h4>Server-client commands


<h2>Client Side Program</h2>
<h3>How does client-side python program work</h3>
