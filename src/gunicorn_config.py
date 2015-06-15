import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count()*2 + 1
certfile = '../lib/python3.4/site-packages/sslserver/certs/development.crt'
keyfile =  '../lib/python3.4/site-packages/sslserver/certs/development.key'
