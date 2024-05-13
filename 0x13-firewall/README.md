# Firewall

In this project, I focused on web stack debugging, especially on configuring firewalls for my web servers. Using UFW (Uncomplicated Firewall), I ensured that my servers are protected while allowing legitimate traffic. I also learned to use telnet for testing server connectivity and was cautious about not blocking port 22/TCP to prevent SSH access issues.

# Tasks 📃

# 0. Block all incoming traffic bu

  + <u>[0-block_all_incoming_traffic_but](https://github.com/Heshbon/alx-system_engineering-devops/blob/master/0x13-firewall/0-block_all_incoming_traffic_but)</u>: Bash script that installs ufw firewall to block all incoming traffic except the following TCP ports 22, 443 and 80 on a web server.

# 1. Port forwarding

  + <u>[100-port_forwarding](https://github.com/Heshbon/alx-system_engineering-devops/blob/master/0x13-firewall/100-port_forwarding)</u>: ufw configuration file that configures a firewall to redirect port 8080/TCP to port 80/TCP
