# python runTest.py torch-61345 buggy
# docker exec -it 00c56b837956  /bin/bash /test/torch-61345/torch-61345-buggy.sh
# docker exec -it 00c56b837956  /bin/bash /test/torch-61345/torch-61345-fix.sh
# docker exec -it 00c56b837956  /bin/bash /test/torch-61754/torch-61754-buggy.sh
# docker exec -it 00c56b837956  /bin/bash /test/torch-61754/torch-61754-fix.sh
import sys
sys.path.append('/home/jiangtianjie/gdefects4dll')

sys.path.insert(0,'../data')
import argparse
import os
from pytorch_detail import get_dict
# python runTest.py torch-61345 buggy
# docker exec -it pytorch-10.2-7 /bin/bash /home/torch-61345/torch-61345-buggy.sh
# docker exec -it gdefects4dll-rebug" /bin/bash /test/torch-61345/torch-61345-buggy.sh
#
# torch-61345 pytorch-10.2-7 defects4dll/pytorch:10.2-7 /home/torch-61345/torch-61345-buggy.sh

def run_test(params):
    bugId = params.bugId
    version = params.version
    bug_dict = get_dict(bugId)
    print(bug_dict)
    cmd = "docker exec - it " + bug_dict.get("gdefects4dll-rebug") + " /bin/bash /test/" + bugId + "/" + bugId + "-" + version + ".sh"
    result = os.system(cmd)
    print(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Experiments Script For runTest")
    parser.add_argument("--bugId", type=str, default="torch-61345", help="see bugId")
    parser.add_argument("--version", type=str, default="buggy", choices=["buggy", "fix"])
    params = parser.parse_args()
    run_test(params)
    # print(params)
    # start_time = time.time()
    # run_mutant(params)
    # time_passed_min = (time.time() - start_time) / 60
    # print("time passed (minutes): %g" % time_passed_min)
