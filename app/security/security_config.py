import secrets
import logging

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.core.config import get_app_settings
from app.model.security_user import SecurityUser

security = HTTPBasic()
settings = get_app_settings()

APP_USERNAME_AND_PASSWORD = settings.app_username_and_password
ADMIN_KEY_TOKEN = settings.admin_key_token
USER = "USER"
ADMIN = "ADMIN"


def get_current_active_user(credentials: HTTPBasicCredentials = Depends(security)):
    if APP_USERNAME_AND_PASSWORD:
        keys = APP_USERNAME_AND_PASSWORD.split(",")

        if len(keys) > 1:
            correct_username = secrets.compare_digest(credentials.username, keys[0])
            correct_password = secrets.compare_digest(credentials.password, keys[1])

            if correct_username and correct_password:
                return SecurityUser(role=USER)

    else:
        logging.warning("Received null Secure Key Token!")

    if ADMIN_KEY_TOKEN:
        correct_admin_username = secrets.compare_digest(credentials.username, ADMIN_KEY_TOKEN)
        correct_admin_password = secrets.compare_digest(credentials.password, ADMIN_KEY_TOKEN)

        if correct_admin_username and correct_admin_password:
            return SecurityUser(role=ADMIN)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
    )