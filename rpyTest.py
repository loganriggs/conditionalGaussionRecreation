#
# Must import R_HOME path. Change to correct path.
#
import os
os.environ['R_HOME'] = '/home/loganriggs/anaconda3/lib/R' #path to your R installation
# os.environ['R_USER'] = 'C:\ProgramData\Anaconda3\Lib\site-packages\rpy2' #path depends on where you installed Python. Mine is the Anaconda distribution

from rpy2.robjects.packages import importr
#
#Utils import solution that didn't work for me.
#
utils = importr('utils')
utils.install_packages("mvtnorm", repos="http://cran.uk.r-project.org/")
from rpy2.robjects import numpy2ri
numpy2ri.activate()
mvt = importr('mvtnorm')
#
# We use the above to use function mvt.qmvnorm()
#