#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import sys
from deploy_util import *


class pushtest():


    def __init__(self):
        self.option = ""
        self.push_env = "test"
        self.origin_branch = "test"
        self.dev_lists = ["dev1","dev2","dev3","dev4","dev5","dev6","dev7","dev8","pre"]
        self.option_list = ["-f"]
        self.argv = sys.argv

    def git_pro(self):

        if len (os.popen('git diff').read().strip()) > 0:
            color_print('还有未提交的代码，请处理')
            return False
        else:
            color_print('推送成功了')
            return True
            
        pass

    def process(self):

        lens = len(self.argv)

        if lens < 2:
            raise AttributeError('argv miss')

        if  self.argv[1]   in  self.option_list:
            self.option = self.argv[1]

        elif self.argv[1] in self.dev_lists:
            self.push_env = self.argv[1]
            self.origin_branch = "f_reserved_%s" % self.push_env
        else:
            color_print("Error: 环境错误：请选择 %s" % self.dev_lists)

        if self.git_pro():
            print ('success')

        else:
            print ('fail')



def main():
    pushtest().process();

if __name__ == '__main__':
    main()

#
# option=""
# push_env="test"
# origin_branch="test"
# dev_lists = ["dev1", "dev2", "dev3", "dev4", "dev5", "dev6", "dev7", "dev8","pre"]
# option_lists = ["-f"]
# arg_len=len(sys.argv)
# if arg_len>1:
#     arg_1 = sys.argv[1]
#     if arg_1 in option_lists:
#         option = arg_1
#     else:
#         if arg_1 not in dev_lists:
#             color_print("Error: 环境错误, 请选择dev1 - dev7, 或预发布pre\n")
#             exit()
#         else:
#             push_env = arg_1
#             origin_branch = "f_reserved_%s"%push_env
# if arg_len>2:
#     push_env = sys.argv[2]
#     origin_branch = "f_reserved_%s"%push_env
#     if push_env not in dev_lists:
#         color_print("Error: 环境错误, 请选择dev1 - dev7\n")
#         exit()
#
# if len(os.popen("git diff").read().strip()) > 0:
#     color_print("Error: 当前工作目录有未提交的内容\n")
#     exit()
#
# # master = os.popen("git branch|grep '*'|grep master").read().strip()
# # if len(master)==0 and option !="-f":
# #     color_print("Error:请切换到master分支进行操作\n")
# #     exit()
#
# #if current branch is master
# # if len(master) > 0:
# #     os.system("git fetch 1>/dev/null 2>/dev/null")
# #     diff = os.popen("git diff master origin/master").read().strip()
# #     if len(diff)>0:
# #       color_print("Error: 请检查是否已经push到中心仓储\n")
# #       exit()
#
# #检查是否有冲突
# conflict = os.popen("git diff origin/online HEAD|egrep '\+<<<<|\+>>>>'").read().strip()
# if len(conflict) > 0:
#     color_print("Error: 有未解决的冲突提交到了仓储")
#     exit()
#
# #执行pre-test
# repodir = get_repodir()
# pre_test = repodir + "/deploy/pre-test"
# if os.path.exists(pre_test):
#     cmd = "cd %s/deploy && ./pre-test"%repodir
#     (status,output) = commands.getstatusoutput(cmd)
#     if status != 0:
#         print "Error:pre-test返回了非零值"
#         print output
#         exit(1)
#
# if 'pre' == push_env:
#     os.system("git fetch 1>/dev/null 2>/dev/null")
#     # 当前分支
#     branch_current = os.popen("git branch|grep '*'").read().strip()
#     branch_current = branch_current.replace('* ', '')
#     # 切换到临时分支合并
#     branch_merge_pre = os.popen("git branch|grep merge_pre").read().strip()
#     if len(branch_merge_pre) > 0:
#         os.system("git checkout merge_pre")
#     else:
#         os.system("git checkout -b merge_pre")
#     if option == "-f":
#         # 独占merge_pre
#         os.system("git reset --hard origin/online")
#     else:
#         os.system("git merge origin/%s"%origin_branch)
#     os.system("git merge %s"%branch_current)
#     os.system("git push origin HEAD:%s %s"%(origin_branch, option))
#     # 切换会原分支
#     os.system("git checkout -")
# else:
#     os.system("git fetch 1>/dev/null 2>/dev/null")
# if option != "-f":
#     # diff origin
#     is_used = os.popen(
#         "git log --pretty=format:\"%%h%%x09%%an%%x09%%ad%%x09%%s\" origin/online..origin/%s" % origin_branch).read().strip()
#     if len(is_used) > 0:
#         color_print("Error: 环境已被占用")
#         print(is_used)
#         exit()
# pushcmd = "git push origin HEAD:refs/heads/%s %s" % (origin_branch, option)
# print pushcmd
# os.system(pushcmd)