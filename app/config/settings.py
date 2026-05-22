from dotenv import load_dotenv 
import os

load_dotenv()

app_name = os.environ.get('APP_NAME')
app_version = os.environ.get('APP_VERSION')
admin_user = os.environ.get('ADMIN_USER')


def variables_entorno():
    print(app_name)
    print(app_version)
    print(admin_user)