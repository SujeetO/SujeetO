pip show <module_name>
pip list -v
####################
pip install jupyter_contrib_nbextensions

jupyter contrib nbextension install --user
 : in my case jupyter was set to some alias hence it was not working. after unalias jupyter , worked fine

jupyter trust .*ipynb

pip freeze > requirements.txt
activate
pip install -r requirements.txt

pip install -U modin
pip uninstall modin

pip list: to get version of all installed modules.
pip show numpy : to get verbose info for numpy module
https://python.plainenglish.io/how-to-generate-requirements-txt-for-your-python-project-235183799d2f
 
https://towardsdatascience.com/useful-pip-commands-in-data-science-6632c7fd2d0a

to create a new venv:
python3 -m venv ./junk/myenv

suppose you want to create a new venv for 3.11:
/home/abc/def/python-.11/bin/python -m venv ./my_python_311_venv
after this acticvate this and install the packages.

-------------------
# create a conda environment
conda create --name yourenvname python=3.8

# activate conda environment
conda activate yourenvname

# install pycaret
pip install pycaret
-------------------------------------------
##################################
