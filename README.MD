# StressTestingStore
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Stress/Load/API test suite using Locust(python) to generate thousands of API requests in seconds.
The application-under-test(AUT) is https://www.demoblaze.com/ , a fully functional ecommerce store.
Key Features:
- Containerized w/ Docker
- Tests for an influx of registered users(login logic, adding items to cart, purchasing cart)
- Tests for an influx of unregistered users(just browsing, simple GET requests)

## QUICK GUIDE
- 8731 GET requests in 20 seconds [Watch Original gif](https://gyazo.com/225384ea9f5485083128afabf1812898)
![video alt](https://i.gyazo.com/225384ea9f5485083128afabf1812898.gif)

## SETUP
- Clone the repo
`git clone https://github.com/BradleyPelton/StressTestingStore`
- Download the image
`sudo docker pull grubykarol/locust`
- Build and run a container
```
sudo docker run --name jbscontainer --hostname jbscontainer \
-e ATTACKED_HOST=https://demoblaze.com \
-e "LOCUST_OPTS=--no-web -c 100 -r 10 --run-time 20s" \
-e "LOCUST_FILE= /locust/justbrowsingswarm.py" \
-v /home/mavric/StressTestingStore:/locust \
grubykarol/locust
```


### WHY NOT JMETER?
- "JMeter is thread-bound. This means for every user you want to simulate, you need a separate
thread. Needless to say, benchmarking thousands of users on a single machine just isn’t feasible."
- Jmeter requires Java or Jython

### NOTES TO AUTHOR: Best practices checklist
- Make sure every request has a timeout
- "It’s a good practice to set connect timeouts to slightly larger than a multiple of 3,
    which is the default TCP packet retransmission window."

### More notes

NAME OF THE GAME: Performance Testing, Load Testing, API TESTING

Great skills I'm going to learn along the way:
- Load testing
- CONCURRENCY
- BENCHMARKING
- HTTP PROXY
- Simultaneous web and mobile user load testing 
- GOOD TIME TO LEARN K8s/DOCKER FOR LINUX
- WEBSOCKET TESTING IS ABOUT AS COMPELX AS IT GETS. CUSTOM CLIENT NEEDS TO BE WRITTEN.
https://docs.locust.io/en/latest/testing-other-systems.html
