#Clientes (client.py)
#Simulam leitores (consultar vaga)
#Simulam escritores (pegar/liberar vaga)
#50 clientes concorrentes

import socket
import threading
import random
import time

HOST = "127.0.0.1"
PORT = 5000

NUM_CLIENTES = 50


def cliente(cliente_id):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        for _ in range(3):
            acao = random.choice(
                ["consultar_vaga", "pegar_vaga", "liberar_vaga"]
            )

            sock.sendall(acao.encode())
            resposta = sock.recv(1024).decode()

            print(f"[Cliente {cliente_id}] {acao} → {resposta}")

            time.sleep(random.uniform(0.3, 1.0))

        sock.close()

    except Exception as e:
        print(f"[Cliente {cliente_id}] Erro: {e}")


def main():
    threads = []

    for i in range(NUM_CLIENTES):
        t = threading.Thread(target=cliente, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Todos os clientes finalizaram.")


if __name__ == "__main__":
    main()
