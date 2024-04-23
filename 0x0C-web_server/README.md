# Web server

In this project, I learned how web servers work and began using one. Additionally, I completed a basic configuration of the server using Nginx.

# Tasks 📃

# 0. Transfer a file to your server

  + <u>[0-transfer_file]()</u>: Bash script that transfers a file from our client to a server.

  + Accepts 4 parameters:

	+ The path to the file to be transferred.

	+ The IP of the server we want to transfer the file to.

	+ The username scp connects with.

	+ The path to the SSH private key that scp uses.

# 1. Install nginx web server

  + <u>[1-install_nginx_web_server]()</u>: Bash script that configures a new Ubuntu machine with Nginx.

	+ Nginx should be listening on port 80.

	+ When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!

# 2. Setup a domain name

  + <u>[2-setup_a_domain_name]()</u>: Domain name set up.

# 3. Redirection

  + <u>[3-redirection]()</u>: Bash script that configures a new Ubuntu machine with Nginx.

# 4. Not found page 404

  + <u>[4-not_found_page_404]()</u>: Bash script that configures a new Ubuntu machine with Nginx.
