import os
is_heroku = os.environ.get('IS_HEROKU', None)

if is_heroku:
    from configurator import config

    # override config with heroku env vars
    config.bot.owner = int(os.environ.get('1916288033', None))
    config.bot.TOKEN = os.environ.get('2076434232:AAGT5Jc3-oRrUi2hAfIdORUyBLlNuX4zDj8', None)

    config.groups.main = int(os.environ.get('-1001230882554', None))
    config.groups.reports = int(os.environ.get('-1001531874578', None))
    config.groups.logs = int(os.environ.get('-1001531874578', None))