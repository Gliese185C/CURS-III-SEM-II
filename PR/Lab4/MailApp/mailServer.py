import smtplib
from email.mime.text import MIMEText
import poplib
import email
from email.header import decode_header
import chardet
from bs4 import BeautifulSoup


def sendMessage(to,sub,body):
    # Создаем объект SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Подключаемся к серверу и аутентифицируемся
    server.starttls()
    server.login("ababiy495@gmail.com", "orailbyarjvrotcr")

    # Создаем сообщение
    msg = MIMEText(body)
    msg['Subject'] = sub
    msg['From'] = 'ababiy495@gmail.com'
    msg['To'] = to

    # Отправляем сообщение
    server.sendmail("ababiy495@gmail.com", to, msg.as_string())

    # Закрываем соединение
    server.quit()

def takeMessages():

    # Указываем данные для подключения к серверу POP3
    pop_server = 'pop.gmail.com'
    pop_port = 995
    username = 'ababiy495@gmail.com'
    password = 'orailbyarjvrotcr'

    # Устанавливаем соединение с сервером
    server = poplib.POP3_SSL(pop_server, pop_port)
    server.user(username)
    server.pass_(password)

    # Получаем количество сообщений в ящике и их общий размер
    message_count, total_size = server.stat()
    print(f'Сообщений в ящике: {message_count}, общий размер: {total_size} байт')

    # Получаем список последних 30 сообщений
    messages = [server.retr(i) for i in range(message_count, max(message_count - 30, 0), -1)]
    list_of_emails = []
    # Разбираем сообщения
    for msg in messages:
        # создаем объект email.Message из байтового представления письма
        msg_str = b"\n".join(msg[1]).decode("utf-8")
        msg_obj = email.message_from_string(msg_str)

        # извлекаем информацию о теме, отправителе и теле письма
        subject = ""
        try:
            subject = decode_header(msg_obj["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
        except Exception as e:
            print(f"Error decoding subject: {e}")
            break

        sender = ""
        try:
            sender = decode_header(msg_obj["From"])[0][0]
        except Exception as e:
            print(f"Error decoding sender: {e}")
            break

        body = ""


        # обходим все части письма
        for part in msg_obj.walk():
            content_type = part.get_content_type()
            if content_type in ["text/plain", "text/html"]:
                try:
                    payload = part.get_payload(decode=True)
                    encodings = ["utf-8", "iso-8859-1", "windows-1252", "utf-16"]
                    for encoding in encodings:
                        try:
                            if content_type == "text/html":
                                soup = BeautifulSoup(payload.decode(encoding), "html.parser")
                                body += soup.get_text()
                            else:
                                body += payload.decode(encoding)
                            break
                        except UnicodeDecodeError:
                            pass
                except Exception as e:
                    print(f"Error: {e}")
                    continue
            elif content_type == "multipart/alternative":
                continue
            else:
                print(f"Ignoring content type: {content_type}")
                break

        # выводим информацию о письме
        list_of_emails.append([sender,subject.strip().replace('\n',''),body.strip().replace('\n','')])

    return list_of_emails
    # Закрываем соединение
    server.quit()

