#!/usr/bin/env python3
"""
echo_server.py

Echo server: 클라이언트가 보낸 데이터를 읽어 서버 로그에 'Received: <msg>' 출력하고
같은 내용을 클라이언트에 그대로 반환(에코).
기본 포트: 5002
"""
from __future__ import annotations
import argparse
import logging
import socket
import threading
import sys

def handle_client(conn: socket.socket, addr):
    try:
        logging.info('[Echo Server] Connected: %s', addr)
        # 한 번의 송수신으로 끝낼 수도 있고, 여러번 처리하도록 루프 유지
        # 여기서는 클라이언트가 보낸 모든 바이트를 받아 에코 후 종료
        data = conn.recv(4096)
        if data:
            msg = data.decode('utf-8', errors='replace').rstrip('\n')
            logging.info('[Echo Server] Received: %s', msg)
            conn.sendall(data)
    except Exception:
        logging.exception('error handling client %s', addr)
    finally:
        try:
            conn.close()
        except Exception:
            pass
        logging.info('[Echo Server] Disconnected: %s', addr)

def run_server(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        logging.info('[Echo Server] Listening on %s:%d', host, port)
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
    parser = argparse.ArgumentParser(description='TCP Echo server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5002, help='Port to listen on (default:5002)')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        run_server(args.host, args.port)
    except Exception:
        logging.exception('server error')
        sys.exit(1)

if __name__ == '__main__':
    main()