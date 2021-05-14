# JG-Modules-Packages-Demo
python modules packages challenge

Step1 (can be done only one time): Create your virtual environment
To create a virtual environment, decide upon a directory where you want to place it, 
and run the venv module as a script with the directory path:
>> python3 -m venv tutorial-env
OR
>> python -m venv tutorial-env


Step2 (done when opening your app): Activate your virtual environment
Once you’ve created a virtual environment, you may activate it.
* On Windows, run:
>> tutorial-env\Scripts\activate.bat
>> .\tutorial-env\Scripts\activate OR tutorial-env\Scripts\activate
* On Unix or MacOS, run:
>>source tutorial-env/bin/activate

in our example: my-venv\Scripts\activate

Step3: Install the required package:
>> pip install colorama

# Now You are ready to start coding!
# Yes, you can leave step4 till the end
Step4: Creating the "requirements.txt"
>> pip freeze > requirements.txt
