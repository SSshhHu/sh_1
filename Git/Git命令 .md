# Git命令

## git常用命令

[Git - git Documentation](https://git-scm.com/docs/git#_git_commands)

## 关于 git clone

- git clone 时，可以所用不同的协议，包括 ssh, git, https 等，其中最常用的是 ssh，因为速度较快，还可以配置公钥免输入密码。各种写法如下：

```
git clone git@github.com:fsliurujie/test.git         --SSH协议
git clone git://github.com/fsliurujie/test.git          --GIT协议
git clone https://github.com/fsliurujie/test.git      --HTTPS协议
```

- 几种效果等价的git clone写法：

```
git clone http://github.com/CosmosHua/locate new
git clone http://github.com/CosmosHua/locate.git new
git clone git://github.com/CosmosHua/locate new
git clone git://github.com/CosmosHua/locate.git new
```

## 关于六个常用命令

![https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg](https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg)

**说明：**

- workspace：工作区
- staging area：暂存区/缓存区
- local repository：或本地仓库
- remote repository：远程仓库

**创建仓库并添加文件：**

- git init - 初始化仓库。
- git add . - 添加文件到暂存区。
- git commit - 将暂存区内容添加到仓库中。

**提交与修改文件：**

- git status 查看仓库当前的状态，显示有变更的文件
- git diff 比较文件的不同，即暂存区核工作区的差异
- git commit 提交暂存区到本地仓库
- git reset 回退版本
- git rm 删除工作区文件
- git mv 移动或重命名工作区文件

**提取日志：**

- git log 查看历史提交记录
- git blame<file> 以列表形式查看指定文件的历史修改记录

**远程操作：**

- git remote 远程仓库操作

    {

    git remote -v; 

    git remote show [url]; 

    git remote add [short_name] [url]（添加远程版本库）; 

    git remote rm name（删除远程仓库）; 

    git remote rename old_name new_name(修改仓库名）

    }

- git fetch 从远程获取代码库
- git pull 下载远程代码并合并
- git push 上传远程代码并合并