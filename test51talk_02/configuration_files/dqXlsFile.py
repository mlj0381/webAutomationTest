#!usr/bin/python
#encoding:utf-8

import xlrd
import xlwt
import os

import time
def dqXlsLoginSuccess():

    gendir = os.path.dirname(os.getcwd())

    # xlsxGenDir = gendir + "\\FileDir\userInfoLoginSuccess.xlsx"

    #mac
    xlsxGenDir = gendir + "/FileDir/userInfoLoginSuccess.xlsx"

    xlsxgendir = xlrd.open_workbook(xlsxGenDir)
    xlsx_table = xlsxgendir.sheets()[0]

    # 获取行数
    r_sum = xlsx_table.nrows

    # 获取列数
    l_sum = xlsx_table.ncols

    l1 = []
    # 获取整行数据并读取每行数据
    for i in range(0, r_sum):
        m_r = xlsx_table.row_values(i)
        l1.append(m_r)
    return l1

def dqXlsLoginFail():

    gendir = os.path.dirname(os.getcwd())

    # xlsxGenDir = gendir + "\\FileDir\userInfoLoginFail.xlsx"

    #mac
    xlsxGenDir = gendir + "/FileDir/userInfoLoginFail.xlsx"

    xlsxgendir = xlrd.open_workbook(xlsxGenDir)
    xlsx_table = xlsxgendir.sheets()[0]

    # 获取行数
    r_sum = xlsx_table.nrows

    # 获取列数
    l_sum = xlsx_table.ncols

    l1 = []
    # 获取整行数据并读取每行数据
    for i in range(0, r_sum):
        m_r = xlsx_table.row_values(i)
        l1.append(m_r)
    return l1

def dqXlsResigetSuccess():

    gendir = os.path.dirname(os.getcwd())

    # xlsxGenDir = gendir + "\\FileDir\userInfoResigetSuccess.xlsx"

    #mac
    xlsxGenDir = gendir + "/FileDir/userInfoResigetSuccess.xlsx"

    xlsxgendir = xlrd.open_workbook(xlsxGenDir)
    xlsx_table = xlsxgendir.sheets()[0]

    # 获取行数
    r_sum = xlsx_table.nrows

    # 获取列数
    l_sum = xlsx_table.ncols

    l1 = []
    # 获取整行数据并读取每行数据
    for i in range(0, r_sum):
        m_r = xlsx_table.row_values(i)
        l1.append(m_r)
    return l1

def dqXlsResigetFail():

    gendir = os.path.dirname(os.getcwd())

    # xlsxGenDir = gendir + "\\FileDir\userInfoResigetFail.xlsx"

    #mac
    xlsxGenDir = gendir + "/FileDir/userInfoResigetFail.xlsx"

    xlsxgendir = xlrd.open_workbook(xlsxGenDir)
    xlsx_table = xlsxgendir.sheets()[0]

    # 获取行数
    r_sum = xlsx_table.nrows

    # 获取列数
    l_sum = xlsx_table.ncols

    l1 = []
    # 获取整行数据并读取每行数据
    for i in range(0, r_sum):
        m_r = xlsx_table.row_values(i)
        l1.append(m_r)
    return l1