URL_SERVICE = "https://cnt-4cb4fe83-ec61-4793-95fb-26e1aae8d799.containerhub.tripleten-services.com"
DOC_PATH = "/docs/"
LOG_MAIN_PATH = "/api/logs/main/"
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
CREATE_USER_PATH = "/api/v1/users/"
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

