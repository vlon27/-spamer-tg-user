#--Версия 1.0 спамер by vlon27
#--Спамер только по юзерам

from pyrogram import Client
import client_config as cfg
import time


def end(number_message, text_message, time_send):
    print(f"Рассылка завершена!\nВся инфа о рассылке:\n\nОтправлено всего: {number_message}\nТекст сообщения: {text_message}\nЗадержка: {time_send} сек")

def logs(chat, number_message, text_message_logs):
    logs_txt = open('logs.txt', 'w')
    logs_txt.write(f"{chat} | {text_message_logs}\n")

def message_send_true(client):
    #--сам спамер
    chats_all = open('files_chats.txt', 'r') #--сам файл с чатами
    number_message = 0 #--кол-во сообщений отправленно

    for chat in chats_all:
        print(f"чат: {chat}")
        client.send_message(chat, cfg.text_message)
        number_message = number_message + 1 #прибавить сообщение

        #--проверка если поставлено ограничение
        if cfg.time_send == 0:
            pass 
        else:
            time.sleep(cfg.time_send)
            #--end цикл

        text_message_logs = cfg.text_message
        logs(chat, number_message, text_message_logs)


    text_message = cfg.text_message
    time_send = cfg.time_send
    end(number_message, text_message, time_send)

    

def run():
    client = Client("session_user", api_id=cfg.api_id, api_hash=cfg.api_hash)
    client.start()
    client.send_message("me", "spamer run 1.0")
    #--запуск успешен

    #--основная конфигурация
    time.sleep(5)
    print("Ожидание включение...")
    message_send_true(client)

    

if __name__ == "__main__":
    run()