# Set up

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations. We cover this in the course!

![image](https://user-images.githubusercontent.com/22293195/117587372-8b093c80-b115-11eb-955d-034096da48e6.png)


![image](https://user-images.githubusercontent.com/22293195/117587379-96f4fe80-b115-11eb-936a-eb5d34495440.png)


Install multirun plugin (Settings > Plugins) then create a multirun runner

![image](https://user-images.githubusercontent.com/22293195/117587435-d91e4000-b115-11eb-8757-3cdba083fe8a.png)

