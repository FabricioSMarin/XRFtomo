# #########################################################################
# Copyright (c) 2018, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2018. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENTn SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
import numpy as np
from pylab import *
import xfluo
import matplotlib.pyplot as plt
from scipy import ndimage, optimize, signal
import tomopy
import dxchange

class ReconstructionActions(QtWidgets.QWidget):
	dataSig = pyqtSignal(np.ndarray, name='dataSig')
	fnamesChanged = pyqtSignal(list,int, name="fnamesChanged")

	def __init__(self):
		super(ReconstructionActions, self).__init__()

	def reconstruct(self, data, element, box_checked, center, method, beta, delta, iters, thetas):
		'''
		load data for reconstruction and load variables for reconstruction
		make it sure that data doesn't have infinity or nan as one of
		entries
		'''
		recData = data[element, :, :, :]
		recData[recData == inf] = True
		recData[np.isnan(recData)] = True
		recCenter = np.array(center, dtype=float32)

		if box_checked:
			recCenter = None
		print("working fine")

		if method == 0:
			self.recon= tomopy.recon(recData, thetas * np.pi / 180, 
				algorithm='mlem', center=recCenter, num_iter=iters)
		elif method == 1:
			self.recon= tomopy.recon(recData, thetas, 
				algorithm='gridrec', emission=True)
		elif method == 2:
			self.recon= tomopy.recon(recData, thetas * np.pi / 180, 
				algorithm='art', num_iter=iters)
		elif method == 3:
			self.recon= tomopy.recon(recData, thetas * np.pi / 180, 
				algorithm='pml_hybrid', center=recCenter, 
				reg_par=np.array([beta, delta], dtype=np.float32), num_iter=iters)
		elif method == 4:
			self.recon = tomopy.recon(recData, thetas * np.pi / 180,
				algorithm='pml_quad', center=recCenter,
				reg_par=np.array([beta, delta], dtype=np.float32), num_iter=iters)

		self.recon = tomopy.remove_nan(self.recon)
		return self.recon

	def reconMultiply(self):
		'''
		multiply reconstruction by 10
		'''
		self.recon = self.recon * 10
		return self.recon
	def reconDivide(self):
		'''
		divide reconstuction by 10
		'''
		self.recon = self.recon / 10
		return self.recon

	def threshold(self, recon, threshold_value):
		'''
		set threshhold for reconstruction
		'''
		self.recon = recon
		self.recon[np.where(self.recon <= threshold_value)] = 0  # np.min(self.rec)
		return self.rec

	def saveRecTiff(self, recon):

		try:
			global debugging
			savedir = QtGui.QFileDialog.getSaveFileName()

			#MAC OS:
			if sys.platform == "darwin":
				savedir = str(savedir[0])
			#Linux:
			if sys.platform == "linux" or "linux2":
				savedir = str(savedir[0])

			if savedir == "":
				raise IndexError
			print(savedir)
			recon = tomopy.circ_mask(recon, axis=0)
			dxchange.writer.write_tiff(recon, fname=savedir)
		except IndexError:
			print("type the header name")
