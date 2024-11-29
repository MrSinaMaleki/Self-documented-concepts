Swagger ---> open source tool that let us test our APIS
https://drf-spectacular.readthedocs.io/en/latest/readme.html

$ pip install drf-spectacular

INSTALLED_APPS = [
    # ALL YOUR APPS
    'drf_spectacular',
]

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

e.g:
"""
     - example request

        {

            "email": "user@example.com",
            "code": "code"

        }

"""
