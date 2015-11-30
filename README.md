# Travis-ci_Pion-one [![Build Status](https://travis-ci.org/Lee-Kevin/Travis-ci_Wio-Link.svg)](https://travis-ci.org/Lee-Kevin/Travis-ci_Wio-Link)

## Description 
This project shows how to use  Wio Link and Travis CI to indicate the project compiled status through traffic lights by red and green.

Put the traffic lights in a conspicuous place, and let the code monkey like me breakdown. ha-ha


## 操作步骤
* 配置Pion One， 添加3个Grove Relay，每个Relay控制一个信号灯. [开始配置Pion One](https://iot.seeed.cc/getting_started/)  
* 升级Pion One固件，然后拿到三个Relay的Rest API
* 把pion_one_execute.py放置在根目录，并且修改API常量为你的API
```
    red_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    red_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital0/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
    green_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    green_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital2/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
    orange_led_on_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/1?access_token=774bdd528b05a2adf734301bfbdf10b0"
    orange_led_off_api = "https://cn.iot.seeed.cc/v1/node/GroveRelayDigital1/onoff/0?access_token=774bdd528b05a2adf734301bfbdf10b0"
```
* 本地测试：  
    * 编译成功 `$python pion_one_execute.py success`
    * 编译失败 `$python pion_one_execute.py failure`
    * 编译进行中 `$python pion_one_execute.py building`
* 修改.travis-ci, 把上述命令嵌入进去 [开始使用travis-ci](http://docs.travis-ci.com/user/for-beginners/)
```yml
    language: python
    python:
      - "2.7"   
    before_install:   
      - pip install requests   
      - python pion_one_execute.py building   
    install:   
    script:   
      - python helloworld.py      
    after_success:    
      - python pion_one_execute.py success   
    after_failure:   
      - python pion_one_execute.py failure   
```
* 假设helloworld.py是你的项目。修改它故意设置一个错误，然后提交。一起见证奇迹吧！

## 动态效果
![gif](/images/logo.png)
