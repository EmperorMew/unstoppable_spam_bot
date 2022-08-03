# :zap: Unstoppable Spam Bot

The only way to stop this, in my experience, is to physically block the number. Which is ineffective because the scripts can utilize infinite numbers.

# :floppy_disk: Installation
```
pip install plivo
pip install time
```

# :electric_plug: Getting Started



To Make API request, you need to create a RestClient and prvide it with authentication credentials (which can be found at Plivo https://manage.plivo.com/dashboard). 

Create an account, obtain your `API_Key` and `API_SECRET`, and add numbers to your account by clicking the number sign in the menu on the left. These numbers cost $0.50 per month and are unrestricted. They will simultaneously function for both the Call and Text scripts.


# :clapper: Usage

:eye_speech_bubble: I made this as simple as possible:
* :key: Add your keys to the config.py file in the proper format.
* :phone: Add the phone numbers you purchased to the callers var in the .py files. 
* :runner: Run script.

#### :bomb: phone_call_spam.py required terminal inputs once file is run.

* :dart: Enter victim's number be sure to add the country code
* :timer_clock: Enter a rest time between calls(in seconds) this should be at least 25 seconds for the call script.


#### :bomb: sms_spam.py required terminal inputs once file is run.

* :dart: Enter victim's number be sure to add the country code.
* :memo: Enter a message this will send one word per message and loop back.
* :timer_clock: Enter a rest time between sms messages(in seconds) you can set this to whatever you want.

# :person_with_probing_cane: DISCLAIMER
Developer shall not be held liable for any misuse or damage caused by unstoppable spam bot or any other component of this repository. This tool is for educational use only.
