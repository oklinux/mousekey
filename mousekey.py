#!/usr/bin/env python3on
#coding: utf-8
sshuoming='''
欧侃鼠标导航 0.1
使用方法：
一，安装
在终端下执行python3 ./mousekey.py setup
不安装，可直接执python3 ./mousekey.py
提示：您在安装或者首次运行本脚本会自动安装pip3、Python-xlib和pynput
二，使用
基本延续了Windows的鼠标键和KDE3、4时代的鼠标导航功能，但把/和*两个键设定为鼠标滚轮，给将来支持安卓应用做准备。除了右侧的数字小键盘区，主键盘区的数字键和相关符号键拥有同等作用。按Num Lock键一到两下进入鼠标控制状态，按任意一个非鼠标控制键即退出鼠标控制状态。注：小键盘在数字输入状态才能控制鼠标。
作者信息：
作者：陈欧侃<sjchenkan@qq.com>
语言：基于Python3加pynput模块开发
授权协议；GPL V2
感谢：SUNBING@红旗
     司延腾@Linux人社区
'''

from select import select
import os
import sys
kaiguan=0

anzhuang_sh='''#!nin/bash
mkdir -p /usr/share/ok-mousekey
cp %s /usr/share/ok-mousekey
echo "#!/bin/bash
python3 /usr/share/ok-mousekey/mousekey.py RUN >/dev/null &
">/usr/bin/mousekey
chmod -R 777 /usr/share/ok-mousekey /usr/bin/mousekey
tee<<desktop>/usr/share/autostart/mousekey.desktop
[Desktop Entry]
Name=mousekey
Exec=mousekey
Icon=
Type=Application
desktop
rm -rf $0
''' % sys.argv[0]


def kaiguanjian(cs):
  #鼠标导航开关
  global kaiguan
  global jp
  from pynput.keyboard import Key,Controller
  jp = Controller()
  aj = Key
  if kaiguan != 2:
    if cs in '.alt':
      jp.press(cs.alt)
      kaiguan=2
    if cs in '.ctrl':
      jp.press(cs.ctrl)
      kaiguan=2
    if cs in '.cmd':
      jp.press(cs.cmd)
      kaiguan=2
    if cs in '.shift':
      jp.press(cs.shift_r)
      kaiguan=2
  else:
    kaiguan=0

  if cs in 'Key.num_lock':
    kaiguan=1

  return int(kaiguan)

#为检查依赖做准备。。。
def zhixingJB(JMJB):
  JBWenjian=open('/dev/shm/testemp.py','w')
  JBWenjian.write(JMJB)
  JBWenjian.close()
  zhixingJG=os.system('python3 /dev/shm/testemp.py')
  return zhixingJG

#利用shell把本软件安装到系统中，并设置成随桌面启动。。。e
def anzhuang():
  for cs in sys.argv:
    if cs == 'setup':
      az=open('setup.sh','w')
      az.write(anzhuang_sh)
      az.close()
      os.system('sudo bash ./setup.sh')


#检查pynput依赖，如过未安装，就使用pip安装。
def jianchaYL():
  test='''from pynput.mouse import *
import os,sys
'''
  anzhuang()
  if zhixingJB(test) != 0:
    if not os.path.isfile('/usr/bin/apt'):
        os.system('sudo apt update')
    elif not os.path.isfile('/usr/bin/apt-get'):
        os.system('sudo apt-get update')
    if not os.path.isfile('/usr/bin/pip3'):
      if os.path.isfile('/usr/bin/yum'):
        os.system('sudo yum install python3-pip python3-xlib')
      if os.path.isfile('/usr/bin/apt-get'):
        os.system('sudo apt-get install -y python3-pip python3-xlib')
      if os.path.isfile('/usr/bin/yum'):
        os.system('sudo dmf install python-pip python3-xlib')
    os.system('sudo pip3 install pynput')

#获取键盘按键信息。。。
def on_press(jian):
  try:
    shubiao(format(jian.char))
    print(jian)
  except AttributeError:
    kaiguanjian(format(jian))
    print(jian)
    #shubiao(format(jian))

def anjian(jan):
  if kaiguan == 1:
    return False

def anjian2(jan):
  if kaiguan == 0:
    return False

#持续侦听。。。
def zhenting():
  from pynput.keyboard import Key,Listener,Controller

  while 0==0:
    if kaiguan == 0:
      with Listener(on_press=on_press,on_release=anjian) as listener:
        listener.join()
    if kaiguan == 1:
      with Listener(on_press=on_press,on_release=anjian2,suppress=True) as listener2:
        listener2.join()

#驱动鼠标
def shubiao(jian):
  from pynput.mouse import Controller,Button
  mouse=Controller()
  #设置鼠标键
  global kaiguan
  if kaiguan == 1:
    if jian in '7':
      print(jian)
      mouse.move(-20,-25)
    elif jian in '8':
      mouse.move(0,-20)
    elif jian in '9':
      mouse.move(20,-25)
    elif jian in '4':
      mouse.move(-20,0)
    elif jian in '5':
      mouse.click(Button.left,1)   #左键在单击
    elif jian in '6':
      mouse.move(30,0)
    elif jian in '1':
      mouse.move(-30,35)
    elif jian in '2':
      mouse.move(0,15)
    elif jian in '3':
      mouse.move(30,20)
    elif jian in '-':
      mouse.click(Button.right,1)   #左键双击
    elif jian in '+':
      mouse.click(Button.left,1)   #右键单击
    elif jian in '/':
      mouse.scroll(0,20)  #滚轮向下移动一个单位
    elif jian in '*':
      mouse.scroll(0,-30)  #轮向上移动一个单位
    elif jian in '0' or jian in '.':
      mouse.click(Button.left)   #左键在按住
    else:
      kaiguan=0

#启动
if __name__ == '__main__':
  jianchaYL()
  zhenting()
