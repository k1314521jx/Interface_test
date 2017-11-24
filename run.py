import os
import unittest
import HTMLTestRunner


caseList = []
#提取需要执行的用例脚本
def set_case_list():
    """
    set case list
    :return:
    """

    caseListFile = os.path.dirname(__file__) + r'\caselist.txt'
    fb = open(caseListFile)
    for value in fb.readlines():
        data = str(value)
        if data != '' and not data.startswith("#"):
            caseList.append(data.replace("\n", ""))
    fb.close()


#添加测试套件
def set_case_suite():
    """
    set case suite
    :return:
    """
    set_case_list()
    print(caseList)
    #创建测试套件
    test_suite = unittest.TestSuite()
    suite_module = []
    caseFile = os.path.dirname(__file__)
    print(caseFile)
    for case in caseList:
        case_name = case.split("/")[-1]
        print(case_name+".py")
        #依次加载测试用例
        discover = unittest.defaultTestLoader.discover(caseFile, pattern=case_name + '.py', top_level_dir=None)
        suite_module.append(discover)
        # runner = unittest.TextTestRunner()
        # runner.run(discover)
        

    if len(suite_module) > 0:

        for suite in suite_module:
            for test_name in suite:
                #把要执行的用例脚本添加到测试套件里
                test_suite.addTest(test_name)
                print('test_name',test_suite)
                
    return test_suite
def run():
    """
    run test
    :return:
    """
    Path = os.path.dirname(__file__)
    resultPath = Path + r'\report.html'
    suit = set_case_suite()
    print(suit)
    if suit is not None:
        fp = open(resultPath, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
        runner.run(suit)

run()

