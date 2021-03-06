import os
import unittest
import vtk, qt, ctk, slicer
from DICOMLib import DICOMUtils
from slicer.ScriptedLoadableModule import *

#
# RSNAVisTutorial
#

class RSNAVisTutorial(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    parent.title = "RSNAVisTutorial" # TODO make this more human readable by adding spaces
    parent.categories = ["Testing.TestCases"]
    parent.dependencies = []
    parent.contributors = ["Steve Pieper (Isomics)"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    This module was developed as a self test to perform the operations needed for the RSNA 2012 Visualization Tutorial
    """
    parent.acknowledgementText = """
    This file was originally developed by Steve Pieper, Isomics, Inc.  and was partially funded by NIH grant 3P41RR013218-12S1.
""" # replace with organization, grant and thanks.

#
# qRSNAVisTutorialWidget
#

class RSNAVisTutorialWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Instantiate and connect widgets ...

    # Collapsible button
    testsCollapsibleButton = ctk.ctkCollapsibleButton()
    testsCollapsibleButton.text = "Tests"
    self.layout.addWidget(testsCollapsibleButton)

    # Layout within the collapsible button
    formLayout = qt.QFormLayout(testsCollapsibleButton)

    # test buttons
    tests = ( ("Part 1: DICOM",self.onPart1DICOM),("Part 2: Head", self.onPart2Head),("Part 3: Liver", self.onPart3Liver),("Part 4: Lung", self.onPart4Lung),)
    for text,slot in tests:
      testButton = qt.QPushButton(text)
      testButton.toolTip = "Run the test."
      formLayout.addWidget(testButton)
      testButton.connect('clicked(bool)', slot)

    # A collapsible button to hide screen shot options
    screenShotsCollapsibleButton = ctk.ctkCollapsibleButton()
    screenShotsCollapsibleButton.text = "Screen shot options"
    self.layout.addWidget(screenShotsCollapsibleButton)

    # layout within the collapsible button
    screenShotsFormLayout = qt.QFormLayout(screenShotsCollapsibleButton)

    #
    # check box to trigger taking screen shots for later use in tutorials
    #
    self.enableScreenshotsFlagCheckBox = qt.QCheckBox()
    self.enableScreenshotsFlagCheckBox.checked = 0
    self.enableScreenshotsFlagCheckBox.setToolTip("If checked, take screen shots for tutorials. Use Save Data to write them to disk.")
    screenShotsFormLayout.addRow("Enable Screenshots", self.enableScreenshotsFlagCheckBox)

    #
    # scale factor for screen shots
    #
    self.screenshotScaleFactorSliderWidget = ctk.ctkSliderWidget()
    self.screenshotScaleFactorSliderWidget.singleStep = 1.0
    self.screenshotScaleFactorSliderWidget.minimum = 1.0
    self.screenshotScaleFactorSliderWidget.maximum = 50.0
    self.screenshotScaleFactorSliderWidget.value = 1.0
    self.screenshotScaleFactorSliderWidget.setToolTip("Set scale factor for the screen shots.")
    screenShotsFormLayout.addRow("Screenshot scale factor", self.screenshotScaleFactorSliderWidget)

    # Add vertical spacer
    self.layout.addStretch(1)

  def onPart1DICOM(self):
    enableScreenshotsFlag = self.enableScreenshotsFlagCheckBox.checked
    screenshotScaleFactor = int(self.screenshotScaleFactorSliderWidget.value)

    tester = RSNAVisTutorialTest()
    tester.setUp()
    tester.test_Part1DICOM(enableScreenshotsFlag,screenshotScaleFactor)

  def onPart2Head(self):
    enableScreenshotsFlag = self.enableScreenshotsFlagCheckBox.checked
    screenshotScaleFactor = int(self.screenshotScaleFactorSliderWidget.value)

    tester = RSNAVisTutorialTest()
    tester.setUp()
    tester.test_Part2Head(enableScreenshotsFlag,screenshotScaleFactor)

  def onPart3Liver(self):
    enableScreenshotsFlag = self.enableScreenshotsFlagCheckBox.checked
    screenshotScaleFactor = int(self.screenshotScaleFactorSliderWidget.value)

    tester = RSNAVisTutorialTest()
    tester.setUp()
    tester.test_Part3Liver(enableScreenshotsFlag,screenshotScaleFactor)

  def onPart4Lung(self):
    enableScreenshotsFlag = self.enableScreenshotsFlagCheckBox.checked
    screenshotScaleFactor = int(self.screenshotScaleFactorSliderWidget.value)

    tester = RSNAVisTutorialTest()
    tester.setUp()
    tester.test_Part4Lung(enableScreenshotsFlag,screenshotScaleFactor)

  def onReload(self,moduleName="RSNAVisTutorial"):
    """Generic reload method for any scripted module.
    ModuleWizard will substitute correct default moduleName.
    """
    globals()[moduleName] = slicer.util.reloadScriptedModule(moduleName)

  def onReloadAndTest(self,moduleName="RSNAVisTutorial"):
    self.onReload()
    evalString = 'globals()["%s"].%sTest()' % (moduleName, moduleName)
    tester = eval(evalString)
    tester.runTest()

#
# RSNAVisTutorialLogic
#

class RSNAVisTutorialLogic(ScriptedLoadableModuleLogic):
  """This class should implement all the actual
  computation done by your module.  The interface
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget.
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
  pass

class RSNAVisTutorialTest(ScriptedLoadableModuleTest):
  """
  This is the test case for your scripted module.
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    self.delayDisplay("Closing the scene")
    layoutManager = slicer.app.layoutManager()
    layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalView)
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    self.test_Part1DICOM()
    self.setUp()
    self.test_Part2Head()
    self.setUp()
    self.test_Part3Liver()
    self.setUp()
    self.test_Part4Lung()

  def test_Part1DICOM(self,enableScreenshotsFlag=0,screenshotScaleFactor=1):
    """ Test the DICOM part of the test using the head atlas
    """

    logic = RSNAVisTutorialLogic()
    logic.enableScreenshots = enableScreenshotsFlag
    logic.screenshotScaleFactor = screenshotScaleFactor

    import os
    self.delayDisplay("Starting the DICOM test")
    #
    # first, get the data - a zip file of dicom data
    #
    import SampleData
    dicomFilesDirectory = SampleData.downloadFromURL(
      fileNames='dataset1_Thorax_Abdomen.zip',
      uris='http://slicer.kitware.com/midas3/download?items=124183')[0]

    try:
      self.delayDisplay("Switching to temp database directory")
      originalDatabaseDirectory = DICOMUtils.openTemporaryDatabase('tempDICOMDatabase')

      self.delayDisplay('Importing DICOM')
      mainWindow = slicer.util.mainWindow()
      mainWindow.moduleSelector().selectModule('DICOM')

      indexer = ctk.ctkDICOMIndexer()
      indexer.addDirectory(slicer.dicomDatabase, dicomFilesDirectory, None)
      indexer.waitForImportFinished()

      dicomWidget = slicer.modules.DICOMWidget
      dicomWidget.detailsPopup.open()

      # load the data by series UID
      dicomWidget.detailsPopup.offerLoadables('1.3.12.2.1107.5.1.4.50025.30000005060811542834300000776','Series')
      dicomWidget.detailsPopup.examineForLoading()

      self.delayDisplay('Loading Selection')
      dicomWidget.detailsPopup.loadCheckedLoadables()

      logic.takeScreenshot('LoadingADICOMVolume-Loaded','Loaded DICOM Volume',-1)

      layoutManager = slicer.app.layoutManager()
      redWidget = layoutManager.sliceWidget('Red')
      slicer.util.clickAndDrag(redWidget,start=(10,10),end=(10,40))
      slicer.util.clickAndDrag(redWidget,start=(10,10),end=(40,10))

      logic.takeScreenshot('LoadingADICOMVolume-WL','Changed level and window',-1)

      redWidget.sliceController().setSliceLink(True)
      redWidget.sliceController().setSliceVisible(True);
      logic.takeScreenshot('LoadingADICOMVolume-LinkView','Linked and visible',-1)

      slicer.util.clickAndDrag(redWidget,button='Right',start=(10,10),end=(10,40))
      logic.takeScreenshot('LoadingADICOMVolume-Zoom','Zoom',-1)

      threeDView = layoutManager.threeDWidget(0).threeDView()
      slicer.util.clickAndDrag(threeDView)
      logic.takeScreenshot('LoadingADICOMVolume-Rotate','Rotate',-1)

      threeDView.resetFocalPoint()
      logic.takeScreenshot('LoadingADICOMVolume-Center','Center the view',-1)

      layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalWidescreenView)
      logic.takeScreenshot('LoadingADICOMVolume-ConventionalWidescreen','Conventional Widescreen Layout',-1)

      slicer.util.mainWindow().moduleSelector().selectModule('VolumeRendering')
      logic.takeScreenshot('VolumeRendering-Module','Volume Rendering',-1)

      volumeRenderingWidgetRep = slicer.modules.volumerendering.widgetRepresentation()
      abdomenVolume = slicer.mrmlScene.GetFirstNodeByName('6: CT_Thorax_Abdomen')
      volumeRenderingWidgetRep.setMRMLVolumeNode(abdomenVolume)
      logic.takeScreenshot('VolumeRendering-SelectVolume','Select the volume 6: CT_Thorax_Abdomen',-1)

      presetsScene = slicer.modules.volumerendering.logic().GetPresetsScene()
      ctCardiac3 = presetsScene.GetFirstNodeByName('CT-Cardiac3')
      volumeRenderingWidgetRep.applyPreset(ctCardiac3)
      logic.takeScreenshot('VolumeRendering-SelectPreset','Select the Preset CT-Cardiac-3')

      self.delayDisplay('Skipping: Select VTK CPU Ray Casting')

      volumeRenderingNode = slicer.mrmlScene.GetFirstNodeByName('VolumeRendering')
      volumeRenderingNode.SetVisibility(1)
      logic.takeScreenshot('VolumeRendering-ViewRendering','View Volume Rendering',-1)

      self.delayDisplay('Skipping Move the Shift slider')

      redWidget.sliceController().setSliceVisible(False);
      logic.takeScreenshot('VolumeRendering-SlicesOff','Turn off visibility of slices in 3D',-1)

      threeDView = layoutManager.threeDWidget(0).threeDView()
      slicer.util.clickAndDrag(threeDView)
      logic.takeScreenshot('VolumeRendering-RotateVolumeRendering','Rotate volume rendered image',-1)

      volumeRenderingNode.SetVisibility(0)
      logic.takeScreenshot('VolumeRendering-TurnOffVolumeRendering','Turn off volume rendered image',-1)

      volumeRenderingNode.SetCroppingEnabled(1)
      annotationROI = slicer.mrmlScene.GetFirstNodeByName('AnnotationROI')
      annotationROI.SetDisplayVisibility(1)
      logic.takeScreenshot('VolumeRendering-DisplayROI','Enable cropping and display ROI',-1)

      redWidget.sliceController().setSliceVisible(True)
      logic.takeScreenshot('VolumeRendering-SlicesOn','Turn on visibility of slices in 3D',-1)

      annotationROI.SetXYZ(-79.61,154.16,-232.591)
      annotationROI.SetRadiusXYZ(43.4,65.19,70.5)
      logic.takeScreenshot('VolumeRendering-SizedROI','Position the ROI over a kidney',-1)

      volumeRenderingNode.SetVisibility(1)
      logic.takeScreenshot('VolumeRendering-ROIRendering','ROI volume rendered',-1)

      annotationROI.SetXYZ(15,146,-186)
      annotationROI.SetRadiusXYZ(138,57,61)
      logic.takeScreenshot('VolumeRendering-BothKidneys','Rendered both kidneys',-1)

      self.delayDisplay('Test passed!')
    except Exception as e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e))

    self.delayDisplay("Restoring original database directory")
    DICOMUtils.closeTemporaryDatabase(originalDatabaseDirectory)

  def test_Part2Head(self,enableScreenshotsFlag=0,screenshotScaleFactor=1):
    """ Test using the head atlas - may not be needed - Slicer4Minute is already tested
    """
    logic = RSNAVisTutorialLogic()
    logic.enableScreenshots = enableScreenshotsFlag
    logic.screenshotScaleFactor = screenshotScaleFactor

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    import SampleData
    SampleData.downloadFromURL(
      fileNames='Head_Scene.mrb',
      loadFiles=True,
      uris='http://slicer.kitware.com/midas3/download?items=124180')

    logic.takeScreenshot('Head-Downloaded','Finished with download and loading',-1)

    try:
      mainWindow = slicer.util.mainWindow()
      layoutManager = slicer.app.layoutManager()
      threeDView = layoutManager.threeDWidget(0).threeDView()
      redWidget = layoutManager.sliceWidget('Red')
      redController = redWidget.sliceController()
      greenWidget = layoutManager.sliceWidget('Green')
      greenController = greenWidget.sliceController()

      mainWindow.moduleSelector().selectModule('Models')
      redWidget.sliceController().setSliceVisible(True);
      logic.takeScreenshot('Head-ModelsAndSliceModel','Models and Slice Model',-1)

      slicer.util.clickAndDrag(threeDView)
      logic.takeScreenshot('Head-Rotate','Rotate',-1)

      redController.setSliceVisible(True);
      logic.takeScreenshot('Head-AxialSlice','Display Axial Slice',-1)

      layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalView)
      logic.takeScreenshot('Head-ConventionalView','Conventional Layout',-1)

      viewNode = threeDView.mrmlViewNode()
      cameras = slicer.util.getNodes('vtkMRMLCameraNode*')
      for cameraNode in cameras.values():
        if cameraNode.GetActiveTag() == viewNode.GetID():
          break
      cameraNode.GetCamera().Azimuth(90)
      cameraNode.GetCamera().Elevation(20)

      # turn off skin and skull
      skin = slicer.util.getNode(pattern='Skin.vtk')
      skin.GetDisplayNode().SetOpacity(0.5)
      logic.takeScreenshot('Head-SkinOpacity','Skin Opacity to 0.5',-1)

      skin.GetDisplayNode().SetVisibility(0)
      logic.takeScreenshot('Head-SkinOpacityZero','Skin Opacity to 0',-1)

      skull = slicer.util.getNode(pattern='skull_bone.vtk')

      greenWidget.sliceController().setSliceVisible(True);
      logic.takeScreenshot('Head-GreenSlice','Display Coronal Slice',-1)

      # hemispheric_white_matter.GetDisplayNode().SetClipping(1)
      skull.GetDisplayNode().SetClipping(1)
      clip = slicer.util.getNode(pattern='vtkMRMLClipModelsNode1')
      clip.SetRedSliceClipState(0)
      clip.SetYellowSliceClipState(0)
      clip.SetGreenSliceClipState(2)
      logic.takeScreenshot('Head-SkullClipping','Turn on clipping for skull model',-1)

      for offset in range(-20,20,2):
        greenController.setSliceOffsetValue(offset)
      logic.takeScreenshot('Head-ScrollCoronal','Scroll through coronal slices',-1)

      skull.GetDisplayNode().SetVisibility(0)
      logic.takeScreenshot('Head-HideSkull','Make the skull invisible',-1)

      for offset in range(-40,-20,2):
        greenController.setSliceOffsetValue(offset)
      logic.takeScreenshot('Head-ScrollCoronalWhiteMatter','Scroll through coronal slices to show white matter',-1)

      hemispheric_white_matter = slicer.util.getNode(pattern='hemispheric_white_matter.vtk')
      hemispheric_white_matter.GetDisplayNode().SetVisibility(0)
      logic.takeScreenshot('Head-HideWhiteMatter','Turn off white matter',-1)

      self.delayDisplay('Rotate')
      slicer.util.clickAndDrag(threeDView)

      self.delayDisplay('Zoom')
      threeDView = layoutManager.threeDWidget(0).threeDView()
      slicer.util.clickAndDrag(threeDView,button='Right')
      logic.takeScreenshot('Head-Zoom','Zoom',-1)

      self.delayDisplay('Test passed!')
    except Exception as e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e))


  def test_Part3Liver(self,enableScreenshotsFlag=0,screenshotScaleFactor=1):
    """ Test using the liver example data
    """
    logic = RSNAVisTutorialLogic()
    logic.enableScreenshots = enableScreenshotsFlag
    logic.screenshotScaleFactor = screenshotScaleFactor

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    import SampleData
    SampleData.downloadFromURL(
      fileNames='LiverSegments_Scene.mrb',
      loadFiles=True,
      uris='http://slicer.kitware.com/midas3/download?items=124181')

    logic.takeScreenshot('Liver-Loaded','Loaded Liver scene',-1)

    try:
      logic = RSNAVisTutorialLogic()
      mainWindow = slicer.util.mainWindow()
      layoutManager = slicer.app.layoutManager()
      threeDView = layoutManager.threeDWidget(0).threeDView()
      redWidget = layoutManager.sliceWidget('Red')
      redController = redWidget.sliceController()
      viewNode = threeDView.mrmlViewNode()
      cameras = slicer.util.getNodes('vtkMRMLCameraNode*')
      for cameraNode in cameras.values():
        if cameraNode.GetActiveTag() == viewNode.GetID():
          break

      mainWindow.moduleSelector().selectModule('Models')
      logic.takeScreenshot('Liver-Models','Models module',-1)

      segmentII = slicer.util.getNode('LiverSegment_II')
      segmentII.GetDisplayNode().SetVisibility(0)
      slicer.util.clickAndDrag(threeDView,start=(10,200),end=(10,10))
      logic.takeScreenshot('Liver-SegmentII','Segment II invisible',-1)

      segmentII.GetDisplayNode().SetVisibility(1)
      logic.takeScreenshot('Liver-SegmentII','Segment II visible',-1)

      cameraNode.GetCamera().Azimuth(0)
      cameraNode.GetCamera().Elevation(0)
      logic.takeScreenshot('Liver-SuperiorView','Superior view',-1)

      segmentII.GetDisplayNode().SetVisibility(0)
      cameraNode.GetCamera().Azimuth(180)
      cameraNode.GetCamera().Elevation(-30)
      redWidget.sliceController().setSliceVisible(True);
      logic.takeScreenshot('Liver-ViewAdrenal','View Adrenal',-1)

      models = slicer.util.getNodes('vtkMRMLModelNode*')
      for modelNode in models.values():
        modelNode.GetDisplayNode().SetVisibility(0)

      transparentNodes = ('MiddleHepaticVein_and_Branches','LiverSegment_IVb','LiverSegmentV',)
      for nodeName in transparentNodes:
        modelNode = slicer.util.getNode(nodeName)
        modelNode.GetDisplayNode().SetOpacity(0.5)
        modelNode.GetDisplayNode().SetVisibility(1)
      cameraNode.GetCamera().Azimuth(30)
      cameraNode.GetCamera().Elevation(-20)
      redWidget.sliceController().setSliceVisible(True);
      logic.takeScreenshot('Liver-MiddleHepatic','Middle Hepatic',-1)

      self.delayDisplay('Test passed!')
    except Exception as e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e))

  def test_Part4Lung(self,enableScreenshotsFlag=0,screenshotScaleFactor=1):
    """ Test using the lung data
    """
    logic = RSNAVisTutorialLogic()
    logic.enableScreenshots = enableScreenshotsFlag
    logic.screenshotScaleFactor = screenshotScaleFactor

    self.delayDisplay("Starting the test")
    #
    # first, get some data
    #
    import SampleData
    SampleData.downloadFromURL(
      fileNames='LungSegments_Scene.mrb',
      loadFiles=True,
      uris='http://slicer.kitware.com/midas3/download?items=124182')

    logic.takeScreenshot('Lung-Loaded','Finished with download and loading',-1)

    try:
      mainWindow = slicer.util.mainWindow()
      layoutManager = slicer.app.layoutManager()
      threeDView = layoutManager.threeDWidget(0).threeDView()
      redWidget = layoutManager.sliceWidget('Red')
      redController = redWidget.sliceController()
      viewNode = threeDView.mrmlViewNode()
      cameras = slicer.util.getNodes('vtkMRMLCameraNode*')
      for cameraNode in cameras.values():
        if cameraNode.GetActiveTag() == viewNode.GetID():
          break

      threeDView.resetFocalPoint()
      logic.takeScreenshot('Lung-ResetView','Reset view',-1)

      mainWindow.moduleSelector().selectModule('Models')
      logic.takeScreenshot('Lung-Models','Models module',-1)

      cameraNode.GetCamera().Azimuth(-100)
      cameraNode.GetCamera().Elevation(-40)
      redWidget.sliceController().setSliceVisible(True);
      lungs = slicer.util.getNode('chestCT_lungs')
      lungs.GetDisplayNode().SetVisibility(0)
      logic.takeScreenshot('Lung-Question1','View Question 1',-1)

      cameraNode.GetCamera().Azimuth(-65)
      cameraNode.GetCamera().Elevation(-20)
      lungs.GetDisplayNode().SetVisibility(1)
      lungs.GetDisplayNode().SetOpacity(0.24)
      redController.setSliceOffsetValue(-50)
      logic.takeScreenshot('Lung-Question2','View Question 2',-1)

      cameraNode.GetCamera().Azimuth(-165)
      cameraNode.GetCamera().Elevation(-10)
      redWidget.sliceController().setSliceVisible(False);
      logic.takeScreenshot('Lung-Question3','View Question 3',-1)

      cameraNode.GetCamera().Azimuth(20)
      cameraNode.GetCamera().Elevation(-10)
      lowerLobeNodes = slicer.util.getNodes('*LowerLobe*')
      for showNode in lowerLobeNodes:
        self.delayDisplay('Showing Node %s' % showNode, 300)
        for node in lowerLobeNodes:
          displayNode = lowerLobeNodes[node].GetDisplayNode()
          if displayNode:
            displayNode.SetVisibility(1 if node == showNode else 0)
      logic.takeScreenshot('Lung-Question4','View Question 4',-1)

      self.delayDisplay('Test passed!')
    except Exception as e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e))
