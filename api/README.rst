Contractt
=========

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Tests
^^^^^^^^^^^^^
::

    $ docker-compose run --rm contractt make tests

Para checar a cobertura de testes basta executar:
::

    $ docker-compose run --rm contractt make tests-coverage

Shell
^^^^^^^^^^^^^

Para entrar no `shell do Django <https://docs.djangoproject.com/en/2.2/ref/django-admin/#shell>`_ e executar operações com os modelos ou outras funções:
::

    $ docker-compose run --rm contractt make shell

Obs: Esse projeto utiliza o `shell_plus` da biblioteca `django-extensions <https://django-extensions.readthedocs.io/en/latest/>`_ que provê algumas funcionalidades extras.


Code Style
^^^^^^^^^^^^^

Esse projeto segue a PEP8, para analisar o código é possível utilizar o `flake8 <http://flake8.pycqa.org/en/latest/>`_ com:
::

    $ make lint

Rodar o `black <https://black.readthedocs.io/en/stable/>`_ para ajustar o estilo de código que segue os arquivos de configuração `pyproject.toml <pyproject.toml>`_ e `.flake8 <.flake8>`_:
::

    $ black .
