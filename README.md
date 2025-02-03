# VocHub automated tests with Selenium

## Installation
* requirements: Python 3.8+, tested on 3.9 and 3.10
* `pip install -r requirements.txt`

## Configuration
we need to set up some env. vars for the script to work. like this:
```sh
export ENTERPRISE: [EDIT THIS]
export XIRCL= [EDIT THIS]
export FBAPI= [EDIT THIS]
export SURVEY= [EDIT THIS]
export SSO: [EDIT THIS]
export SMSTEST: [EDIT THIS]
export USERNAME=[EDIT THIS]
export PASSWORD=[EDIT THIS]
export ACCESS_CODE: [EDIT THIS]
export SSO_API_APPNAME: feedback
export SSO_API_SECRET: [EDIT THIS]
export SMS_GATEWAY_NAME: [EDIT THIS]
export SMS_SENDER_NAME: [EDIT THIS]
export SMS_PHONE_NUMBER: [EDIT THIS]
export SENDER_EMAIL=[EDIT THIS]
export MYSQL_HOST: [EDIT THIS]
export MYSQL_PORT: [EDIT THIS]
export MYSQL_USER: [EDIT THIS]
export MYSQL_PASS: [EDIT THIS]
export VOCACT_CASEALERT_URL: [EDIT THIS]
export VOCACT_CASEALERT_TOKEN: [EDIT THIS]
export BOUNCE_MAIL_ADDRESS: [EDIT THIS]
```

for convenient using with local env (and also for historic reasons) we support
fetching these variables from a YAML file.

for example, you can use a following `enterprise_settings/staging.yml`:

```yaml
enterprise: [EDIT THIS]
xircl: [EDIT THIS]
fbapi: [EDIT THIS]
survey: [EDIT THIS]
sso: [EDIT THIS]
smstest: [EDIT THIS]
username: [EDIT THIS]
password: [EDIT THIS]
access_code: [EDIT THIS]
sso_api_appname: [EDIT THIS]
sso_api_secret: [EDIT THIS]
sms_gateway_name: [EDIT THIS]
sms_sender_name: [EDIT THIS]
sms_phone_number: [EDIT THIS]
sender_email: [EDIT THIS]
mysql_host: [EDIT THIS]
mysql_port: [EDIT THIS]
mysql_user: [EDIT THIS]
mysql_pass: [EDIT THIS]
vocact_case_alert: [EDIT THIS]
vocact_case_alert_token: [EDIT THIS]
bounce_email_address: [EDIT THIS]
```

to process this config, you need to set `CLUSTER=stage`
(change this name if file is named differently).

## Running (example)
`pytest --driver Chrome`