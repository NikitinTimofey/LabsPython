ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False

    for word in ignore:
        if word in command:
            return True
    return ignore_command


def config_to_dict(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает словарь:
    - Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    - Если у команды верхнего уровня есть подкоманды,
    они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
    - Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    """
    conf_dict = {}
    with open(config, 'r') as conf_file:
        for command in conf_file:
            if command.startswith('!') or ignore_command(command, ignore):
                continue
            if not command.startswith(' '):
                current_key = command.strip()
                conf_dict[current_key] = []
            else:
                conf_dict[current_key].append(command.strip())

    return conf_dict

print(config_to_dict('config_sw1.txt'))
