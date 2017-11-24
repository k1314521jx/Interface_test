# Interface_test
1.readConfig.py  获取config.ini里面的配置数据（需要导入第三方库configparser）<br>
2.configDB.py    连接数据库操作（数据库信息填写在config.ini文件里） <br>
3.configHttp.py  进行接口请求<br>
4.common.py      定义了一些公共的方法（如读取Excel，xml文件） <br>
5.config.ini     配置文件 <br>
6.interfaceURL   管理接口地址 <br>
7.caselist       设置需要执行的用例脚本 <br>
8.testLogin.py   定义你的测试用例脚本 <br>
9.run.py         运行自动化 <br>
10.HTMLTestRunner.py   生成测试报告 <br>

整个框架实现数据与业务代码分离，以便于后续代码和数据的维护 <br>
需提前安装的第三方库：configparser（操作ini文件）  requests（封装了很多接口测试的方法，神器） xlrd（读取excle）  xml.ertree（读取XML）<br>
最后测试的参数，统一用Excel管理起来就行
