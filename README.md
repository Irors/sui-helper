# sui-helper

### Практически идеальный скрипт для управления фермой sui аккаунтов, который позволит тебе:
# Описание - название модуля.
- Объединение 50(максимум за раз) объектов в один - `Merge coin`.
- Разбить один объект на два, с точным указанием баланса нового объекта - `Split coin`.
- Создать объект для оплаты комиссий - `Create gas object`.
- Посмотреть баланс нативной монеты на всех аккаунтах и записать результат в xlsx таблицу- `Balance`.
- Взаимодействовать с доступными dApps - `dApps`.
 И всё это делается ассинхронно(быстро)!

### Для запуска потребуется:
- Rust [установить](https://rustup.rs/)
- python >= 3.10

### Настройка.
1. Основная настройка в файле settings.py, описание там же.
2. Если нужно поменять/добавить объект sui_coin, то делать это в constant.py(так же там можно поменять задержку между транзакциями).
3. Кошельки указывать в `Wallet/private_keys.txt` один кошелёк = одна строка.

### Важно.
- На rpc ноды стоит ограничение по запросам, поэтому лучше не запускать много аккаунтов за ордин раз, иначе словите error 429.

