# 天府插件合集

1. [获取ip](#获取ip)

2. [TFinfo-评教](#tfinfo-评教)

3. [web-评教](#)

4. [TFinfo-晚签到](#)

5. [最后请点个赞吧](#个人博客)

   

____



## 获取ip

###### 项目介绍
自动登录西南财经大学天府学院校网并且获取ip发到指定邮箱

![](img/pingmu.png "屏保") 
![](img/bat.png "BAT") 
![](img/email_success.png "邮件发送成功") 


感谢[robertzhang10](https://blog.csdn.net/robertzhang10/article/details/2099589?utm_source=blogxgwz3)
提供的bat命令框不关闭的方法
#### 软件架构
软件架构说明
获取data
发送数据到服务器
认证成功
发送ip


#### 安装教程

环境 python 3.6

#### 使用说明
1. 建议将以及需要输入的东西保存为字符串
2. 自己电脑获取ip只需将getip.py丢到电脑启动项（百度）
3. 开机 自动联网 获取ip 指定邮箱 走人
4. 若是提醒别人的请选择bat命令

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

_____



## TFinfo-评教

###### 项目介绍

自动进行tfinfo软件app评教

![](./img/2018-2019-pingjiao01.png)



#### 软件架构

软件架构说明

1. tfpingjiao new一个类 保存初始化信息
2. 使用抓包精灵开始抓包
3. 定义get_detail_course 开始发包
4. 一秒完成（随机3-5打分 修改grade 即可）

#### 安装教程

环境 python 3.6

#### 使用说明

1. 输入自己的学号

2. 选择学期 字符串要对

3. 运行

   

+++++



## TFinfo-晚签到

###### 项目介绍

自动进行tfinfo软件晚签到实现（未实现）

#### 参数

1. 签到原理 登陆tfinfo，点击晚签到，第一步经过设备验证，匹配成功，调到签到界面，匹配失败，不给予通过，签到界面点击签到，签到成功
2. 发包的网址 ：https://qd.tfswufe.edu.cn/itfer-dailySign/rest/student/sign
3. 请求方式 : POST
4. 发包的参数：USERID,KEYID,LATITUDE,LONGITUDE,SIGNPLANID,IP,IDENTIFCATIONUNIQUE,CURRENTDATE,CLIENT(等等)
   1. USERID：学生用户通过md5生成的id（不变）
   2. KEYID:学生学号（不变）
   3. LATITUDE:经度
   4. LONGITUDE：纬度
   5. SIGNPLANID：签到计划 是一段字符串（不变）
   6. IP（不变 学校公网ip）
   7. IDENTIFCATIONUNIQUE：唯一设备号识别 
   8. CURRENTDATE：当前签到的时间
   9. CLIENT：学生用户的第几个设备号（一个学生只能绑定两个设备）
   10.  暂时抓包就是这几个 
5. 加密方式：url传输json字符串的过程中采用的是base64加密
6. 可通过技术解决以下下问题
   1. 设备验证
      1.  手机root ，将自己的设备号改成自己绑定了的设备号（难度低 不建议 没啥用）
   2. 晚签到
      1. 将tfinfo反编译找到关于签到的模块查看 加密的顺序 难度高
7. 获得参数方式1（GET）https://qd.tfswufe.edu.cn/itfer-dailySign/rest/student/sign/itfer-dailySign/rest/student/getTodaySignPlan/12ef88e214804e9aa1ba5560a476c4e9/B02201708
8. ![获取图片](./img/签到1.png)
9. 晚签到（POST）https://qd.tfswufe.edu.cn/itfer-dailySign/rest/student/sign
10. ![](./img/签到2.png)

++++



#### 用java写的后台

![](./img/后台1.png)

++++

#### 加密数据

[]()

#### 总结

要先解决晚签到 首先要知道加密方式，加密方式猜出来后知道是base64加密的，但是采用的是非对称加密，拥有公钥和私钥，也就是为什么前面12个字符基本上都是一样的，然后加密不是加密的字符串，而是加密了json字符串（有引号 括号这些 ）还采用了 防止出现加减 用了等号去代替，一句话来说，不是专业的 破解起来太难了。



### 

### 个人博客
[我的博客](https://abbhay.github.io) 欢迎stat


