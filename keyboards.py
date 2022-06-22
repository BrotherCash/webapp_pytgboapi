from telebot import types


def web_app_keyboard(): #создание клавиатуры с webapp кнопкой
    main_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #создаем клавиатуру

    web_app_main_url = types.WebAppInfo("https://web-app-test-shop.oml.ru/") #создаем webappinfo - формат хранения url
    web_app_main_button = types.KeyboardButton(text="Тестовая страница", web_app=web_app_main_url) #создаем кнопку типа webapp

    main_keyboard.add(web_app_main_button) #добавляем кнопки в клавиатуру

    return main_keyboard #возвращаем клавиатуру


# def webAppKeyboardInline(): #создание inline-клавиатуры с webapp кнопкой
#    keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру inline
#    webApp = types.WebAppInfo("https://telegram.mihailgok.ru") #создаем webappinfo - формат хранения url
#    one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp) #создаем кнопку типа webapp
#    keyboard.add(one) #добавляем кнопку в клавиатуру
#
#    return keyboard #возвращаем клавиатуру