# Load balancer

In this task, I continued on developing the web server configuration that was started in project 0x0B .  Two more servers were provided to me; one was used to duplicate my original server's Nginx setup, and the other was used to set up a HAproxy load balancer to control both web servers.

# Tasks 📃

# 0. Double the number of webservers

  + <u>[0-custom_http_response_header](https://github.com/Heshbon/alx-system_engineering-devops/blob/master/0x0F-load_balancer/0-custom_http_response_header)</u>: Bash script that configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02).

	- The name of the custom HTTP header must be X-Served-By.

	- The value of the custom HTTP header must be the hostname of the server Nginx is running on.

# 1. Install your load balancer

  + <u>[1-install_load_balancer](https://github.com/Heshbon/alx-system_engineering-devops/blob/master/0x0F-load_balancer/1-install_load_balancer)</u>: Bash script that install and configure HAproxy on the lb-01 server.

    - Requests are distributed using roundrobin algorithm.

    - HAproxy is managed via an init script.
