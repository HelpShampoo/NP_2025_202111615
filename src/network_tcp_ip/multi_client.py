#!/usr/bin/env python3
"""
multi_client_seq.py

서버 IP를 한 번 입력받아 아래 순서대로 자동으로 호출합니다:
  1) Time Server (포트 5001) -> 서버로부터 시간 수신 후 출력
  2) Echo Server (포트 5002) -> 사용자로부터 에코할 메시지 입력 -> 서버에 전송 후 응답 출력
  3) Number Server (포트 5003) -> 서버로부터 번호 수신 후 출력

기본 포트: 5001 / 5002 / 5003
타임아웃: 8초
"""
from __future__ import annotations
import socket
import sys

TIME_PORT = 5001
ECHO_PORT = 5002
NUMBER_PORT = 5003
CONNECT_TIMEOUT = 8  # seconds

def recv_all(sock: socket.socket, bufsize: int = 4096) -> bytes:
    parts = []
    while True:
        chunk = sock.recv(bufsize)
        if not chunk:
            break
        parts.append(chunk)
    return b''.join(parts)

def do_time(ip: str):
    print()
    print("[1] Time Server (5001)")
    try:
        with socket.create_connection((ip, TIME_PORT), timeout=CONNECT_TIMEOUT) as s:
            data = recv_all(s)
            print(f"Response from server ({TIME_PORT}): {data.decode('utf-8').rstrip()}")
    except Exception as e:
        print(f"Error connecting to {ip}:{TIME_PORT} -> {e}", file=sys.stderr)

def do_echo(ip: str):
    print()
    print("[2] Echo Server (5002)")
    msg = input("Echo할 메시지를 입력: ")
    try:
        with socket.create_connection((ip, ECHO_PORT), timeout=CONNECT_TIMEOUT) as s:
            s.sendall(msg.encode('utf-8'))
            data = recv_all(s)
            print(f"Response from server ({ECHO_PORT}): {data.decode('utf-8').rstrip()}")
    except Exception as e:
        print(f"Error connecting to {ip}:{ECHO_PORT} -> {e}", file=sys.stderr)

def do_number(ip: str):
    print()
    print("[3] Number Server (5003)")
    try:
        with socket.create_connection((ip, NUMBER_PORT), timeout=CONNECT_TIMEOUT) as s:
            data = recv_all(s)
            print(f"Response from server ({NUMBER_PORT}): {data.decode('utf-8').rstrip()}")
    except Exception as e:
        print(f"Error connecting to {ip}:{NUMBER_PORT} -> {e}", file=sys.stderr)

def main():
    print("서버 IP 입력 (예: 192.168.0.10). 빈칸이면 'localhost' 사용:")
    ip = input().strip()
    if not ip:
        ip = 'localhost'

    # 자동 순차 실행: Time -> Echo -> Number
    do_time(ip)
    do_echo(ip)
    do_number(ip)

if __name__ == '__main__':
    main()