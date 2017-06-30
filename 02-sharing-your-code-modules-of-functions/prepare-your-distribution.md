# 发布代码

## 初始化
* 首先为模块创建一个文件夹，文件夹名为模块的命名空间。
* 在文件夹中创建一个 "setup.py" 的文件，并写入代码[传送门](./setup.py)。
* 构建一个发布文件：
    * 在文件夹中使用 `python3 setup.py sdist` 进行初始化文件和打包模块。
    * 使用 `python3 setup.py install` 安装代码。

## 查看
* 使用 `import sys; sys.path` 可以查看代码存放位置。

## 使用
* 导入命名空间 `import nester`, 使用 `nester.print_lol`。
* 使用 `from module import function`，使用这种形式会重新再当前命名空间中导入 `module`。

## 上传代码
* 在文件夹中使用 `python3 setup.py register` 进行账号的登录。
* 使用 `python3 setup.py sdist upload` 进行代码的上传。

