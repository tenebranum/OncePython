DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        #'USER':'students_user',
        #'PASSWORD':'kava98banga',
        'USER':'root',
        'PASSWORD':'kava98banga',
        'NAME': 'students_db',
        'TEST':{
        	'CHARSET':'utf8',
        	'COLLATION':'utf8_general_ci',
        }
    }
}