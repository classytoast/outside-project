from flask_mail import Message


def create_message(header: str,
                   body_html: str,
                   address: str) -> Message:
    """
    формирование сообщения для отправки

    :param header: Тема будущего письма
    :param body_html: Само сообщение в формате html
    :param address: email адрес, на который будет отправлено письмо
    :return: объект класса Message, с необходимыми данными для отправки
    """
    return Message(
        header,
        recipients=[address],
        html=body_html
    )
