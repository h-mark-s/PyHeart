# PyHeart: a simple heartbeat package for Python 3

**PyHeart** is a simple and lightweight Python 3 Package. With PyHeart you can easily run periodic heartbeat pings to check if your application is still available on the */heartbeat* endpoint.

### Installing PyHeart

Installing PyHeart is very simple you only have to run the following command in your terminal:
```
$ pip3 install pyheart
```
After you successfully installed PyHeart, you just need to import it in your python script:
```
import pyheart
```

### How PyHeart works

As of August 2019, PyHeart has only one function, called **heartbeat()**, which waits for a URL as an argument; heartbeat() then takes that URL, appends the */heartbeat* endpoint to it, and sends a simple GET request.

For example, calling
```
pyheart.heartbeat('http://yourserver.com')
```
will send a GET request to *http://yourserver.com/heartbeat*. If the response code is not 200, PyHeart will warn you that your server is unavailable. PyHeart saves all information in *heartbeat.log*, which is created in your working directory.

### Recommended usage of PyHeart

Naturally, the best way to use PyHeart is to assign your script to a cron job, and/or combine it with other packages. For example, you can set up another cron job script, that parses PyHeart's logs, and notifies you in case of too many failures. 
