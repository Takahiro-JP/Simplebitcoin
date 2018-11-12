from concurrent.futures import ThreadPoolExecutor
import socket
import os

def __handle_message(args_tuple):

conn, addr, data_sum = args_tuple
while True:
 data = conn.recv(1024)