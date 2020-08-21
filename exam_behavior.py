# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exam_behavior.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import cv2
import threading
import exam_behavior_model
import os
import time
import numpy as np


class Ui_Dialog_exam_behavior(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 1051, 741))
        self.label_2.setStyleSheet("QLabel{\n"
"background:white;;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 790, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 80, 111, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(690, 80, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 80, 181, 41))
        self.label_4.setObjectName("label_4")
        self.label_photo = QtWidgets.QLabel(Dialog)
        self.label_photo.setGeometry(QtCore.QRect(40, 180, 821, 501))
        self.label_photo.setStyleSheet("QLabel{\n"
"    background:blue;\n"
"}")
        self.label_photo.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 80, 111, 41))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(510, 80, 101, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(750, 80, 111, 41))
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(890, 270, 171, 231))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    background:white;\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(870, 550, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 550, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_photo.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)

        self.pushButton.clicked.connect(self.previous)
        self.pushButton_3.clicked.connect(self.next)

        global nownum,picnum,count
        count = 1
        picnum = 0
        nownum = 0




        threads = []
        t1 = threading.Thread(target=self.showcamera)
        threads.append(t1)
        t2 = threading.Thread(target=self.counttime)
        threads.append(t2)
        for t in threads:
            t.setDaemon(False)
            t.start()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">教室号：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">班级：</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">正在考试的科目是：</span></p></body></html>"))
        self.label_photo.setText(_translate("Dialog", "我是图片"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">钟海楼03021</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">离散数学</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">软件工程1164</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "previous"))
        self.pushButton_3.setText(_translate("Dialog", "next"))


    def showcamera(self):
        global count
        vc = cv2.VideoCapture('G:/test/tiaozhanbeidataset/video/exam_1.mp4')
        while(1):
                # get a frame
                ret, img = vc.read()
                img2 = np.array(img)
                imgmake,pointlist = exam_behavior_model.addlabel(img) # 加上标签
                if((pointlist)and(count==1)):
                    self.takepic(img2,pointlist)
                    count = 0
                height, width, bytesPerComponent = imgmake.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                cv2.cvtColor(imgmake, cv2.COLOR_BGR2RGB, imgmake)
                # 转为QImage对象
                self.image = QImage(imgmake.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.label_photo.setPixmap(QPixmap.fromImage(self.image).scaled(self.label_photo.width(), self.label_photo.height()))
                #cv2.waitKey(10)


    def counttime(self):
        global count
        while(1):
            if(count==0):
                time.sleep(40)
                count=1

    def takepic(self,img2,pointlist):
        global picnum,nownum
        for point in pointlist:
            strpicnum = str(picnum)
            imgsave = img2[point[1]:point[3],point[0]:point[2]]
            imgsave = cv2.resize(imgsave,(171,231))
            #cv2.cvtColor(imgsave, cv2.COLOR_BGR2RGB, imgsave)
            cv2.imwrite("G:/test/tiaozhanbeitest/exampic/example"+strpicnum+".jpg", imgsave)
            pix2 = QPixmap("G:/test/tiaozhanbeitest/exampic/example" + strpicnum + ".jpg")
            self.label_5.setPixmap(pix2)
            nownum = picnum
            picnum += 1
            print("截图成功")


    def previous(self):
        global nownum
        if(nownum!=0):
            nownum = nownum - 1
            pix2 = QPixmap("G:/test/tiaozhanbeitest/exampic/example" + str(nownum) + ".jpg")
            self.label_5.setPixmap(pix2)

    def next(self):
        global picnum,nownum
        if(nownum!=picnum-1):
            nownum = nownum + 1
            pix2 = QPixmap("G:/test/tiaozhanbeitest/exampic/example" + str(nownum) + ".jpg")
            self.label_5.setPixmap(pix2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_exam_behavior()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())