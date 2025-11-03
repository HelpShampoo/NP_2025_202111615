#!/usr/bin/env python3
"""
number_server.py

Number server: 접속 시 고유 증가 정수(한 줄)를 클라이언트에 전송하고 닫음.
기본 포트: 5003
"""
from __future__ import annotations
import argparse
import logging
import socket
import threading
import sys

_counter = 0
_lock = threading.Lock()

def next_number() -> int:
    global _counter
    with _lock:
        _counter += 1
        return _counter

def handle_client(conn: socket.socket, addr):
    try:
        logging.info('[Number Server] Connected: %s', addr)
        n = next_number()
        conn.sendall((str(n) + '\n').encode('utf-8'))
    except Exception:
        logging.exception('error handling client %s', addr)
    finally:
        try:
            conn.close()
        except Exception:
            pass
        logging.info('[Number Server] Disconnected: %s', addr)

def run_server(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        logging.info('[Number Server] Listening on %s:%d', host, port)
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
    parser = argparse.ArgumentParser(description='TCP Number server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5003, help='Port to listen on (default:5003)')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        run_server(args.host, args.port)
    except Exception:
        logging.exception('server error')
        sys.exit(1)

if __name__ == '__main__':
    main()