Before start, the application makes sure you have downloaded or cloned the chatRoom.
`https://github.com/c1c4/ChatRoom` and `https://github.com/c1c4/chatRoom-Backend`

You can create a virtual environment and after that on your terminal inside de project use: **pip install -r requirement.txt** to install the dependecies.

You'll need to go to your terminal again and create a docker **docker run --rm -p 5672:5672 -p 8081:15672 rabbitmq:3-management**

This Bot application has the purpose to get message commands like /stock=sotck_code
In this case, go to Sootq API, grab CSV, and change to a string with the pieces of information needed.
