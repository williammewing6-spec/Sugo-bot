import telebot
from telebot import types

# التوكن الخاص بك
TOKEN = '8628819447:AAFv46sSe9K06U0y3ncuvPFji-pD2outrR0'
CHANNEL_ID = '@parissugo' 
bot = telebot.TeleBot(TOKEN)

def check_sub(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['creator', 'administrator', 'member']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('تحميل التطبيق 📥')
        btn2 = types.KeyboardButton('شروط الوكالة 📋')
        btn3 = types.KeyboardButton('قناة الشروحات 📢')
        btn4 = types.KeyboardButton('تواصل مع الوكيلة آية 👩‍💼')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "أهلاً بك في بوت وكالة سوغو! اختر من القائمة أدناه:", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        join_btn = types.InlineKeyboardButton("انضم للقناة أولاً ✅", url="https://t.me/parissugo")
        start_again = types.InlineKeyboardButton("تحقق من الانضمام 🔄", callback_data="check")
        markup.add(join_btn)
        markup.add(start_again)
        bot.send_message(message.chat.id, f"يجب عليك الانضمام لقناتنا {CHANNEL_ID} لتتمكن من استخدام البوت.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_callback(call):
    if check_sub(call.from_user.id):
        try: bot.delete_message(call.message.chat.id, call.message.message_id)
        except: pass
        start(call.message)
    else:
        bot.answer_callback_query(call.id, "أنت لم تشترك بالقناة بعد! ⚠️", show_alert=True)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'تحميل التطبيق 📥':
        bot.send_message(message.chat.id, "رابط تحميل تطبيق سوغو:\nhttps://play.google.com/store/apps/details?id=com.voicemaker.android")
    elif message.text == 'شروط الوكالة 📋':
        bot.send_message(message.chat.id, "شروط قبول الوكيل:\nيجب أن يكون لديك 5 مضيفات جاهزين للمباشرة مع حساب شاب مشحون بـ 5 دولار على الأقل.")
    elif message.text == 'قناة الشروحات 📢':
        bot.send_message(message.chat.id, "قناة الشروحات الرسمية:\nhttps://t.me/parissugo")
    elif message.text == 'تواصل مع الوكيلة آية 👩‍💼':
        bot.send_message(message.chat.id, "يمكنك التواصل مباشرة مع الوكيلة آية عبر واتساب:\nhttps://wa.me/963934171022")

if __name__ == "__main__":
    bot.infinity_polling()
    
