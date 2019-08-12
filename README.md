# Dentist Chatbot Service
> A skeleton of dentist chatbot service

## Deployment Instruction
To build the dentist service
```sh
$ cd dentist_service/ && docker build -t dentist_service . 
$ docker run -p 5200:5200 dentist_service
```
To build the timeslot service
```sh
$ cd timeslot_service/ && docker build -t timeslot_service .
$ docker run -p 5100:5100 timeslot_service
```

## How To Run the Application

 - Complete the deployment instruction above
 (If you haven't install docker, you can run in terminal as well, Here's the instruction)
	 ```sh
	 $ cd dentist_service/ && pip3 install requirements.txt
	 $ python3 -m swagger_server
	```
	Open another tap or terminal window
	```sh
	$ cd timeslot_service/ && pip3 install requirements.txt
	$ python3 -m swagger_server
	```
 - Run the chatbot service
	 ```sh 
	 $ cd chatbot/ && pip3 install -r requirements.txt
	 $ python3 -m swagger_server
	 ```
 - Install front end dependency
	 ```sh
	 $ cd botui && npm install
	 ```
 - open the chatbot.html file in the Chrome and you should see the content