#!/usr/bin/env python3
"""
time_server.py

Time server: 연결 시 현재 로컬 시간을 한 줄 전송하고 닫음.
기본 포트: 5001
로그: 접속 시 Connected by ('IP', port) 출력
"""
from __future__ import annotations
import argparse
import datetime
import logging
import socket
import threading
import sys

def handle_client(conn: socket.socket, addr):
    try:
        logging.info('Connected by %s', addr)
        now = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        conn.sendall((now + '\n').encode('utf-8'))
    except Exception:
        logging.exception('error handling client %s', addr)
    finally:
        try:
            conn.close()
        except Exception:
            pass

def run_server(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        logging.info('[Time Server] Listening on %s:%d', host, port)
        while True:
            try:
                conn, addr = s.accept()
            except KeyboardInterrupt:
                logging.info('KeyboardInterrupt received, shutting down server.')
                break
            except Exception:
                logging.exception('accept failed')
                continue
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    finally:
        try:
            s.close()
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(description='TCP Time server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5001, help='Port to listen on (default:5001)')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        run_server(args.host, args.port)
    except Exception:
        logging.exception('server error')
        sys.exit(1)

if __name__ == '__main__':
    main()