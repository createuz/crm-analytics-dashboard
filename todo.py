task = '''
        Postman: Analytic >>>>>>>
        crm-analytics-dashboard

        Ro'yxatdan o'tish (register):
        Method: POST
        URL: http://localhost:8000/users/register
        Body (form-data):
        username: testuser
        email: test@example.com
        password: testpassword
        Parolni tiklash havolasini yuborish (reset_password):

        Method: POST
        URL: http://localhost:8000/users/reset_password
        Body (form-data):
        email: test@example.com
        Parolni tiklash (reset_password_confirm):

        Method: POST
        URL: http://localhost:8000/users/reset_password_confirm
        Body (form-data):
        token: <token_value> (bu tokenni email yuborish qadamida olganiz)
        uid: <uid_value> (bu uid ni email yuborish qadamida olganiz)
        password: newpassword
        Chiqish (logout):

        Method: POST
        URL: http://localhost:8000/logout
'''