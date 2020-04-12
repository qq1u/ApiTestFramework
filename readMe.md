# 使用前须知

    此框架用到两个第三方库
        1、requuests 库
        2、parameterized 库
    
    快速体验：
        pip install -r requirements.txt
        python manage.py

## <1>、api层
    放置接口的请求对象层

## <2>、case层
    放置测试用例，需要以test_开头.py的文件，并且当中的测试类要继承自 case.base里的Base类。

## <3>、data层
    放置测试数据,类似[{"config": {"url": "xxx", "header": {}}}, {}, {}]
    case中需要使用一些依赖参数的情况，可以用${userId}的方式调用， 前提是需要在setup_function里编写相应方法，可参考当中 login 的实现。
    config.json, 放置主机相关配置
    可参考现存在的login.json文件。

## <4>、log层
    测试过程中产生的测试日志
 
## <5>、report层
    测试结束后产生的html的测试报告
 
## <6> tools层
    测试框架内部使用的工具
    注意 setup_teardown.py, 可以定义一些case里的 setup、teardown 方法，并在function里写好对应的调用关系，然后在data里需要调用的时候，指定对应的映射名字。

## <7> manage.py
    python manage.py 会运行case下所有的测试用例。
