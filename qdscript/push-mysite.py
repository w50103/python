#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import sys
import subprocess

from datetime import date, datetime
from deploy_util import *

from deploy_util import get_repodir


class pushtest():


    def __init__(self):
        self.option = ""
        self.push_env = "test"
        self.origin_branch = "test"
        self.dev_lists = ["dev1","dev2","dev3","dev4","dev5","dev6","dev7","dev8","pre"]
        self.option_list = ["-f"]
        self.argv = sys.argv

    def git_pro(self):

        try:
            # 验证是否有未提交内容
            if len(os.popen('git diff').read().strip()) > 0:
                mes = 'Error: 还有未提交的代码，请处理'
                return False, mes

            # 验证是否有冲突

            if len(os.popen('git diff origin/master HEAD |egrep "\+<<<<|\+>>>>"').read().strip()) > 0:
                mes = 'Error: 有未解决的冲突提交到了仓储'
                return False, mes

            # 执行git pre-test

            repdir = get_repodir()
            if os.path.exists(repdir + '/deploy/pre-test'):
                cmd = "cd %s/deploy && ./pre-test" % repdir

                (status, mes) = subprocess.getstatusoutput(cmd)

                if status != 0:
                    return False, 'Error: pre-test 返回非0值异常, mes: %s' % mes

            # 拉去最新代码
            subprocess.getstatusoutput('git fetch 1 >/dev/null 2>/dev/null')

            if 'pre' == self.push_env:
                self.branch_current = os.popen('git branch| grep "*"').read().strip().replace('*', '')
                if (len(os.popen('git branch| grep merge_pre').read().strip()) < 0):
                    subprocess.getstatusoutput('git checkout -b merge_pre')
                else:
                    subprocess.getstatusoutput('git checkout merge_pre')

                if self.option.upper() == '-F':
                    subprocess.getstatusoutput('git reset --hard origin/online')
                else:
                    subprocess.getstatusoutput('git merge origin/%s' % self.origin_branch)

                subprocess.getstatusoutput('git merge %s' % self.branch_current)
                subprocess.getstatusoutput('git push origin HEAD:%s %s' % (self.origin_branch, self.option))
                subprocess.getstatusoutput('git checkout -')

            if '-F' != self.option.upper():
                if (len(os.popen('git log --pretty=format:\"%%h%%x09%%an%%x09%%ad%%x09%%s\" origin/master..origin/%s' % self.origin_branch).read().strip()) > 0):
                    return False, 'Error: 环境被占用 \n '
            print('params %s|%s|%s|%s' % (self.origin_branch, self.option, 'abc', repdir))

            pushcmd = 'git push origin HEAD:refs/heads/%s %s' % (self.origin_branch, self.option)

            print(pushcmd)

            [status, mes] = subprocess.getstatusoutput(pushcmd)

            return status, mes



        except BaseException as e:
            raise

        finally:
            print(datetime.now())



        #force up






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

        [res, mes] = self.git_pro()

        if not res:
            color_print(mes)

        else:
            print ('success')




def main():
    pushtest().process()

if __name__ == '__main__':
    main()
