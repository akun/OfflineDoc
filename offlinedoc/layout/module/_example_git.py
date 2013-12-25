#!/usr/bin/env python
# coding: utf-8
# yc@2013/03/20

'''
项目放在 github 上的项目
'''

import os
import re
from offlinedoc.module._base import GitModule, Version


class Module(GitModule):
  '''
  '''
  # 唯一 id（格式要求同 Linux 文件名）
  name = 'django'
  # 主页，获取 favicon 用（没有的话可以为 None）
  homepage = 'https://www.djangoproject.com/'
  # 以什么做为版本标识，releases 或 tags（默认为 releases）
  version_by = 'tags'
  # 项目地址（可以 git clone 的地址）
  url = 'https://github.com/django/django'
  # 版本类型
  #   normal: 递增，保留所有版本（例如：bootstrap）
  #   latest: 递增，只保留最新版本（例如：jquery）
  #   single: 只抓取一次，无论新旧（例如：sed）
  versioning = 'normal'

  def post_update(self, version, ret=None):
    '''
    需要返回一个包含生成的 HTML 文档的目录地址
    当前已经在 git clone 出来的代码目录中了
    '''
    # cd 到 docs 目录
    self.pushd('docs')
    # 执行 make dirhtml，后台会进行 shpinx 编译
    self.shell('make dirhtml')
    # 返回代码目录
    self.popd()
    # 返回包含 HTML 文档的目录地址
    return os.path.join(os.getcwd(), 'docs/_build/dirhtml/')
