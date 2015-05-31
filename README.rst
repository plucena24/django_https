Super basic example on how to encrypt all traffic over SSL using django and django-sslify.

To use:

.. code-block:: console

   $ sudo /bin/bash
   $ git clone https://github.com/NAThompson/django_https.git    
   $ pyvenv django_https
   $ cd django_https    
   $ pip install -r requirements.txt
   $ cd src
   $ ./manage.py runsslserver 127.0.0.1:443
    
