https://towardsdatascience.com/7-setups-you-should-include-at-the-beginning-of-a-data-science-project-8232ab10a1ec

https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
Import numexpr as ne
inspecting a Python decorator : check this subject in gmail.
np.random.seed(0)

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

From Ipython.display import display,html ,Math ,Image
display(HTML(“<style>.container { width:91% !important ;}<style>”))

In juypter to run a .py file:
%run abc.py

To load the code of a .py file:
%load abc.py

def times():
	global startTime
startTime = time.time() # Your code here !
def timee():a
	global endtime
endtime = time.time() ; runtime = endtime - starttime
min,sec = divmod(runtime , 60 ) ; hour,min = divmod(min,60)
print(“hour:”, hour , “min:”,min , “sec:”, sec)

—----------------------------------------------------------
# better way to measure runtime of function using decorator:
https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk


Import time
def timer(func_name):
	def inner():
		start = time.time()
		data = func_name()
		end = time.time()
		print(f“runtime is {end-start:.2f} seconds”)
		return data
	return inner
@timer
def myfunc():
	pass
—-----------------------------------------


import psutil
print("="*20, "CPU Info", "="*20)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
from joblib import Memory
    memory = Memory(cachedir='/path/to/cachedir',verbose=1)

    @memory.cache(ignore=[‘debug’])
    def sum2(a, b):
        return a + b
memory.clear(warn=False)

%load_ext memory_profiler
numbers = range(1000000)
%memit map_comprehension(numbers)
peak memory: 166.33 MiB, increment: 102.54 MiB
%memit map_normal(numbers)
peak memory: 71.04 MiB, increment: 0.00 MiB



A Jupyter Notebook in its JSON-based file format can be converted to a pure Python code using the nbconvert application and the python format :
$ jupyter nbconvert --to python Notebook.ipynb
This generates the file Notebook.py, which only contains executable Python code (or if IPython extensions were used in the notebook; a file that is executable with ipython). The noncode content of the notebook is also included in the resulting Python code file in the form of comments that do not prevent the file from being interpreted by the Python interpreter. Converting a notebook to pure Python code is useful, for example, when using the Jupyter Notebooks to develop functions and classes that need to be imported in other Python files or notebooks.










