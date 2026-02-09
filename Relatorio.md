## Atividade Avaliativa – Problema dos Leitores/Escritores com Sockets

Disciplina: Sistemas operacionais  
Semestre letivo: 2025.2  
Aluno: Maria Clara da Silva Melo

## 1. Título

**Implementação do Problema dos Leitores/Escritores utilizando Sockets em Python**

---

## 2. Contexto Inicial do Trabalho (Introdução)

O Problema dos Leitores/Escritores é um problema clássico da área de Sistemas Operacionais que aborda a concorrência no acesso a recursos compartilhados. Ele demonstra situações em que múltiplos processos ou threads precisam acessar uma mesma área de memória, sendo que leituras podem ocorrer simultaneamente, enquanto escritas exigem acesso exclusivo para garantir consistência dos dados.

Neste trabalho, o problema foi aplicado a um cenário de estacionamento com número limitado de vagas, acessado remotamente por múltiplos clientes por meio de sockets. O objetivo é demonstrar conceitos fundamentais como sincronização, exclusão mútua, prevenção de deadlock e comunicação entre processos.

---

## 3. Descrevendo a Solução em Python para o Problema de Leitores/Escritores

A solução foi implementada utilizando o modelo cliente-servidor. O servidor é responsável por gerenciar o recurso compartilhado (número de vagas disponíveis), enquanto os clientes realizam operações de leitura e escrita por meio de mensagens enviadas via socket.

As operações de leitura permitem que os clientes consultem a quantidade de vagas disponíveis, enquanto as operações de escrita permitem ocupar ou liberar vagas. Para evitar condições de corrida, o servidor utiliza mecanismos de exclusão mútua.

---

## 4. Implementando o Servidor e o Cliente

### 4.1 Servidor

O servidor utiliza sockets TCP para aceitar múltiplas conexões simultâneas. Cada cliente conectado é tratado em uma thread separada, garantindo concorrência. O número de vagas é protegido por um lock para assegurar exclusão mútua durante operações críticas.

Principais responsabilidades do servidor:

* Escutar conexões de múltiplos clientes
* Interpretar comandos recebidos
* Controlar o acesso ao recurso compartilhado
* Garantir consistência dos dados

### 4.2 Cliente

O cliente simula usuários concorrentes acessando o estacionamento. Foram criados 50 clientes que, de forma aleatória, realizam operações de consulta, ocupação ou liberação de vagas. Cada cliente se conecta ao servidor via socket e envia mensagens seguindo o protocolo definido.

---

## 5. Tratando Impasse (Deadlock)

### 5.1 Estratégia de Tratamento de Impasses

O sistema foi projetado para evitar deadlock por meio de uma estratégia simples e eficaz: o uso de um único lock para proteger a região crítica. Como não há aquisição de múltiplos recursos simultaneamente, elimina-se a possibilidade de espera circular.

### 5.2 Implementação do Tratamento de Impasse em Python

A implementação utiliza o objeto `Lock` da biblioteca `threading`. O lock é adquirido antes de qualquer operação de escrita ou leitura crítica e liberado imediatamente após o término da operação.

---

## 6. Execução do Código e Comportamento Observado

Durante a execução, foi possível observar múltiplos clientes acessando o servidor simultaneamente. As consultas de vagas retornaram valores consistentes, e as operações de ocupação e liberação respeitaram o limite máximo de vagas disponíveis.

Não foram observados comportamentos inconsistentes, como valores negativos ou superiores ao total de vagas, evidenciando que a sincronização foi implementada corretamente.

---

## 7. Conceitos de Concorrência Demonstrados

* **Sockets:** Comunicação cliente-servidor via TCP
* **Exclusão Mútua Remota:** Controle de acesso ao recurso no servidor
* **Sincronização:** Coordenação entre processos concorrentes
* **Prevenção de Deadlock:** Uso de lock único e ordem fixa
* **Condição de Corrida:** Evitada com uso adequado de locks

---

## 8. Considerações Finais

Este trabalho permitiu aplicar de forma prática conceitos fundamentais de Sistemas Operacionais, unindo concorrência e comunicação em rede. A solução proposta mostrou-se eficiente, segura e escalável para o cenário apresentado, atendendo a todos os requisitos estabelecidos na atividade avaliativa.
