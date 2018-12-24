# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook(r'teachers.xls')
  # 获取所有sheet
  print workbook.sheet_names() # [u'sheet1']
  sheet_name = workbook.sheet_names()[0]

  # 根据sheet索引或者名称获取sheet内容
  sheet = workbook.sheet_by_index(0) # sheet索引从0开始
  sheet = workbook.sheet_by_name('Sheet2')

  # sheet的名称，行数，列数
  print sheet.name,sheet.nrows,sheet.ncols

  # 获取整行和整列的值（数组）
  rows = sheet.row_values(3) # 获取第四行内容
  cols = sheet.col_values(2) # 获取第三列内容
  print rows
  print cols

  # 获取单元格内容
  # print sheet.cell(1,0).value.encode('utf-8')
  # print sheet.cell_value(1,0).encode('utf-8')
  # print sheet.row(1)[0].value.encode('utf-8')
  
  for row in range(sheet.nrows):
      print sheet.cell(row, 0), sheet.cell(row, 1).value.encode('utf-8'), sheet.cell(row, 2).value

  # 获取单元格内容的数据类型
  print sheet.cell(1,0).ctype

if __name__ == '__main__':
  read_excel()