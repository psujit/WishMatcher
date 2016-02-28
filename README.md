# WishMatcher

Android Project:
Steps to open and edit the Android Project in Android Studio:-

1) Open Android Studio and create a blank project
2) Go to the source of this blank project (eg. C:\Users\user\AndroidStudioProjects\WISHMATCHER)
3) Replace all the files and folders of this project with the ones of WISHMATCHER project
4) Now open or refresh the blank project in Android Studio
5) Use an emulator or a real device and run the project

Note: Use the latest Android Data Bridge (ADB) installed in your PC in order to run the project on the real device. Make sure to keep USB Debugging turned on in the device and keep it unlocked so that the ADB can run for the first time and accept the data exchange dialogue on the device. Now you can use the same device to run the project without having to run ADB again. But in order to use another device, repeat the steps again.


Web Services:
You will require NLTK to run the web services successfully.
-- NLTK requires Python versions 2.7 or 3.2+
Installing NLTK for Unix/MAC:
1) Install NLTK: run sudo pip install -U nltk
2) Install Numpy (optional): run sudo pip install -U numpy
3) Test installation: run python then type import nltk

Installing NLTK for Windows:
These instructions assume that you do not already have Python installed on your machine.

1) Install Python 3.4: http://www.python.org/downloads/ (avoid the 64-bit versions)
2) Install Numpy (optional): http://sourceforge.net/projects/numpy/files/NumPy/ (the version that specifies pythnon3.4)
3) Install NLTK: http://pypi.python.org/pypi/nltk
4) Test installation: Start>Python34, then type import nltk

Once you have NLTK installed, download the NLTK Data using:

-->import nltk

-->nltk.download()

For running the webservices, we need to ensure that we have the corpus for WordNet in the corpora folder.
Also, you will find the folder stanford-ner-2014-08-27 in the project folder. Copy the folder in nltk_data/taggers.

You will also require to install Pylucene for fetching the records and saving the records. The steps to install PyLucene for UNIX are available here : http://bendemott.blogspot.de/2013/11/installing-pylucene-4-451.html

You will also require Pyspotlight which can be installed using: pip install pyspotlight

Word2Vec can be installed using instructions on: http://textminingonline.com/getting-started-with-word2vec-and-glove

Steps to run the WebService:
Run Webservices.py. This will start the WebServices on your localhost.
To access the WebService use some RESTClient(e.g. Advanced RESTClient is a plugin for Google Chrome), make a POST request to the URL: http://localhost:8080/post and provide a JSON request in the format:
{
  "request" : "your search string"
}
This would return a list of JSON objects of matching records.
Each of these JSON objects have a product header and a url to access the Craigslist page for that product.

In order to integrate it with the Android application, we have to either deploy it on a server or expose the port 8080 using tunneling like NGROK and then update the webservice url in MainActivity.java file in the WISHMATCHER04 project folder to the url of your server.
