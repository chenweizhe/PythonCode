#! /usr/bin/env python3
# 模块 在Python中，一个.py文件就称之为一个模块（Module）。

# 你也许还想到，如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，
# Python又引入了按目录来组织模块的方法，称为包（Package）。

# 现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：

# mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# 类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

# mycompany
#  ├─ web
#  │  ├─ __init__.py
#  │  ├─ utils.py
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py
#  └─ xyz.py
# 文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。

#  自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，
# 自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

# 总结
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

# 创建自己的模块时，要注意：

# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
