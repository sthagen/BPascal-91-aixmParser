#!/usr/bin/env python3

import bpaTools
import aixmReader

if __name__ == '__main__':
    ### Context applicatif
    callingContext      = "Paragliding-OpenAir-French-Files"         #Your app calling context
    linkContext         = "http://pascal.bazile.free.fr/paraglidingFolder/divers/GPS/OpenAir-Format/"
    appName             = "aixmParser"                              #or your app name
    appPath             = bpaTools.getFilePath(__file__)            #or your app path
    appVersion          = bpaTools.getVersionFile()                 #or your app version
    appId               = appName + " v" + appVersion
    outPath             = appPath + "../out/"
    logFile             = outPath + "_" + appName + ".log"
    bpaTools.createFolder(outPath)                                  #Init dossier de sortie

    ####  Source test file  ####
    srcFile = "../tst/aixm4.5_SIA-FR_map-Airspaces.xml"
    #srcFile = "../tst/aixm4.5_SIA-FR_ctrl-Airspaces.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_Test4CleaningCatalog_aixm45.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_Test4AppendDelta1_aixm45.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_Test4AppendDelta2_aixm45.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_TestBORDERs_aixm45.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_Test4Circles_Arcs_aixm45.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_Test4ZonesWithArc.xml"
    #srcFile = "../../poaff/input/Tests/99999999_BPa_TestGroundEstimatedHeight_aixm45.xml"
    #srcFile = "../../poaff/output/Tests/map/99999999_ComplexArea_aixm45.xml"
    #srcFile = "../../poaff/input/FFVP/20201204_FFVP_ParcsNat_BPa_aixm45.xml"
    #srcFile = "../../poaff/input/FFVP/20191214_FFVP_BirdsProtect_aixm45.xml"
    #srcFile = "../../poaff/input/FFVL/20210104_FFVL_ParcBauges_BPa_aixm45.xml"
    #srcFile = "../../poaff/input/FFVL/20210122_FFVL_ZonesComplementaires_aixm45.xml"
    #srcFile = "../../poaff/input/BPa/20210101_LTA-ExtractSIA_BPa_aixm45.xml"
    #srcFile = "../../poaff/input/BPa/20230313_LTA-ExtractSIA_BPa_aixm45.xml"
    #srcFile = "../../poaff/input/BPa/20230331_BPa_ZonesComplementaires_aixm45.xml"
    #srcFile = "../../poaff/input/BPa/20230330_BPa_FR-ZSM_Protection-des-rapaces_aixm45.xml"
    #srcFile = "../../poaff/input/FFVL/20220402_FFVL_ProtocolesParticuliers_BPa_aixm45.xml"
    #srcFile = "../../poaff/input/BPa/20230417_BPa_FR-SIA-SUPAIP_aixm45.xml"

    #sSrcPath:str = "D:/_Users_/BPascal/_4_Src/GitHub/poaff/input/LPO_Biodiv/"
    #srcFile = sSrcPath + "20230401_biodiv-sports-fr_Parc_aixm45.xml"
    #srcFile = sSrcPath + "20230403_biodiv-sports-fr_Zsm-Active_aixm45.xml"

    #sSrcPath:str = "D:\_Users_\BPascal\_4_Src\GitHub\poaff\input\SpotAir/"
    #srcFile = sSrcPath + "20231229c_zsm-SpotAir_aixm45.xml"

    sSrcPath:str = "D:\_Users_\BPascal\_4_Src\GitHub\poaff\input\STAC/"
    srcFile = sSrcPath + "20240229_ZSM-coeur-france_aixm45.xml"

    ####  quelques options d'appels  ####
    #Simulation des arguments d'appels 'sys.argv' via le tableau 'aArgv'
    #------- tests unitaires ---
    #aArgv = [appName, srcFile, "-Fgeojson", aixmReader.CONST.optTstGeojson, aixmReader.CONST.optDraft]
    #aArgv = [appName, srcFile, "-Fgeojson", aixmReader.CONST.typeAIRSPACES, aixmReader.CONST.optFreeFlight, aixmReader.CONST.optMakePoints4map]
    #------- tests de non-reg ---
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeCTRLTOWERS]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeAERODROMES]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeOBSTACLES]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeRUNWAYCENTER]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeGATESTANDS]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeGEOBORDER]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeAIRSPACES, aixmReader.CONST.optIFR, aixmReader.CONST.optVFR, aixmReader.CONST.optFreeFlight]
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeAIRSPACES, aixmReader.CONST.optFreeFlight]
    #------- appels standards ---
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeAIRSPACES, aixmReader.CONST.optFreeFlight]
    aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeALL, aixmReader.CONST.optALL, aixmReader.CONST.optIFR, aixmReader.CONST.optVFR, aixmReader.CONST.optFreeFlight]


    #### 4POAFF - Tests for real bigData files ####
    #srcFile = "../../poaff/input/SIA/20200813-20200909_aixm4.5_SIA-FR.xml"
    #srcFile = "../../poaff/input/EuCtrl/20200618_aixm4.5_Eurocontrol-FR.xml"
    #srcFile = "../../poaff/input/EuCtrl/20201231_aixm4.5_Eurocontrol-Euro_BPa.xml"
    #aArgv = [appName, srcFile, aixmReader.CONST.frmtALL, aixmReader.CONST.typeAIRSPACES, aixmReader.CONST.optVFR, aixmReader.CONST.optFreeFlight]


    ####  Ajout d'options d'appel  ####
    aArgv += [aixmReader.CONST.optCleanLog]                         #Mode classique avec log et afficages sur console système
    #aArgv += [aixmReader.CONST.optDraft]                           #Mode Draft sur les tracés d'arcs ou de cercles
    #aArgv += [aixmReader.CONST.optSilent]                          #Mode silencieux sans utilisation du fichier log et sans retour d'affichage
    #aArgv += [aixmReader.CONST.optGeojsonDigitOptimize + "=10"]    #Optimisation par arrondi des coordonnées Geojson (default=6)
    aArgv += [aixmReader.CONST.optOpenairDigitOptimize + "=0"]      #Optimisation par arrondi des coordonnées Openair (default=-1)
    aArgv += [aixmReader.CONST.optEpsilonReduce + "=0.0001"]        #Optimisation des tracés Default=0 removal-duplicates-values and no-optimize, <0 for no-optimize or >0 for optimize, sample=0.0001 / 0.001 / 0.002

    ####  Préparation d'appel ####
    oOpts = bpaTools.getCommandLineOptions(aArgv)       #Arguments en dictionnaire

    oLog = bpaTools.Logger(appId, logFile, callingContext, linkContext, debugLevel=1, isSilent=bool(aixmReader.CONST.optSilent in oOpts))
    if aixmReader.CONST.optCleanLog in oOpts:
        oLog.resetFile()                                #Clean du log si demandé
    oLog.writeCommandLine(aArgv)                        #Trace le contexte d'execution
    aixmCtrl = aixmReader.AixmControler(srcFile, outPath, "", oLog=oLog)	    #Init controler
    if aixmCtrl.execParser(oOpts):                                              #Execution des traitements
        print()
        if oLog.CptCritical or oLog.CptError:
            print("/!\ Processing Error(s)")
        oLog.Report()
    oLog.closeFile()

