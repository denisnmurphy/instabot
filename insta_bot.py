from instapy import InstaPy
import config
InstaPy(username=config.username, password=config.password).login()
