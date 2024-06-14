# Web stack debugging #4

This project focuses on debugging a web server setup featuring Nginx under high load conditions using ApacheBench for benchmarking. Initially, the setup experienced a significant number of failed requests, prompting investigation and remediation steps. Through careful debugging and adjustments, including configuration tweaks and possibly script optimizations, I successfully reduced the failed requests to zero. This project underscores the importance of meticulous debugging practices and leveraging tools like ApacheBench and server logs for effective troubleshooting in web stack management.

# Tasks

# 0. Sky is the limit, let's bring that limit higher

  + <u>[0-the_sky_is_the_limit_not.pp]()</u>: Puppet file that increases the amount of traffic an Apache web server can effectively handle.

# 1. User limit

  + <u>[1-user_limit.pp]</u>: Puppet file that changes the operating system configuration so that it is possible to login with the user holberton and open a file without error.
