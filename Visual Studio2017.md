ctrl+-（shift+ctrl+-）：移动光标到上次位置或相反，比如定位一个函数，转到函数定义后想回到函数使用处，则用ctrl+-，若又想回到函数定义处则可以按shift+ctrl+-
F12：Go to Definition，到变量或函数定义的地方，如变量声明处，函数实现处。与ctrl+-配合使用非常方便

Ctrl+]：匹配选中的括号（大括号、小括号都行），在多层循环+判断语句时非常方便

ctrl+Space：代码补全

ctrl+tab：在VS中切换打开的窗口，即切换各个文件

ctrl+I：递增搜索，与ctrl+F不同的是搜索期间不显示搜索对话框，且ctrl+F搜索下一个直接按Enter即可，而ctrl+I搜索下一个按ctrl+I或F3，Escape退出，连续按两次ctrl+I重复上次搜索
Ctrl+Shift+F：旧式的文件搜索对话框（与记事本中的搜索替换框差不多，可以替换）
Ctrl+F3：为当前选中的部分进行搜索（不需要再输入要搜索的内容）

Shift+Alt+Enter：最大化代码编写区域（代码全屏模式），即去掉所有其它辅助窗口只留下代码编写窗口，再按一次返回到原来界面

ctrl+K，Ctrl+C：注释一段代码块（先要选中一段代码）
ctrl+K，Ctrl+U：取消注释一段代码块
ctrl+K，Ctrl+D：代码自动格式化（整个文档）
ctrl+K，Ctrl+F：只格式化你选中的部分


Ctrl+K，Ctrl+K：在当前行创建一个书签
Ctrl+K, Ctrl+N：去下一个书签处
 

Ctrl+C, Ctrl+V：在当前行的下一行复制当前行内容（不用选中当前行），即复制当前行并粘贴到下一行，在两行内容差不多时很有用，可以先复制再改
Ctrl+L：删除当前行

Ctrl+M, Ctrl+M：展开或关闭当前的代码


## 项目相关的快捷键



Ctrl + Shift + B = 生成项目

Ctrl + Alt + L = 显示Solution Explorer（解决方案资源管理器）

Shift + Alt+ C = 添加新类

Shift + Alt + A = 添加新项目到项目

## 编辑相关的键盘快捷键

Ctrl + Enter = 在当前行插入空行

Ctrl + Shift + Enter = 在当前行下方插入空行

Ctrl +空格键 = 使用IntelliSense（智能感知）自动完成

Alt + Shift +箭头键(←,↑,↓,→) = 选择代码的自定义部分

Ctrl + } = 匹配大括号、括号

Ctrl + Shift +} = 在匹配的括号、括号内选择文本

Ctrl + Shift + S = 保存所有文件和项目

Ctrl + K，Ctrl + C = 注释选定行

Ctrl + K，Ctrl + U = 取消选定行的注释

Ctrl + K，Ctrl + D = 正确对齐所有代码

Shift + End = 从头到尾选择整行

Shift + Home = 从尾到头选择整行

Ctrl + Delete = 删除光标右侧的所有字



## 导航相关的键盘快捷键

Ctrl +Up/Down = 滚动窗口但不移动光标

Ctrl + - = 让光标移动到它先前的位置

Ctrl ++ = 让光标移动到下一个位置

F12 = 转到定义



## 调试相关的键盘快捷键

Ctrl + Alt + P = 附加到进程

F10 = 调试单步执行

F5 = 开始调试

Shift + F5 = 停止调试

Ctrl + Alt + Q = 添加快捷匹配

F9 = 设置或删除断点



## 搜索相关的键盘快捷键
Ctrl + K Ctrl + K = 将当前行添加书签

Ctrl + K Ctrl + N = 导航至下一个书签

Ctrl + . = 如果你键入一个类名如Collection<string>，且命名空间导入不正确的话，那么这个快捷方式组合将自动插入导入

Ctrl + Shift + F = 在文件中查找

Shift + F12 = 查找所有引用

Ctrl + F = 显示查找对话框

Ctrl + H = 显示替换对话框

Ctrl + G = 跳转到行号或行

Ctrl + Shift + F = 查找所选条目在整个解决方案中的引用

```C#
DataTable dt = bll.Query(strSQL);
count = dt.Rows.Count;
return dt;
```