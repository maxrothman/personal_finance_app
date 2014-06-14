personal\_finance\_app
====================
_Budget your way_

---

#Setup:
- If you do not already have it, install Python 2.7
  - Visit https://www.python.org/download/releases/2.7
- If you do not already have it, install pip:

   ```bash
$ sudo easy_install pip
```

- If you do not already have it, install virtualenv. This is preferable so that you don't muck up your existing environment.

   ```bash
$ sudo pip install virtualenv
```

- Clone this repo
- Navigate to inside the repo directory, then activate the virtualenv.

   In Mac/Linux:

   ```bash
$ source venv/bin/activate
```

   In Windows:

   ```
$ venv\scripts\activate
```

You're ready to go!

#Testing and Deployment
- To test the app on a local development server, run:

   ```bash
$ dev_appserver.py .
```

- To deploy the app, run:

 ```bash
$ appconfig.py update .
```

#Teardown:
- Deactivate the virtualenv:

   ```bash
$ deactivate
```

#Notes:
- If you add any more packages to the project (via pip), be sure to run this command:

 ```bash
$ linkenv env/lib/python2.7/site-packages lib
```
