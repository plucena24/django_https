import multiprocessing

bind = "127.0.0.1:8000"

workers = multiprocessing.cpu_count()*2 + 1

#The .crt and .key here must be exactly the same as in the nginx.conf or else 501
certfile = '/home/NAThompson/jeremiahcornsticks.com.ssl/jeremiahcornsticks_com.crt'
keyfile  = '/home/NAThompson/jeremiahcornsticks.com.ssl/jeremiahcornsticks.com.key'

# sslserver generates self-signed keys for testing:
#certfile = '../lib/python3.4/site-packages/sslserver/certs/development.crt'
#keyfile =  '../lib/python3.4/site-packages/sslserver/certs/development.key'
