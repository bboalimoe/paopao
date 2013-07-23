paopao
======

跑炮--跑到另一个城市约炮去，是这个节奏么？

重要说明
--------

1. 对 settings.py 的任何变更，需提前以邮件的形式告知项目组全体成员。

     对于数据库链接参数等的配置，请使用 local_settings.py 文件。模板见邮件附件。
2. 请不要把 `local_settings.py` 文件上传至代码库。
3. ubuntu 下 ./run.sh 可以执行运行 django 环境。

目录说明
--------

1. 全局通用的静态文件（js/img/css）存放在 static 目录下，按文件类型存放。
2. 暂定 2 个 APP，分别是 service 和 blog。

    每个 app 的 模板、views 文件、特有的静态文件，放在每个 app 的目录下。
3. 开发服务器（目前主要托管redmine）的最新ip 存于 real-time-ip，
    以 git submodule 的形式存在。
4. url 请统一在根目录下的 urls.py 中定义，后续我们再根据需要做 url 的规划。


开发环境说明
------------

暂时我们使用 github + 本地服务器的方式。

本地服务器的主要问题在于暂时没有静态IP。
后面我们托管到阿里云之后，问题就会得到相应的解决。

目前的临时解决方案是：

当前的代码库中开一个branch `ip_realtime`，
服务器上用一个脚本定期的获取外部ip并push到github上。

任务管理使用redmine，代码使用github，详细的说明，稍后补充。
