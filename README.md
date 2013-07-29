paopao
======

跑炮--跑到另一个城市约炮去，是这个节奏么？


开发环境部署指南
----------------

1. 开发环境
    - 系统: Ubuntu 12.04(推荐，可使用VirtualBox以虚拟机形式安装)
    - python 2.7
    - mysql 5.5+
    - git
    - pip
2. 支持的浏览器
    - Chrome
    - Firefox
3. 安装 python 类库

    ``` sudo pip install -r requirement.txt```
4. 配置ssh(连接github时无需输入密码)

    请参考：[https://help.github.com/articles/generating-ssh-keys](https://help.github.com/articles/generating-ssh-keys)

5. 从Github上clone项目

    ``` $git clone git@github.com:JackonYang/paopao.git```

6. 数据库配置
    - 创建 database

        使用"mysql"命令登录mysql，创建数据库，如paopao：

        ```mysql>create database paopao;
           Query OK, 1 row affected (0.00 sec) ```

        注意：数据库使用utf-8编码
    - 复制settings.py配置文件：

        ```$cp settings.py local_settings.py```

        注意：`local_settings.py`不允许放到Github上
    - 编辑`local_settings.py`，配置本地数据库：

        ``` DATABASES = {  
            'default': {  
                'ENGINE': 'django.db.backends.mysql',  # 数据库类型  
                'NAME': 'paopao',                   # 数据库名称  
                'USER': 'root',                      # 数据库用户名  
                'PASSWORD': 'myrootpasswd',        # 数据库密码  
                'HOST': '',                         # 主机名  
                'PORT': '',                         # 端口  
            }  
        } ```
    - 同步数据库

        `$python manage.py syncdb`
8. 运行项目

    `$python manage.py runserver <ip:port>`

    如果不填ip和port，默认为`127.0.0.1:8000`

    如果一切正常，通过浏览器访问 “http://<ip:port>/”就可以打开项目网页。

开发约定
--------

1. 每次 pull 代码以后，请检查 settings.py, requirement.txt, models 是否有更新。对应的操作为：更新 `local_sttings.py`, pip 安装类库, 更新数据库database。
2. 数据库配置信息，请不要写入 settings.py 文件。
3. push 代码时，新增的需手动安装的module，请写入 requirement.txt
