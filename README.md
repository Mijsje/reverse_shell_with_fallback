This repo can create a Master-slave connection remotely
	it sends a heartbeat every minute with some info and tries to make a reverse shell connection (first TCP, then HTTP)
	
it also consist of some experimental reverse shells on ICMP
	
	
	Master:
		1) (443)Start the heartbeat receiver (sudo python /FindThePwnie/Heartbeat/HBserver.py)
		2) (4444)Start the listener you want
			i. TCP listener support multiple slaves (sudo python3 /FindThePwnie/TCP-shell/TCPshellServer.py)
			ii. HTTP is the only fallback right now (sudo python /FindThePwnie/HTTP-shell/HTTPshellServer.py)
	
	Slave:
		1) Start the fallbackmechanism with:
		Python FallBackMechanism.py Heartbeat/HBclient.py TCP-shell/TCPshellClient.py HTTP-shell/HTTPshellClient.py
		
		This will retest connection and send a heartbeat every 60 seconds
		
		
	Remarks:
		1) Might want to implement more fallbacks (UDP/DNS/ICMP) later, but these are unreliable
		2) Heartbeat only works on TCP connection
	
		
