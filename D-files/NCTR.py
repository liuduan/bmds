import os
import inspect
import sys

import pytest
scriptpath = "../bmds/"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
import bmds


"""
@pytest.fixture
def dataset():
    return bmds.ContinuousDataset(
        doses=[0, 10, 50, 150, 400],
        ns=[111, 142, 143, 93, 42],
        responses=[2.112, 2.095, 1.956, 1.587, 1.254],
        stdevs=[0.235, 0.209, 0.231, 0.263, 0.159])
"""

Model_name = "NCTR"
User_notes = "BMDS NCTR model, ..."
Input_file_name = "NCTR.(D)"
Output_file_name = "NCTR.OUT"
N_obs = 39      # [5] number of observations
N_dose_groups = 4   # [5a] number of dose groups

Max_iter = 500      # [6a] Maximum # of iterations
Rel = 1.00e-8          # [6b] Rel Function Convergence
Para_conv = 1.00e-8     # [6c] Parameter Convergence
Curve = 0       # 7 BMDL Curve Calculation
Restrict = 1    # 8 Restrict Power
Calculation = 1 # 9 BMD Calculation
F_size = 0      # 10 fixed size

Append = 0      # [11] Append or Overwrite Output File
Smooth = 0      # [12] Smooth Option
BMR = 0.100     # [13] BMR (BMR level)
Risk = 0        # [14] Risk Type
Confidence = 0.95   # [15] Confidence Level

Bootstrap = 1000    # [16] Bootstrap Iterations
Seed = 0            # [17] Seed
Alpha = -9999       # [18] Alpha Parameter, [28]
Rho = -9999         # [19] Rho Parameter, [29]
Beta = -9999        # [20] Beta Parameter, [30]

Theta1 = -9999      # [21] Theta1 Parameter, [31]
Theta2 = -9999      # [22] Theta2 Parameter, [32]
Phi1 = -9999        # [23] Phi1 Parameter, [33]
Phi2 = -9999        # [24] Phi2 Parameter, [34]
Phi3 = -9999        # [25] Phi3 Parameter, [35]
Phi4 = -9999        # [26] Phi4 Parameter, [36]
Init = 0            # [27] Initialize Parameters
#
#
#


"""
# [37] Dose Name
# [38] Response Name
# [39] Constant String: NEGATIVE_RESPONSE
# [40] Litter Specific Covariate
# [41] Column 5 name

"""
doses=[0, 25, 50, 100]
sample_size=[111, 142, 143, 93, 42]
responses=[2.112, 2.095, 1.956, 1.587, 1.254]
stdevs=[0.235, 0.209, 0.231, 0.263, 0.159]

f = open('NCTR.(D)', 'w')


f.write(Model_name + '\n')
f.write(User_notes + '\n')
f.write(Input_file_name + '\n')
f.write(Output_file_name + '\n')
f.write(str(N_obs) + " " + str(N_dose_groups) + '\n')
f.write(str(Max_iter) + " " + str(Rel) + " " + str(Para_conv) + " " + str(Curve) + " " + str(Restrict) + " ")
f.write(str(Calculation) + " " + str(F_size) + " " + str(Append) + " " + str(Smooth) + '\n')
f.write(str(BMR) + " " + str(Risk) + " " + str(Confidence) + " " + str(Bootstrap) + " " + str(Seed) + '\n')
f.write(str(Alpha) + " " + str(Rho) + " " + str(Beta) + " " + str(Theta1) + " " + str(Theta2) + '\n')
f.write(str(Phi1) + " " + str(Phi2) + " " + str(Phi3) + " " + str(Phi4) + '\n')
f.write(str(Init) + '\n')
f.write(str(Alpha) + " " + str(Rho) + " " + str(Beta) + " " + str(Theta1) + " " + str(Theta2) + '\n')
f.write(str(Phi1) + " " + str(Phi2) + " " + str(Phi3) + " " + str(Phi4) + '\n')

f.write("Dose Resp Negative_Resp Covariate Dose_Group" + '\n')
f.write(str(doses[0]) + " 1 15 16 -9999" + '\n')
f.write(str(doses[0]) + " 1 8 9 -9999" + '\n')
f.write(str(doses[0]) + " 2 13 15 -9999" + '\n')
f.write(str(doses[0]) + " 3 11 14 -9999" + '\n')
f.write(str(doses[0]) + " 3 10 13 -9999" + '\n')
f.write(str(doses[0]) + " 0 9 9 -9999" + '\n')
f.write(str(doses[0]) + " 2 8 10 -9999" + '\n')
f.write(str(doses[0]) + " 2 12 14 -9999" + '\n')
f.write(str(doses[0]) + " 1 9 10 -9999" + '\n')
f.write(str(doses[0]) + " 2 9 11 -9999" + '\n')

f.write(str(doses[1]) + " 4 10 14 -9999" + '\n')
f.write(str(doses[1]) + " 5 4 9 -9999" + '\n')
f.write(str(doses[1]) + " 6 8 14 -9999" + '\n')
f.write(str(doses[1]) + " 2 7 9 -9999" + '\n')
f.write(str(doses[1]) + " 6 7 13 -9999" + '\n')
f.write(str(doses[1]) + " 3 9 12 -9999" + '\n')
f.write(str(doses[1]) + " 1 9 10 -9999" + '\n')
f.write(str(doses[1]) + " 2 8 10 -9999" + '\n')
f.write(str(doses[1]) + " 4 7 11 -9999" + '\n')
f.write(str(doses[1]) + " 3 11 14 -9999" + '\n')

f.write(str(doses[2]) + " 4 7 11 -9999" + '\n')
f.write(str(doses[2]) + " 5 6 11 -9999" + '\n')
f.write(str(doses[2]) + " 5 9 14 -9999" + '\n')
f.write(str(doses[2]) + " 4 7 11 -9999" + '\n')
f.write(str(doses[2]) + " 5 5 10 -9999" + '\n')
f.write(str(doses[2]) + " 4 7 11 -9999" + '\n')
f.write(str(doses[2]) + " 5 5 10 -9999" + '\n')
f.write(str(doses[2]) + " 6 9 15 -9999" + '\n')
f.write(str(doses[2]) + " 2 5 7 -9999" + '\n')
f.write(str(doses[2]) + " 4 10 14 -9999" + '\n')

f.write(str(doses[3]) + " 6 5 11 -9999" + '\n')
f.write(str(doses[3]) + " 6 8 14 -9999" + '\n')
f.write(str(doses[3]) + " 8 4 12 -9999" + '\n')
f.write(str(doses[3]) + " 7 6 13 -9999" + '\n')
f.write(str(doses[3]) + " 8 4 12 -9999" + '\n')
f.write(str(doses[3]) + " 6 8 14 -9999" + '\n')
f.write(str(doses[3]) + " 6 5 11 -9999" + '\n')
f.write(str(doses[3]) + " 5 3 8 -9999" + '\n')
f.write(str(doses[3]) + " 4 6 10 -9999" + '\n')

f.close()
exit()

def test_executable_path():

    parents = (
        bmds.Dichotomous,
        bmds.DichotomousCancer,
        bmds.Continuous,
    )

    for name, obj in inspect.getmembers(bmds):
        if inspect.isclass(obj):
            if obj not in parents and issubclass(obj, parents):
                exe = obj.get_exe_path()
                print(obj.__name__, exe)
                assert os.path.exists(exe)


@pytest.mark.skipif(sys.platform != "win32",
                    reason='BMDS can only be executed on Windows')
def test_execute(dataset):
    model = bmds.Logistic_213(dataset)
    model.execute()
    assert model.output_created is True
