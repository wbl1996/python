# python
将要下载的图片的url保存在redis数据库中
还有一些问题要解决：
1. 首先，不是将数据存在redis中，而是用redis做缓存，增加存放的速度
2. 其次，没有轮换ip，容易被网站禁用ip
3. 数据存放只是一个快照，无法将数据存放到本地

-----------------
## 关于启动redis
*经常会出现无法启动的错误，还没有弄明白，但是有解决方案，如下*
1. redis-cli.exe
2. shutdown
3. exit
4. redis-server redis.windows.conf         //可以使用默认配置文件的，不加redis.windows.conf，这里我加上了启动的密码
