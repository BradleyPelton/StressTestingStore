



"""ATTACK (an approved) PUBLIC WEBSITE OR ATTACK MY OWN WEBSITE DEPLOYED VIA GCP"""


-



- Simultaneous web and mobile user load testing 


https://github.com/locustio/locust
https://www.blazemeter.com/blog/locust-assertions-a-complete-user-manual
https://www.blazemeter.com/blog/how-to-run-locust-with-different-users
https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module


<!-- # Running Locust on Windows should work fine for developing and testing your load testing scripts.
# However, when running large scale tests, it’s recommended that you do that on Linux machines,
# since gevent’s performance under Windows is poor.

# Every HTTP connection on a machine opens a new file (technically a file descriptor). Operating
# systems may set a low limit for the maximum number of files that can be open. If the limit is
# less than the number of simulated users in a test, failures will occur. -->


PROXY 