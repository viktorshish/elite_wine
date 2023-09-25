# Новое русское вино

Сайт магазина авторского вина **"Новое русское вино"**.

## Как установить

- Скачайте код
- Для изоляции проекта рекомендуется развернуть виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
- В корне проекта создать excel файл **wine.xlsx** с информацией по продукции:
  
[wine.xlsx](https://github.com/viktorshish/elite_wine/files/12718221/wine.xlsx)

  
## Использование

- Запустите сайт командой 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
![MySite](https://github.com/viktorshish/elite_wine/assets/108957333/492fe190-9e22-4852-8736-49f62e0537b3)
- На сайте отобразится продукция, перечисленная в файле **wine.xlsx**:
![Productions](https://github.com/viktorshish/elite_wine/assets/108957333/80ed6ab3-7ff8-4063-adfb-fec822b43ef0)
 
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
