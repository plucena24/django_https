Super basic example on how to encrypt all traffic over SSL using django and django-sslify.

To use:

.. code-block:: console

   $ sudo /bin/bash
   $ git clone https://github.com/NAThompson/django_https.git    
   $ pyvenv django_https
   $ cd django_https
   $ source bin/activate
   $ pip install -r requirements.txt
   $ cd src
   $ ./manage.py checksecure # Validate that basic security steps have been taken
   $ ./manage.py runsslserver --addrport 127.0.0.1:443

Visit at ``https://127.0.0.1``; your browser won't trust your certificate.
    
