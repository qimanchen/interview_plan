# python运行必须文件
# rpc实现步骤
Python
Python Requirements
Avro is available from pypi

It seems that the Avro python egg requires snappy:

sudo apt-get install libsnappy-dev # 'brew install snappy' if you're on Mac
sudo pip install python-snappy
sudo pip install avro
Python - start_server.py
Run this first to start the python avro Mail server.

the MailResponder class implements the Mail protocol defined in mail.avpr
main starts the server which implements the Mail service (Mail/MailResponder)
Python - send_message.py
You'll see that the structure of the python code is similar to the java/ruby source.

send_message.py

the main function takes three arguments; to, from and body of the message. After the server is started a Mail client is created, attached to the service, and used to send a "Message", the result of the RPC call is printed to the console.
Run the python
From the rpc directory run:

./start_server.py

then in a separate shell run:

./send_message.py avro_user pat Hello_World
