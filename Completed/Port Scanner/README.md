# Port Scanner
What is Port Scanning?
  
  Port scanning is a method of determining which ports on a network are open and could be receiving or sending data. It is also a process for sending packets to specific ports on a host and analyzing responses to identify vulnerabilities.

What is a Port Scanner?

  A port scanner is a tool used to identify open ports and services on a networked system.

How does a Port Scanner Work?

  Scanning Process:

  Send Probe Requests: The scanner sends requests to various ports on the target system. These requests can be of different types, such as TCP SYN packets (used in SYN scan), UDP packets, or others depending on the scanning method.

  Receive Responses: The scanner then listens for responses from the target system. The responses indicate the status of the ports:

  Open: The port is actively accepting connections. The target system responds positively to the scan.

  Closed: The port is not open. The system acknowledges the request but indicates that the port is closed.

  Filtered: The port status cannot be determined because the response is blocked by a firewall or other security mechanism.

  Types of Scans:

  TCP Connect Scan: Completes the TCP handshake with the target port. If the connection is established, the port is open.

   SYN Scan: Sends SYN packets and checks for SYN-ACK responses. This method is often stealthier because it doesn’t complete the handshake.

  UDP Scan: Sends UDP packets and waits for responses or timeouts to determine port status, which can be slower and less reliable due to the nature of UDP.

  Service Version Detection: After identifying open ports, some scanners can probe these ports further to determine the version of the services running.

  Output and Analysis:

  Port List: The scanner generates a list of open, closed, or filtered ports along with associated services and versions if detected.

  Security Assessment: The information gathered helps in assessing the security posture of the target system, identifying potential vulnerabilities, and planning further actions.