# 🫂💌 socket-hugs

> Um servidor de mensagens, feito pra praticar redes e aprender com os erros de forma carinhosa 💟 

Este projeto é uma implementação simples de comunicação cliente-servidor usando sockets em Python. A ideia é permitir que os clientes enviem ou recebam recadinhos aleatórios, transformando o aprendizado em algo legal ✨

Criado como forma de reaprender com leveza depois de uma experiência frustrante com a matéria de redes I.

---

## ✨ Funcionalidades

- Escolher um apelido (para implementações futuras rs)
- Enviar uma mensagem para o servidor
- Adicionar o autor da mensagem (para casos de poemas ou provérbios)
- Receber uma mensagem aleatória do servidor
- Comunicação usando protocolo TCP
- Interface via terminal 

---

## ⚙️ Tecnologias

- Python 3.x
- Bibliotecas padrão utilizadas:
  - `socket`: para comunicação cliente-servidor via TCP
  - `threading`: para lidar com múltiplos clientes simultaneamente
  - `random`: para selecionar recadinhos de forma aleatória


---

## 🚀 Como usar

### 1. Clone este repositório

```bash
git clone git@github.com:gseovana/socket-hugs.git socket-hugs
cd socket-hugs
```

### 2. Inicie o servidor
```bash
python servidor.py
```

### 3. Em outro terminal, rode o cliente (quantos quiser)
```bash
python client.py
```

### 4. No cliente, escolha uma opção do menu
- Enviar uma mensagem
- Pegar uma mensagem
- Sair da aplicação

---

## 🌱 Coming soon...
- Ver usuários (nicks) conectados no servidor
- Salvar recados em arquivo .txt ou .json
- Categorizar mensagens (motivação, humor, amor…)
- Criar uma interface gráfica com Tkinter
- Criar uma versão web com Flask
- Login/usuários (Cada pessoa tem um nome e pode ver só seus recados ou logar e deixar bilhetes só pra alguém específico)

--- 

## 💖 Sobre
Este projeto foi desenvolvido como uma forma de praticar conceitos de redes de computadores, especificamente a comunicação via sockets em Python. A proposta surgiu depois de uma experiência frustrante com a entrega de um trabalho, em que os resultados não refletiram o esforço investido.

A ideia foi transformar essa frustração em um desafio pessoal, criando uma aplicação funcional que tivesse a ver comigo. O projeto simula um servidor de mensagens que permite o envio e o recebimento de recadinhos, um projeto simples que com certeza irá me auxiliar no de aprendizado técnico de uma matéria que me interessei muito.

Além de consolidar conhecimentos em sockets e comunicação cliente-servidor, ele também reflete a importância de manter a curiosidade e a motivação, mesmo quando os resultados imediatos não são os esperados 💪😼

---

<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGxpY3ZyeHgzYWc0dGJpcnI3NTZhM3Qwa3JqamdsbTczcXE4YXF0NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IbI0H8ie0rUMohFMbP/giphy.gif" width="250"/><br/>
  📌 Feito com carinho por Geovana ✨
</p>
