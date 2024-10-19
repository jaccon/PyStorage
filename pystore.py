# -*- coding: utf-8 -*-
import requests
import subprocess
import os

# Configurações do Telegram
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')  # Adicione sua token do bot aqui
bot_chatID = os.getenv('TELEGRAM_CHAT_ID')    # Adicione seu chat ID aqui
max_message_length = 4096

def telegram_bot_sendtext(bot_message):
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
    response = requests.get(send_text)
    return response.json()

def get_disk_usage():
    df_output = subprocess.check_output(['df', '-h']).decode('utf-8')
    lines = df_output.splitlines()[1:]  # Ignora o cabeçalho
    disk_info = []
    
    for line in lines:
        parts = line.split()
        disk_name = parts[0]
        total_space = parts[1]
        used_space = parts[2]
        available_space = parts[3]
        disk_info.append(f"{disk_name}: Total: {total_space}, Usado: {used_space}, Disponível: {available_space}")
    
    return disk_info

def send_disk_usage(disk_info):
    disk_usage_message = "Disk Space Monitoring\n\n" + "\n".join(disk_info)
    
    # Dividir a mensagem se for muito longa
    for i in range(0, len(disk_usage_message), max_message_length):
        part = disk_usage_message[i:i + max_message_length]
        sendMessage = telegram_bot_sendtext(part)
        print(sendMessage)

# Obtém o uso do disco
disk_info = get_disk_usage()
send_disk_usage(disk_info)
