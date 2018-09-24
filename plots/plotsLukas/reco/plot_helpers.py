#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2


MW = 80.385
Mt = 172.5

#
# Text on the plots
#
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

#
# plots
#
def drawPlots(plots, mode, dataMCScale, lumi_scale, selection, directory, noData, normalize):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', directory, mode + ("_log" if log else ""), selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      postFix = " (legacy)"
      if not noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data" + postFix
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)" + postFix
      extensions_ = ["pdf", "png", "root"] if mode == 'all' else ['png']

      plotting.draw(plot,
	    plot_directory = plot_directory_,
        extensions = extensions_,
	    ratio = {'yRange':(0.1,1.9)} if not noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

# check dim6Top reference point
def checkReferencePoint( sample ):
    ''' check if sample is simulated with a reference point
    '''
    return pickle.load(file(sample.reweight_pkl))['ref_point'] != {}

# powheg reweighting
def get_powheg_reweight( histo_pow, histo_amc ):
    def get_histo_reweight(Z_pt):
        return histo_pow.GetBinContent(histo_amc.FindBin( Z_pt ))/histo_amc.GetBinContent(histo_amc.FindBin( Z_pt ) )
    return get_histo_reweight

# define 3l selections
def get3LeptonSelection( mode ):
    if   mode=="mumumu": return "nMuons_tight_3l==3&&nElectrons_tight_3l==0"
    elif mode=="mumue":  return "nMuons_tight_3l==2&&nElectrons_tight_3l==1"
    elif mode=="muee":   return "nMuons_tight_3l==1&&nElectrons_tight_3l==2"
    elif mode=="eee":    return "nMuons_tight_3l==0&&nElectrons_tight_3l==3"
    elif mode=='all':    return "nMuons_tight_3l+nElectrons_tight_3l==3"

# define 2l selections
def get2LeptonSelection( mode ):
    if   mode=="mumu": return "nMuons_tight_3l==2&&nElectrons_tight_3l==0"
    elif mode=="mue":  return "nMuons_tight_3l==1&&nElectrons_tight_3l==1"
    elif mode=="ee":   return "nMuons_tight_3l==0&&nElectrons_tight_3l==2"
    elif mode=='all':    return "nMuons_tight_3l+nElectrons_tight_3l==2"

# define 1l selections
def get1LeptonSelection( mode ):
    if   mode=="mu": return "nMuons_tight_3l==1&&nElectrons_tight_3l==0"
    elif mode=="e":  return "nMuons_tight_3l==0&&nElectrons_tight_3l==1"
    elif mode=='all':    return "nMuons_tight_3l+nElectrons_tight_3l==1"

def addTransverseVector( p_dict ):
    ''' add a transverse vector for further calculations
    '''
    p_dict['vec2D'] = ROOT.TVector2( p_dict['pt']*cos(p_dict['phi']), p_dict['pt']*sin(p_dict['phi']) )

def addTLorentzVector( p_dict ):
    ''' add a TLorentz 4D Vector for further calculations
    '''
    p_dict['vec4D'] = ROOT.TLorentzVector()
    p_dict['vec4D'].SetPtEtaPhiM( p_dict['pt'], p_dict['eta'], p_dict['phi'], 0 )
#    p_dict['vec4D'] = ROOT.TLorentzVector( p_dict['pt']*cos(p_dict['phi']), p_dict['pt']*sin(p_dict['phi']),  p_dict['pt']*sinh(p_dict['eta']), 0 )

def UnitVectorT2( phi ):
    ''' 2D Unit Vector
    '''
    return ROOT.TVector2( cos(phi), sin(phi) )

def MTSquared( p1, p2 ):
    ''' compute MT from 2 particles
    '''
    return 2*p1['pt']*p2['pt']*( 1-cos(p1['phi']-p2['phi']) )

def MSquared( p1, p2 ):
    ''' compute MassSquared from 2 particles
    '''
    return 2*p1['pt']*p2['pt']*( cosh(p1['eta']-p2['eta'])-cos(p1['phi']-p2['phi']) )

def addIDeltaBeta( p_dict ):
    ''' add I_rel^{DeltaBeta}
    '''
    p_dict['IDeltaBeta'] = ( p_dict['sumPtCharged'] + p_dict['sumPtNeutral'] - 0.5* p_dict['sumPtChargedPU'] ) / ( p_dict['pt'] )


def isGoodJet( j ):
    ''' jet object selection
    '''
    return j['pt'] > 30 and abs( j['eta'] ) < 2.4

def isGoodPhoton( j ):
    ''' jet object selection
    '''
    return j['pt'] > 15 and abs( j['eta'] ) < 2.1

def isGoodLepton( l ):
    ''' lepton object selection
    '''
    return l['pt'] > 10 and abs( l['eta'] ) < 2.5 and abs( int(l['pdgId']) ) in [11,13]

def isGoodLooseLepton( l ):
    ''' lepton object selection
    '''
    return l['pt'] > 10 and abs( int(l['pdgId']) ) in [11,13]
