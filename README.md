# Miniproject #3

## Hello, Antony😎

Ось тобі summary по тому проекті

## Задумка

<div style="background: linear-gradient(to right, #293b2d,rgb(15, 67, 25)); padding: 5px; border-radius: 10px;">

Це вже третя практика з пайтону в цьому семестрі. Сама задумка проекту - сайт, на якому люди зможуть купувати/продавати б/у речі.
Він включає можливість додавання нових товарів на сайт і створення замовлень, які зберігаються в базі даних. Також
Pydatic моделі для валідації (перевірки того, що всі елементи додаються правильно і по коректній схемі).

Більш детальне пояснення всіх моментів і таск можете подивитися тут:

<a href="https://edu.goiteens.com/learn/17539896/21288373/21288394/training" style="font-size: 18px">Python Miniproject #3</a>

</div>

## Схема проекту

Проект ділиться на дві основні частини:
* Back-end
* Front-end

Бек-частина (тобто сам API) тут написана на `FastAPI`. 
Фронт-енд реалізований з допомогою бібліотеки `ReactJS`, яка дозволяє створювати легкі додатки на основі мови програмування `JavaScript`.
База даних `PostgreSQL`, зв'язок з якою відбувається з допомогою:
* `sqlalchemy` - ORM бібліотека, яка дозволяє створювати моделі для реляційних (SQL) баз даних у вигляді Python-класів
* `alembic` - інструмент відстеження і контролю міграціями реляційних баз даних, який йде у св'язці з sqlalchemy

В директорії `app/` знаходиться основна частина додатку, а саме:
1. FastAPI-based API і ендпоінти
2. Pydantic схеми (`/schemas/`)
3. Моделі бази даних (`/models/`)
4. Різні утиліти, тобто функції/класи які часто використовуються в проекті (`/utils/`)

В папці `frontend/` знаходиться візуальна частина апки, тобто фронтенд.



## Як правильно запустити та використовувати проект

### Запуск

* Спочатку потрібно установити всі бібліотеки і фреймворки які тут використовуються.

<div style="background-color: #333; padding: 5px; border-radius: 10px;">

#### Back-end
- Оскільки тут є `pyproject.toml` файл в якому описані всі додаткові залежності бек-енд частини, 
ти можеш просто в терміналі корневої папки 
написати команду `poetry install`, яка завантажить всі використані ліби. 

Потім, коли всі залежності установлені, для запуску API потрібно написати команду:
#### `uvicorn app.main:app --reload --port 8000`
#### <span style="color: red;">УВАГА: </span> значення `--port` обов'язково установлювати саме `8000`, тому що саме на цей порт виконує запит фронт-енд частина

</div>

<hr>

<div style="background-color: #333; padding: 5px; border-radius: 10px;">

#### Front-end

Тепер треба встановити пакети і на фронті. Тут також є аналог poetry файлів, це `package.json` і `package-lock.json`, і в першому з цих файлів описані всі дод. біліотеки в майже такому ж вигляді як на бек стороні. Щоб завантажити їх, потрібно:
* перейти в термінал цієї папки: `cd frontend/`
* написати тут команду для встановлення: `npm install`.

потім пакетний менеджер npm установить ліби. 

для запуску потрібно буде в цьому ж терміналі написати дві команди:
1. #### `npm build`

2. #### `npm run dev`

npm build потрібно писати тільки один раз, вона типу вибудовує проект. npm run dev його вже остаточно запускає.
після цього ритуалу npm запустить ваш проект на url `localhost:5173`
</div>


#### Використання

<div style="background-color: #333; padding: 5px; border-radius: 10px;">

Тут не вийшло зробити все завдання повністю, тому що деякі моменти я просто не знав як реалізувати на фронті, але загалом тут логіка така,
що якщо ти не автентифікований то воно тебе не пропустить. В юзера на фронті є вибір: або створити новий акаунт або увійти в існуючий. 
незалежно що він вибере, коли він увійде то на головній сторінці буде виведено привітання з ім'ям, яке `взято з бази даних`. потім, тільки якщо у користовача тип `seller` він зможе додавати нові продукти. якщо ж ні - то в нього просто не буде кнопки. коли людина ввела всі дані і вони валідні, то продукт додається в БД.

</div>

<hr>

### Inspired by `Lil Uzi Vert`