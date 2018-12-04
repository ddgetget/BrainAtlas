__all__ = ["recv_msg", "send_msg"]  # 表示外界使用from 包名 import * 的时候可以使用那些指定的模块

# 控制包导入模块的行为
# from first_package import recv_msg
# from first_package import send_msg

# .表示当前包
from . import recv_msg
from . import send_msg



# 包管理不同模块，模块管理不同的功能代码