# Monitoramento de Espaço em Disco com Telegram

**Descrição:**  
Este projeto é um script em Python que permite monitorar o espaço em disco de servidores Linux e enviar essas informações para um chat do Telegram.

## Funcionalidades

- **Listagem de Discos:**  
  Coleta informações sobre todos os discos montados, incluindo espaço total, usado e disponível.
  
- **Envio de Mensagens:**  
  As informações são enviadas diretamente para um chat do Telegram.
  
- **Divisão de Mensagens:**  
  Se as informações excederem o limite de caracteres do Telegram, a mensagem é dividida automaticamente.

## Requisitos

- Python 3
- Biblioteca `requests`

## Instalação

1. Clone este repositório ou baixe o código.
2. Instale a biblioteca `requests`:
   ```bash
   pip install requests
