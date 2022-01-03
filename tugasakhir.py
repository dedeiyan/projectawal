# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cobahitungan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import cv2 as cv
import numpy as np
from skimage.transform import rescale
from skimage.filters import threshold_otsu

import pickle
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
import os
import pandas as pd
import numpy as np

from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage.transform import rescale


class Ui_Identification(object):
    def setupUi(self, Identification):
        Identification.setObjectName("Identification")
        Identification.resize(823, 493)
        self.centralwidget = QtWidgets.QWidget(Identification)
        self.centralwidget.setObjectName("centralwidget")
        self.PengolahanCitra = QtWidgets.QGroupBox(self.centralwidget)
        self.PengolahanCitra.setGeometry(QtCore.QRect(30, 220, 771, 91))
        self.PengolahanCitra.setObjectName("PengolahanCitra")
        self.open = QtWidgets.QPushButton(self.PengolahanCitra)
        self.open.setGeometry(QtCore.QRect(10, 30, 141, 41))
        self.open.setObjectName("open")
        self.graybutton = QtWidgets.QPushButton(self.PengolahanCitra)
        self.graybutton.setGeometry(QtCore.QRect(160, 30, 141, 41))
        self.graybutton.setObjectName("graybutton")
        self.restbutton = QtWidgets.QPushButton(self.PengolahanCitra)
        self.restbutton.setGeometry(QtCore.QRect(310, 30, 141, 41))
        self.restbutton.setObjectName("restbutton")
        self.nbc = QtWidgets.QPushButton(self.PengolahanCitra)
        self.nbc.setGeometry(QtCore.QRect(460, 30, 141, 41))
        self.nbc.setObjectName("nbc")
        self.reset = QtWidgets.QPushButton(self.PengolahanCitra)
        self.reset.setGeometry(QtCore.QRect(610, 30, 141, 41))
        self.reset.setObjectName("reset")
        self.groupBoxRGB = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxRGB.setGeometry(QtCore.QRect(280, 10, 261, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxRGB.setFont(font)
        self.groupBoxRGB.setObjectName("groupBoxRGB")
        self.grayscale = QtWidgets.QLabel(self.groupBoxRGB)
        self.grayscale.setGeometry(QtCore.QRect(30, 30, 201, 151))
        self.grayscale.setFrameShape(QtWidgets.QFrame.Box)
        self.grayscale.setText("")
        self.grayscale.setObjectName("grayscale")
        self.groupBoxRGB_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxRGB_5.setGeometry(QtCore.QRect(540, 10, 261, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxRGB_5.setFont(font)
        self.groupBoxRGB_5.setObjectName("groupBoxRGB_5")
        self.result = QtWidgets.QLabel(self.groupBoxRGB_5)
        self.result.setGeometry(QtCore.QRect(30, 30, 201, 151))
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setText("")
        self.result.setObjectName("result")
        self.groupBoxRGB_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxRGB_6.setGeometry(QtCore.QRect(20, 10, 261, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxRGB_6.setFont(font)
        self.groupBoxRGB_6.setObjectName("groupBoxRGB_6")
        self.picture = QtWidgets.QLabel(self.groupBoxRGB_6)
        self.picture.setGeometry(QtCore.QRect(30, 30, 201, 151))
        self.picture.setFrameShape(QtWidgets.QFrame.Box)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.groupBoxHasil = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxHasil.setGeometry(QtCore.QRect(40, 330, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxHasil.setFont(font)
        self.groupBoxHasil.setObjectName("groupBoxHasil")
        self.linehasil = QtWidgets.QLineEdit(self.groupBoxHasil)
        self.linehasil.setGeometry(QtCore.QRect(10, 30, 281, 41))
        self.linehasil.setObjectName("linehasil")
        self.label = QtWidgets.QLabel(self.groupBoxHasil)
        self.label.setGeometry(QtCore.QRect(420, 0, 191, 31))
        self.label.setObjectName("label")
        self.linehasil2 = QtWidgets.QLineEdit(self.groupBoxHasil)
        self.linehasil2.setGeometry(QtCore.QRect(420, 30, 281, 41))
        self.linehasil2.setObjectName("linehasil2")
        Identification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Identification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 31))
        self.menubar.setObjectName("menubar")
        Identification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Identification)
        self.statusbar.setObjectName("statusbar")
        Identification.setStatusBar(self.statusbar)

        self.retranslateUi(Identification)
        QtCore.QMetaObject.connectSlotsByName(Identification)

    def retranslateUi(self, Identification):
        _translate = QtCore.QCoreApplication.translate
        Identification.setWindowTitle(_translate("Identification", "MainWindow"))
        self.PengolahanCitra.setTitle(_translate("Identification", "Image Processing"))
        self.open.setText(_translate("Identification", "Open File"))
        self.graybutton.setText(_translate("Identification", "Grayscale"))
        self.restbutton.setText(_translate("Identification", "Result"))
        self.nbc.setText(_translate("Identification", "Classifying"))
        self.reset.setText(_translate("Identification", "Reset"))
        self.groupBoxRGB.setTitle(_translate("Identification", "Grayscale"))
        self.groupBoxRGB_5.setTitle(_translate("Identification", "Result"))
        self.groupBoxRGB_6.setTitle(_translate("Identification", "Picture"))
        self.groupBoxHasil.setTitle(_translate("Identification", "Latin"))
        self.label.setText(_translate("Identification", "Nama Hangeul"))


        self.open.clicked.connect(self.OpenImages)
        self.reset.clicked.connect(self.functionreset)
        self.graybutton.clicked.connect(self.konversigrayscale)
        self.restbutton.clicked.connect(self.konversibiner)
        self.nbc.clicked.connect(self.prosesnbc)
        
    def OpenImages(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
            if fileName:
                pixmap = QtGui.QPixmap(fileName)
                pixmap = pixmap.scaled(self.picture.width(),self.picture.height())
                self.picture.setPixmap(pixmap)
                self.picture.setAlignment(QtCore.Qt.AlignCenter)
                self.file = fileName
  
            self.image = cv.imread(self.file, cv.IMREAD_ANYCOLOR)
            #print(self.image)
            self.processedImage = self.image.copy()
            self.previewImage = ((cv.resize(self.processedImage, (201,151))))
            
    # ini buat nampilin grayscale belum berhasil
    def displaykonversigray(self):
            self.previewgray=self.extract_feature()[0]
            print(self.previewgray)
            qFormat = QtGui.QImage.Format_Indexed8
            if len (self.previewgray.shape) == 3:
                if (self.previewgray.shape[2]) == 4:
                    qFormat = QtGui.QImage.Format_RGBA8888
                else:
                    qFormat = QtGui.QImage.Format_RGB888
            self.img1 = QtGui.QImage(self.previewgray, self.previewgray.shape[1], self.previewgray.shape[0], self.previewgray.strides[0], qFormat)
            self.img1 = self.img1.rgbSwapped()
            self.grayscale.setPixmap(QtGui.QPixmap.fromImage(self.img1))
            self.grayscale.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            
    # ini buat nampilin binary belum berhasil
    def displaykonversibiner(self):
            self.previewHasil=self.extract_feature()[1]
            print(self.previewHasil)
            qFormat = QtGui.QImage.Format_Indexed8
            if len (self.previewHasil.shape) == 3:
                if (self.previewHasil.shape[2]) == 4:
                    qFormat = QtGui.QImage.Format_RGBA8888
                else:
                    qFormat = QtGui.QImage.Format_RGB888
            self.img1 = QtGui.QImage(self.previewHasil, self.previewHasil.shape[1], self.previewHasil.shape[0], self.previewHasil.strides[0], qFormat)
            self.img1 = self.img1.rgbSwapped()
            self.hasil.setPixmap(QtGui.QPixmap.fromImage(self.img1))
            self.hasil.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                 
    #preprocessing
    def extract_feature(self):
            dim=28
            image = imread(self.file, as_gray=True)

            thresh = threshold_otsu(image)
            binary = image <= thresh
        
            rows = np.where(np.any(binary==True, axis=1))
            cols = np.where(np.any(binary==True, axis=0))
            cropped = binary[min(rows[0]):max(rows[0]+1), min(cols[0]):max(cols[0])+1]
        
            if cropped.shape[0] > cropped.shape[1]:
                rescaled = rescale(cropped, dim/cropped.shape[0])
                kurang = dim-rescaled.shape[1]
                zeros_l = np.zeros((dim,int(np.ceil(kurang/2))))
                zeros_r = np.zeros((dim,int(np.floor(kurang/2))))
                new_img = np.hstack((rescaled, zeros_r))
                new_img = np.hstack((zeros_l, new_img))
            else:
                rescaled = rescale(cropped, dim/cropped.shape[1])
                kurang = dim-rescaled.shape[0]
                zeros_l = np.zeros((int(np.ceil(kurang/2)),dim))
                zeros_r = np.zeros((int(np.floor(kurang/2)),dim))
                new_img = np.vstack((rescaled, zeros_r))
                new_img = np.vstack((zeros_l, new_img))
            return image,binary, cropped, rescaled, new_img
    
    
    def prosesnbc(self):
            data=[]
            data.append(self.extract_feature()[4].astype(np.uint8).reshape(28*28))
            model = pickle.load(open('model_training2.sav', 'rb'))
            hasil = model.predict(data)
            print(hasil[0])
            self.linehasil.setText(hasil[0])
            if hasil[0] == 'a':
                self.linehasil2.setText("a")
            if hasil[0] == 'ae':
                self.linehasil2.setText("ae")
            if hasil[0] == 'b':
                self.linehasil2.setText("bieup")
            if hasil[0] == 'bb':
                self.linehasil2.setText("ssang bieup")
            if hasil[0] == 'ch':
                self.linehasil2.setText("chieut")
            if hasil[0] == 'd':
                self.linehasil2.setText("digeut")
            if hasil[0] == 'e':
                self.linehasil2.setText("e")
            if hasil[0] == 'eo':
                self.linehasil2.setText("eo")
            if hasil[0] == 'eu':
                self.linehasil2.setText("eu")
            if hasil[0] == 'eui':
                self.linehasil2.setText("eui")
            if hasil[0] == 'g':
                self.linehasil2.setText("giyeok")
            if hasil[0] == 'gg':
                self.linehasil2.setText("ssang giyeok")
            if hasil[0] == 'h':
                self.linehasil2.setText("hieut")
            if hasil[0] == 'i':
                self.linehasil2.setText("i")
            if hasil[0] == 'j':
                self.linehasil2.setText("jieut")
            if hasil[0] == 'jj':
                self.linehasil2.setText("ssang jieut")
            if hasil[0] == 'k':
                self.linehasil2.setText("kieut")
            if hasil[0] == 'm':
                self.linehasil2.setText("mieum")
            if hasil[0] == 'n':
                self.linehasil2.setText("nieun")
            if hasil[0] == 'ng':
                self.linehasil2.setText("ieung")
            if hasil[0] == 'o':
                self.linehasil2.setText("o")
            if hasil[0] == 'oi':
                self.linehasil2.setText("oi")
            if hasil[0] == 'p':
                self.linehasil2.setText("pieup")
            if hasil[0] == 'r':
                self.linehasil2.setText("rieul")
            if hasil[0] == 's':
                self.linehasil2.setText("shiot")
            if hasil[0] == 'ss':
                self.linehasil2.setText("ssang shiot")
            if hasil[0] == 't':
                self.linehasil2.setText("tieut")
            if hasil[0] == 'tt':
                self.linehasil2.setText("ssang digeut")
            if hasil[0] == 'u':
                self.linehasil2.setText("u")
            if hasil[0] == 'wa':
                self.linehasil2.setText("wa")
            if hasil[0] == 'wae':
                self.linehasil2.setText("wae")
            if hasil[0] == 'we':
                self.linehasil2.setText("we")
            if hasil[0] == 'weo':
                self.linehasil2.setText("weo")
            if hasil[0] == 'wi':
                self.linehasil2.setText("wi")
            if hasil[0] == 'ya':
                self.linehasil2.setText("ya")
            if hasil[0] == 'yae':
                self.linehasil2.setText("yae")
            if hasil[0] == 'ye':
                self.linehasil2.setText("ye")
            if hasil[0] == 'yeo':
                self.linehasil2.setText("yeo")
            if hasil[0] == 'yo':
                self.linehasil2.setText("yo")
            if hasil[0] == 'yu':
                self.linehasil2.setText("yu")
            #self.linehasil2.setText("")
            
 #--- nampilin grayscale dan binary ---#
            
    def konversigrayscale(self):
        self.gray = cv.cvtColor(self.previewImage, cv.COLOR_BGR2GRAY)
        #self.processedImageGray = self.gray.copy()
        #self.previewgray = cv.resize(self.processedImageGray,(201,151))
        self.previewgray= self.gray
        #print ("previewgray")
        #print(len(self.previewgray))
        
        self.displayGrayscale()
        
    def displayGrayscale(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.previewgray.shape) == 3:
            if (self.previewgray.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888
        self.img1 = QtGui.QImage(self.previewgray, self.previewgray.shape[1], self.previewgray.shape[0], self.previewgray.strides[0], qFormat)
        self.img1 = self.img1.rgbSwapped()
        self.grayscale.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.grayscale.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def konversibiner(self):
        ret3,th3 = cv.threshold(self.gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        self.processedImageBlur = th3.copy()
        self.previewbiner = cv.resize(self.processedImageBlur,(128,128))
        self.previewbiner= th3
        self.displaybiner()
       
    def displaybiner(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len (self.previewbiner.shape) == 3:
            if (self.previewbiner.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888
        self.img1 = QtGui.QImage(self.previewbiner, self.previewbiner.shape[1], self.previewbiner.shape[0], self.previewbiner.strides[0], qFormat)
        self.img1 = self.img1.rgbSwapped()
        self.result.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.result.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

            
    def functionreset(self):
        self.picture.clear()
        self.grayscale.clear()
        self.result.clear()
        self.linehasil.setText("")
        self.linehasil2.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Identification = QtWidgets.QMainWindow()
    ui = Ui_Identification()
    ui.setupUi(Identification)
    Identification.show()
    sys.exit(app.exec_())

