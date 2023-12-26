from enum import Enum


class BOT_ANSWERS(str, Enum):
    greeting = "Приветствую! Я бот приюта для животных. Готовы ли вы представиться?"
    permission = (
        f"""Жаль, без этой информации нам будет сложнее держать вас в курсе последних новостей.\n"""
        """Может быть вы хотели получить ответ на ваш вопрос либо узнать дополнительную информацию о нас?"""
    )
    name = "Введите ваш имя:"
    surname = "Введите вашу фамилию:"
    email = "Введите ваш email:"
    phone = "Введите ваш номер телефона (в формате 7ХХХХХХХХХХ):"
    registration_message = (
        f"""Спасибо за регистрацию!\n"""
        """Теперь вы можете узнать дополнительную информацию о нас либо получить ответ на свой вопрос."""
    )
    shelter = "Информация о приюте"
    shelter_info = """
    Основная задача приюта — устройство наших подопечных в семьи, где о них будут заботиться. У каждого котика своя история и свой нелегкий путь, но всех их объединяет одно – желание и надежда обрести теплый дом, где их будут любить.
    «Преданное Сердце» – это про ответственное обращение с животными. «Преданное Сердце» - это про победу над низким уровнем культуры по отношению к братьям нашим меньшим. Про заботу и любовь. Про защиту и опеку. Про осознанное отношение человека к выбору питомца.
    Мы против эвтаназии, кроме тех случаев, когда животное страдает и помочь ему невозможно (по показаниям врача-ветеринара). Мы гордимся тем, что за каждую кошку боремся до конца и результат этого — счастливые фотографии питомцев, присылаемые нам их новыми хозяевами.
    За годы существования приюта больше 3000 подопечных уже разъехались по домам. У нас многоступенчатая система передачи животного в новую семью, включающая анкетирование будущих владельцев, собеседование и посещение квартиры представителями приюта. У нас заключаются договоры о передачи животных. Мы поддерживаем тесный контакт с новыми владельцами наших выпускников, регулярно получаем фото и видеоотчеты.
    Наряду с содержанием и уходом за здоровыми подопечными, приют специализируется на больных, травмированных животных. Мы оказываем помощь пожилым кошкам, инвалидам и кошкам, нуждающимся в паллиативной помощи. Ведь такие животные не понимают, что они чем-то отличаются от других. И им, не меньше, чем другим нужна помощь и забота. Они — тоже достойны жить.
    Животные со сложными диагнозами поступают в наш приют со всей страны, из регионов, где им не смогли оказать квалифицированную помощь, где не смогли найти дом, и где им грозила только улица.
        """
    questions = "Задать вопрос"
    questions_title = "Что бы вы хотели узнать?"
    faq = "Часто задаваемые вопросы"
    unique_question = "Задать свой вопрос"
    enter_unique_question = "Введите ваш вопрос"
    unique_question_reply = "Спасибо, мы свяжемся с Вами."
    cancel = "Отмена"
    yes = "Да"
    no = "Нет"
    try_again = "Попробовать ввести данные еще раз"
    validation_error = "Ошибка валидации, попробуйте еще раз"
    user_creation_error = "Ошибка создания пользователя, попробуйте еще раз"
    question_creation_error = "Ошибка создания вопроса, попробуйте еще раз"
    something_went_wrong = "Что-то пошло не так, попробуйте еще раз"


PAGINATION = 5
