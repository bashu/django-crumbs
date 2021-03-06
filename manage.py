# -*- coding: utf-8 -*-

import os, sys

from django.core.management import ManagementUtility

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

MIDDLEWARE_CLASSES = [
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request'
)

PROJECT_APPS = [
    'crumbs',
]

INSTALLED_APPS = [
    'breadcrumbs',

    'django_jenkins',
] + PROJECT_APPS

ROOT_URLCONF = 'test_urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'test_templates'),
]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
)

COVERAGE_EXCLUDES_FOLDERS = ['crumbs/tests/*']
PYLINT_RCFILE = os.path.join(PROJECT_ROOT, 'pylint.rc')

if __name__ == "__main__":
    from django.conf import settings
    settings.configure(
        DATABASES = DATABASES,
        MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES,
        INSTALLED_APPS = INSTALLED_APPS,
        PROJECT_APPS = PROJECT_APPS,
        JENKINS_TASKS = JENKINS_TASKS,
        ROOT_URLCONF = ROOT_URLCONF,
        COVERAGE_EXCLUDES_FOLDERS = COVERAGE_EXCLUDES_FOLDERS,
        PYLINT_RCFILE = PYLINT_RCFILE,
        TEMPLATE_DIRS = TEMPLATE_DIRS,
        TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS,
        TEMPLATE_DEBUG = TEMPLATE_DEBUG,
        )
    utility = ManagementUtility(sys.argv)
    utility.execute()
