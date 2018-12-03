# RxStore

RxStore is a distributed information system for patient prescription management that is location agnostic. RxStore currently only handles prescription management, but is capable of handling patient medical information provided enough resources and security.

## Actionables
* Insert a footer into base.html that uses Bootstrap 3
* Figure out why "- [ ]" did not work
* Update database models for patient to remove primary_physician and migrate

## Why RxStore?
RxStore follows the [Chord](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1180543) protocol to the best of our abilities to ensure that information can be found efficiently and it is capable of handling node joins and departures (failures).

## User Capabilities
RxStore allows for prescription management across patients, doctors, and pharmacists. Patients have full read access to their prescription data but are unable to change any of their prescription information. Doctors have read access to their patients' data but cannot change patient information except for adding new prescriptions. Pharmacists only have read access to patient information and limited write access to prescriptions filled at the pharmacist's respective pharmacy. Pharmacists only have write access when it pertains to updating when and how prescriptions have been filled.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
```
git clone https://github.com/DarianNwankwo/RxStore
cd RxStore
```

### Prerequisites

We **RECOMMEND** using a virtual environment to manage your instance of RxStore. Issue the command below to setup your local environment. If you do not wish to do so, skip this step.

```
python3 -m venv <virtual_environment_name>
source <virtual_environment_name>/bin/activate
```

When you are done working in your environment, be sure to deactivate your virtual environment.

```
deactivate
```

RxStore's backend was developed using Python 3.6.5 and the Flask microframework. In order to run the system locally, install all of the packages in **requirements.txt** using the following command.

```
pip install -r requirements.txt
```

### Installing

Once the prerequisites have been installed, it is now time to setup your development environment. In order to run the app, issue the **flask run** command from the command line. This command, however, relies on an environment variable named **FLASK_RUN**. This environment variable needs to be set prior to issuing the **flask run** command.

##### (OPTIONAL STEP BELOW)
This can be rather bothersome, so to mitigate this problem, I have installed the packpage **python-dotenv**. More information about that package can be found [here](https://pypi.org/project/python-dotenv/). This package allows us to create a file **.flaskenv** and each time we run **flask run** it uses this file to set the appropriate environment variables.
##### (OPTIONAL STEP ABOVE)


```
export FLASK_APP=rxstore.py
flask run
```

(NOTE) Development was done on macOS Mojave version 10.14. For other operating systems, it is expected that you understand how to set your environment variables appropriately.

## Developing
RxStore stores information locally using SQLite, which has its own limitations, but is enough for proof-of-concept. If you decide to change the models to fit your preferences, be sure to track those changes to the database and maintain an updated migration directory. More information on doing so can be found [here](https://flask-migrate.readthedocs.io/en/latest/).


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Darian Nwankwo** - *Initial work* - [DarianNwankwo](https://github.com/DarianNwankwo)
* **Chinasa Okolo** - *Initial work* - [ChiNasa511](https://github.com/ChiNasa511)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
