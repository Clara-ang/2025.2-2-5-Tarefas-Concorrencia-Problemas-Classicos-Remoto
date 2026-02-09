# Servidor (server.py)
# Mantém o número de vagas (recurso compartilhado)
# Usa Lock para exclusão mútua (escrita exclusiva)
# Atende vários clientes simultaneamente com threads 

import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

TOTAL_VAGAS = 10
vagas_disponiveis = TOTAL_VAGAS

lock = threading.Lock()


def tratar_cliente(conn, addr):
    global vagas_disponiveis
    print(f"[+] Cliente conectado: {addr}")

    try:
        while True:
            mensagem = conn.recv(1024).decode()

            if not mensagem:
                break

            if mensagem == "consultar_vaga":
                with lock:
                    resposta = f"Vagas disponíveis: {vagas_disponiveis}"
                conn.sendall(resposta.encode())

            elif mensagem == "pegar_vaga":
                with lock:
                    if vagas_disponiveis > 0:
                        vagas_disponiveis -= 1
                        resposta = "Vaga ocupada com sucesso"
                    else:
                        resposta = "Estacionamento lotado"
                conn.sendall(resposta.encode())

            elif mensagem == "liberar_vaga":
                with lock:
                    if vagas_disponiveis < TOTAL_VAGAS:
                        vagas_disponiveis += 1
                        resposta = "Vaga liberada"
                    else:
                        resposta = "Erro ao liberar vaga"
                conn.sendall(resposta.encode())

            else:
                conn.sendall("Comando inválido".encode())

    except Exception as e:
        print(f"[ERRO] {addr}: {e}")

    finally:
        conn.close()
        print(f"[-] Cliente desconectado: {addr}")


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("=" * 50)
    print("Servidor de Vagas iniciado")
    print("=" * 50)

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
