#!/usr/bin/python
__doc__ = 'CRUST.PY -- affix low-density SLy crust from Read+ 2009 to core EoS'
__usage__ = 'crust(eos,pts=1e3)'
__author__ = 'philippe.landry@ligo.org'
__date__ = '08-2018'

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

rhonuc = 2.7e14

def crust(eos,pts=1e3):

	# LOAD EOS DATA

	eosdatx = eos[:,0]/rhonuc # rho in units of rhonuc
	eosdaty = eos[:,1]/rhonuc # p in units of rhonuc
	eosintp = interp1d(eosdatx,eosdaty,kind='linear',bounds_error=False,fill_value=0.)
	
	def p(rho):
	
		return eosintp(rho)
		
	eosdaty2 = eos[:,2]/rhonuc # mu in units of rhonuc
	eosintp2 = interp1d(eosdatx,eosdaty2,kind='linear',bounds_error=False,fill_value=0.)
	
	def mu(rho):
	
		return eosintp2(rho)
		
	# BUILD SLY CRUST
	
	K = [0,6.80110e-9,1.06186e-6,5.32697e1,3.99874e-8]
	Gamma = [1,1.58425,1.28733,0.62223,1.35692]
	rhodiv = [0,2.44034e7,3.78358e11,2.62780e12,1e20]
	a = np.zeros(5)
	a[1] = 0
	a[2] = (rhodiv[1]+K[1]*rhodiv[1]**Gamma[1]/(Gamma[1]-1.)+a[1]*rhodiv[1])/rhodiv[1]-1.-K[1]*rhodiv[1]**(Gamma[1]-1.)/(Gamma[1]-1)
	a[3] = (rhodiv[2]+K[2]*rhodiv[2]**Gamma[2]/(Gamma[2]-1.)+a[2]*rhodiv[2])/rhodiv[2]-1.-K[2]*rhodiv[2]**(Gamma[2]-1.)/(Gamma[2]-1)
	a[4] = (rhodiv[3]+K[3]*rhodiv[3]**Gamma[3]/(Gamma[3]-1.)+a[3]*rhodiv[3])/rhodiv[3]-1.-K[3]*rhodiv[3]**(Gamma[3]-1.)/(Gamma[3]-1)

	def pSLy(rho):
	
		if isinstance(rho,list) or isinstance(rho,np.ndarray):	
	
			rho = np.asarray(rho)
		
		else:
	
			rho = np.asarray([rho])
	
		pwpoly = [K[1]*(rho*rhonuc)**Gamma[1]/rhonuc,K[2]*(rho*rhonuc)**Gamma[2]/rhonuc,K[3]*(rho*rhonuc)**Gamma[3]/rhonuc,K[4]*(rho*rhonuc)**Gamma[4]/rhonuc]
		
		conds = [(rhodiv[0]/rhonuc <= rho) & (rho < rhodiv[1]/rhonuc),(rhodiv[1]/rhonuc <= rho) & (rho < rhodiv[2]/rhonuc),(rhodiv[2]/rhonuc <= rho) & (rho < rhodiv[3]/rhonuc),(rhodiv[3]/rhonuc <= rho) & (rho < rhodiv[4]/rhonuc)]
				
		return np.piecewise(rho,conds,[lambda rho=rho, i=j: pwpoly[i] for j in np.arange(0,4)])
	
	def muSLy(rho):
	
		if isinstance(rho,list) or isinstance(rho,np.ndarray):	
	
			rho = np.asarray(rho)
		
		else:
	
			rho = np.asarray([rho])
	
		pwpolymu = [(K[1]*(rho*rhonuc)**Gamma[1]/(Gamma[1]-1.)+(1.+a[1])*rho*rhonuc)/rhonuc,(K[2]*(rho*rhonuc)**Gamma[2]/(Gamma[2]-1.)+(1.+a[2])*rho*rhonuc)/rhonuc,(K[3]*(rho*rhonuc)**Gamma[3]/(Gamma[3]-1.)+(1.+a[3])*rho*rhonuc)/rhonuc,(K[4]*(rho*rhonuc)**Gamma[4]/(Gamma[4]-1.)+(1.+a[4])*rho*rhonuc)/rhonuc]
	
		conds = [(rhodiv[0]/rhonuc <= rho) & (rho < rhodiv[1]/rhonuc),(rhodiv[1]/rhonuc <= rho) & (rho < rhodiv[2]/rhonuc),(rhodiv[2]/rhonuc <= rho) & (rho < rhodiv[3]/rhonuc),(rhodiv[3]/rhonuc <= rho) & (rho < rhodiv[4]/rhonuc)]
	
		return np.piecewise(rho,conds,[lambda rho=rho, i=j: pwpolymu[i] for j in np.arange(0,4)])

	# FIND CORE-CRUST INTERFACE
	
	def corecrust(p,pSLy):
	
		def intersect(rho):
		
			return abs(p(rho)-pSLy(rho))
	
		res = minimize_scalar(intersect,bounds=(rhodiv[2]/rhonuc,1.),method='bounded')
		rhocr = res.x
	
		return rhocr

	rhocr = corecrust(p,pSLy)

	# BUILD UNIFIED EOS
	
	def puni(rho):
	
		if isinstance(rho,list) or isinstance(rho,np.ndarray):	
	
			rho = np.asarray(rho)
		
		else:
	
			rho = np.asarray([rho])
	
		plist = [pSLy(rho),p(rho)]
	
		return np.piecewise(rho,[rho < rhocr, rho >= rhocr],[lambda rho=rho, i=j: plist[i] for j in np.arange(0,2)])
		
	def muuni(rho):
	
		if isinstance(rho,list) or isinstance(rho,np.ndarray):	
	
			rho = np.asarray(rho)
		
		else:
	
			rho = np.asarray([rho])
	
		mulist = [muSLy(rho),mu(rho)]
	
		return np.piecewise(rho,[rho < rhocr, rho >= rhocr],[lambda rho=rho, i=j: mulist[i] for j in np.arange(0,2)])

	rholist = np.logspace(-12.,np.log10(eosdatx[-1]),pts)
	mudat = np.zeros(len(rholist))
	pdat = np.zeros(len(rholist))
	
	for i in np.arange(len(rholist)):
	
		rho = rholist[i]
	
		mudat[i] = muuni(rho)
		pdat[i] = puni(rho)
	
	return [rholist,mudat,pdat]
