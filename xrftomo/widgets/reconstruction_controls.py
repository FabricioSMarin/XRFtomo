# #########################################################################
# Copyright © 2020, UChicago Argonne, LLC. All Rights Reserved.           #
#                                                                         #
#                       Software Name: XRFtomo                            #
#                                                                         #
#                   By: Argonne National Laboratory                       #
#                                                                         #
#                       OPEN SOURCE LICENSE                               #
#                                                                         #
# Redistribution and use in source and binary forms, with or without      #
# modification, are permitted provided that the following conditions      #
# are met:                                                                #
#                                                                         #
# 1. Redistributions of source code must retain the above copyright       #
#    notice, this list of conditions and the following disclaimer.        #
#                                                                         #
# 2. Redistributions in binary form must reproduce the above copyright    #
#    notice, this list of conditions and the following disclaimer in      #
#    the documentation and/or other materials provided with the           #
#    distribution.                                                        #
#                                                                         #
# 3. Neither the name of the copyright holder nor the names of its        #
#    contributors may be used to endorse or promote products derived      #
#    from this software without specific prior written permission.        #
#                                                                         #
#                               DISCLAIMER                                #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR   #
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT    #
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,  #
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT        #
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,   #
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY   #
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT     #
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.    #
###########################################################################


from PyQt5 import QtCore, QtWidgets


class ReconstructionControlsWidget(QtWidgets.QWidget):

    def __init__(self):
        super(ReconstructionControlsWidget, self).__init__()

        self.initUI()

    def initUI(self):
        button1size = 270       #long button (1 column)
        button12size = 200       #2/3 column button
        button2size = 142.5     #mid button (2 column)
        button33size = 98.3
        button3size = 93.3      #small button (almost third)
        button4size = 78.75     #textbox size (less than a third)

        self.combo1 = QtWidgets.QComboBox(self)
        self.combo1.setFixedWidth(button1size)
        self.method = QtWidgets.QComboBox(self)
        self.method.setFixedWidth(button1size)
        self.reconGroup = QtWidgets.QComboBox(self)
        self.reconGroup.setFixedWidth(button2size)
        self.reconGroup.setToolTip("reconstruction group")
        reconGroup_lbl = QtWidgets.QLabel("reconstruction set")
        reconGroup_lbl.setFixedWidth(button2size)


        self.btn = QtWidgets.QPushButton('Reconstruct')
        self.btn.setFixedWidth(button3size)     
        self.btn2 = QtWidgets.QPushButton('recon & save all')
        self.btn2.setFixedWidth(button3size)
        self.recon2npy = QtWidgets.QPushButton('recon all to npy')
        self.recon2npy.setFixedWidth(button3size)
        self.lbl = QtWidgets.QLabel("")
        self.lbl.setFixedWidth(button3size)
        self.equalizeBtn = QtWidgets.QPushButton('equalize')
        self.equalizeBtn.setFixedWidth(button3size)   
        self.rmHotspotBtn = QtWidgets.QPushButton('remove hotspot')
        self.rmHotspotBtn.setFixedWidth(button3size)   
        self.setThreshBtn = QtWidgets.QPushButton('set L-threshold')
        self.setThreshBtn.setFixedWidth(button3size)   

        self.start_lbl = QtWidgets.QLabel("bottom cross-section index")
        self.start_lbl.setFixedWidth(button12size)
        self.start_indx = QtWidgets.QLineEdit("0")
        self.start_indx.setFixedWidth(button4size)
        self.end_lbl = QtWidgets.QLabel("top cross-section index")
        self.end_lbl.setFixedWidth(button12size)
        self.end_indx = QtWidgets.QLineEdit("0")
        self.end_indx.setFixedWidth(button4size)
        self.mid_lbl = QtWidgets.QLabel("middle cross-section index")
        self.mid_lbl.setFixedWidth(button12size)
        self.mid_indx = QtWidgets.QLineEdit("-1")
        self.mid_indx.setFixedWidth(button4size)
        self.mid_indx.setDisabled(True)
        self.recon_stats = QtWidgets.QCheckBox("show reconstructions statistics")
        self.recon_stats.setChecked(False)
        self.recon_save = QtWidgets.QCheckBox("reconstruct & save simultaneously")
        self.recon_save.setChecked(False)


        self.mulBtn = QtWidgets.QPushButton("x 10")
        self.mulBtn.setFixedWidth(button2size)
        self.divBtn = QtWidgets.QPushButton("/ 10")
        self.divBtn.setFixedWidth(button2size)
        self.maxLbl = QtWidgets.QLabel("Max")
        self.maxLbl.setFixedWidth(button2size)
        self.minLbl = QtWidgets.QLabel("Min")
        self.minLbl.setFixedWidth(button2size)
        self.itersName = QtWidgets.QLabel("Iteration")
        self.itersName.setFixedWidth(button2size)
        self.betaName = QtWidgets.QLabel("Beta")
        self.betaName.setFixedWidth(button2size)
        self.deltaName = QtWidgets.QLabel("Delta")
        self.deltaName.setFixedWidth(button2size)
        self.lThreshLbl = QtWidgets.QLabel("Lower Threshold")
        self.lThreshLbl.setFixedWidth(button2size)

        self.iters = QtWidgets.QLineEdit("10")
        self.iters.setFixedWidth(button2size)
        self.beta = QtWidgets.QLineEdit("1")
        self.beta.setFixedWidth(button2size)
        self.delta = QtWidgets.QLineEdit("0.01")
        self.delta.setFixedWidth(button2size)
        self.lThresh = QtWidgets.QLineEdit("0.0")
        self.lThresh.setFixedWidth(button2size)

        self.maxText = QtWidgets.QLineEdit()
        self.maxText.setFixedWidth(button2size)
        self.minText = QtWidgets.QLineEdit()
        self.minText.setFixedWidth(button2size)
       
        reconGroupBox = QtWidgets.QHBoxLayout()
        reconGroupBox.addWidget(reconGroup_lbl)
        reconGroupBox.addWidget(self.reconGroup)


        startBox = QtWidgets.QHBoxLayout()
        startBox.addWidget(self.start_lbl)
        startBox.addWidget(self.start_indx)
        endBox = QtWidgets.QHBoxLayout()
        endBox.addWidget(self.end_lbl)
        endBox.addWidget(self.end_indx)
        midBox = QtWidgets.QHBoxLayout()
        midBox.addWidget(self.mid_lbl)
        midBox.addWidget(self.mid_indx)
        paddingBox = QtWidgets.QHBoxLayout()

        mdBox = QtWidgets.QHBoxLayout()
        mdBox.addWidget(self.mulBtn)
        mdBox.addWidget(self.divBtn)
        maxBox = QtWidgets.QHBoxLayout()
        maxBox.addWidget(self.maxLbl)
        maxBox.addWidget(self.maxText)
        minBox = QtWidgets.QHBoxLayout()
        minBox.addWidget(self.minLbl)
        minBox.addWidget(self.minText)
        itersBox = QtWidgets.QHBoxLayout()
        itersBox.addWidget(self.itersName)
        itersBox.addWidget(self.iters)
        betaBox = QtWidgets.QHBoxLayout()
        betaBox.addWidget(self.betaName)
        betaBox.addWidget(self.beta)
        deltaBox = QtWidgets.QHBoxLayout()
        deltaBox.addWidget(self.deltaName)
        deltaBox.addWidget(self.delta)
        threshBox = QtWidgets.QHBoxLayout()
        threshBox.addWidget(self.lThreshLbl)
        threshBox.addWidget(self.lThresh)
        reconBox = QtWidgets.QHBoxLayout()
        reconBox.addWidget(self.btn)
        reconBox.addWidget(self.btn2)
        reconBox.addWidget(self.recon2npy)

        postReconBox = QtWidgets.QHBoxLayout()
        postReconBox.addWidget(self.equalizeBtn)
        postReconBox.addWidget(self.rmHotspotBtn)
        postReconBox.addWidget(self.setThreshBtn)


        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.combo1)
        vb.addWidget(self.method)
        vb.addLayout(reconGroupBox)
        vb.addLayout(endBox)
        vb.addLayout(startBox)
        vb.addLayout(midBox)
        vb.addLayout(paddingBox)
        vb.addWidget(self.recon_stats)
        vb.addWidget(self.recon_save)
        vb.addWidget(self.lbl)
        vb.addLayout(mdBox)
        vb.addLayout(maxBox)
        vb.addLayout(minBox)
        vb.addLayout(itersBox)
        vb.addLayout(betaBox)
        vb.addLayout(deltaBox)
        vb.addLayout(threshBox)
        vb.addLayout(reconBox)
        vb.addLayout(postReconBox)

        
        self.setLayout(vb)
