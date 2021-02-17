Before start, the application makes sure you have downloaded or cloned the chatRoom.
`https://github.com/c1c4/ChatRoom` and `https://github.com/c1c4/chatRoom-Backend`

You can create a virtual environment and after that on your terminal inside de project use: **pip install -r requirement.txt** to install the dependecies.

This project is created with flask and have kombu as our publisher.

For use, the message broker is on the requirements.txt
Install localy rabbitmq on you machine or build a docker_compose or what you prefere where you can enable **rabbitmq_web_stomp** and can access a websocket.
More info here https://www.rabbitmq.com/web-stomp.html

This Bot application has the purpose to get message commands like /stock=sotck_code
In this case, go to Sootq API, grab CSV, and change to a string with the pieces of information needed.
