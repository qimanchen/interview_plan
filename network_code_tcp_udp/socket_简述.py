#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
套接字 socket
socket.socket(AddressFamily, Type)

AddressFamily: AF_INET,AF_INET
Type: SOCK_STREAM,SOCK_DGRAM
"""
import socket


# tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)