# Космический Инстаграм

Данный проект позволяет скачивать фотографии с API [Hubble](http://hubblesite.org/api/documentation) и [SpaceX](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1) и выкладывать их в свой аккаунт в [Instagram](https://www.instagram.com).

### Как установить

* Python3 должен быть уже установлен. 
* Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

* Создайте файл `.env` в папке со скачанными скриптами, в котором должны быть указаны:
	* `INSTAGRAM_USERNAME` - аккаунт пользователя в [Instagram](https://www.instagram.com)
	* `INSTAGRAM_PASSWORD` - пароль от аккаунта

### Запуск

* Теперь Вы можете запустить:
 ```bash
 python fetch_spacex.py
 ```
 ```bash
 python fetch_hubble.py
 ```
 для скачивания фотографии с соответствующих сервисов. Фотографии будут сохранены в папке `images` в основном каталоге
* Для загрузки фото на Вашу страницу в [Instagram](https://www.instagram.com) запустите:
```
python upload_image.py
```
Скрипт преобразует фотографии в формат, необходимый для загрузки фото и выложит их. К уже загруженным фото будет добавлено расширение `.REMOVE_ME`, их можно свободно удалять
* Для повторного запуска скрипта `upload_image.py` необходимо удалить папку `config` в основном каталоге

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).