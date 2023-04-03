import logging

class SecurityManager:
    def __init__(self):
        self.authorized_users = {
            "user1": ["resource1"],
            "user2": ["resource2", "resource3"]
        }

    def is_authorized(self, user, resource):
        if user in self.authorized_users:
            if resource in self.authorized_users[user]:
                return True
        return False


class AccessControlDecorator:
    def __init__(self, security_manager):
        self.security_manager = security_manager

    def is_authorized(self, user, resource, action):
        if action == "read" and not self.security_manager.is_authorized(user, resource):
            return False
        return True


class LoggingDecorator:
    def __init__(self, access_control):
        self.access_control = access_control

    def is_authorized(self, user, resource, action):
        try:
            return self.access_control.is_authorized(user, resource, action)
        except Exception as e:
            logging.error(f"Ошибка проверки доступа: {e}")
            return False


security_manager = SecurityManager()
access_control = AccessControlDecorator(security_manager)
decorated_security_manager = LoggingDecorator(access_control)

# Проверка прав доступа к чтению ресурса для пользователя user1 и resource1
if decorated_security_manager.is_authorized("user1", "resource1", "read"):
    print("Доступ разрешен")
else:
    print("Ошибка доступа")

# Проверка прав доступа к записи ресурса для пользователя user2 и resource2
if decorated_security_manager.is_authorized("user2", "resource2", "write"):
    print("Доступ разрешен")
else:
    print("Ошибка доступа")