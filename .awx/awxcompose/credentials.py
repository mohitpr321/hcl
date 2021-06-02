DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "password",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "SV9BNUsuYyxxRjZWLm00OmNrYWNwUWJweS1DeXkwVS1zNF9waTFxY016aDlJcHVZLi5zWnkzTjVaYkJVSkNtZkNCUHdHdUdJdEVhR3lGQ3MuYmR6NS1IeFh3UU9DWThnZ0M2dzpkUERLeGVVN3FDM3FuLlc0ZjExLGNqQ2ROd0g="
