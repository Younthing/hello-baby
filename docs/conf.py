# Sphinx 文档生成器的配置文件。

# 有关内置配置值的完整列表，请参阅文档：
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- 项目信息 -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../"))
# 将上一级目录的绝对路径插入到 sys.path 的起始位置，从而确保Sphinx能够找到项目源文件

# 设置路径后再导入版本，不然有报错麻烦
from hello_baby import __version__

release = __version__

project = "Hello Baby"
copyright = "2024, fanxi"
author = "fanxi"

# -- 常规配置 ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 插件配置
extensions = [
    "sphinx.ext.autodoc",  # 启用自动生成文档的扩展
    # "sphinx.ext.viewcode",  # 添加源代码链接
    # "sphinx.ext.napoleon",  # 支持Google和NumPy风格的docstrings
]

# 设置模板路径，指定在 _templates 目录中查找模板文件
templates_path = ["_templates"]

# 配置不需要包含在生成文档中的文件和目录模式，
# 如 _build（构建目录）、Thumbs.db（Windows系统自动生成的缩略图数据库文件）
# .DS_Store（macOS系统自动生成的目录属性文件）
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML 输出选项 -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# pip install sphinx-rtd-theme
# html_theme = "sphinx_rtd_theme"
html_theme = "sphinx_book_theme"

# 设置静态文件路径，Sphinx将在 _static 目录中查找用户的静态文件（如样式表、图片等）
html_static_path = ["_static"]


# -- 国际化 ----------------------------------------------------------
# 国际化配置部分
# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
# 链接至Sphinx文档中的国际化配置页面

locale_dirs = ["locale/"]  # 指定翻译文件的目录，推荐使用 "locale/" 目录。
gettext_compact = False  # 各个语言的翻译文件将分别存储在不同的子目录中
