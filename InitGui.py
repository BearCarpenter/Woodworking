class WoodworkingWorkbench(Workbench):  # type: ignore # noqa: F821
  import FreeCAD

  translate = FreeCAD.Qt.translate

  def QT_TRANSLATE_NOOP(context, text):
    return text

  import os
  import sys

  import fakemodule

  path = os.path.dirname(fakemodule.__file__)
  iconPath = os.path.join(path, "Icons")
  translationsPath = os.path.join(path, "translations")

  MenuText = QT_TRANSLATE_NOOP("Workbench", "Woodworking")
  ToolTip = QT_TRANSLATE_NOOP("Workbench", "Workbench for woodworking.")
  Icon = os.path.join(iconPath, "Woodworking.png")

  def Initialize(self):
    import FreeCAD
    import FreeCADGui

    def QT_TRANSLATE_NOOP(context, text):
      return text

    FreeCADGui.addLanguagePath(self.translationsPath)

    # uncomment those lines below if you want to add icon from other workbenches
    # however the DraftTools will slow down the FreeCAD loading
    # for woodworking purposes there will be new tools, so do not cry ;-)

    import PartDesignGui
    import PartGui
    import SketcherGui
    import SpreadsheetGui

    import loadMenu

    # import DraftTools
    import loadToolbar

    # toolbar
    # ################################################################################################

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - default"),
      loadToolbar.getItems("Woodworking - default"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - copy"),
      loadToolbar.getItems("Woodworking - copy"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - move"),
      loadToolbar.getItems("Woodworking - move"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - resize"),
      loadToolbar.getItems("Woodworking - resize"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - special"),
      loadToolbar.getItems("Woodworking - special"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - face"),
      loadToolbar.getItems("Woodworking - face"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - between"),
      loadToolbar.getItems("Woodworking - between"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - construction"),
      loadToolbar.getItems("Woodworking - construction"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - dowels and screws"),
      loadToolbar.getItems("Woodworking - dowels and screws"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - fixture"),
      loadToolbar.getItems("Woodworking - fixture"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - joinery"),
      loadToolbar.getItems("Woodworking - joinery"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - drilling holes"),
      loadToolbar.getItems("Woodworking - drilling holes"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - project manage"),
      loadToolbar.getItems("Woodworking - project manage"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - code and debug"),
      loadToolbar.getItems("Woodworking - code and debug"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - dimensions"),
      loadToolbar.getItems("Woodworking - dimensions"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - router"),
      loadToolbar.getItems("Woodworking - router"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - decorations"),
      loadToolbar.getItems("Woodworking - decorations"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - advanced"),
      loadToolbar.getItems("Woodworking - advanced"),
    )

    self.appendToolbar(
      QT_TRANSLATE_NOOP("Workbench", "Woodworking - preview"),
      loadToolbar.getItems("Woodworking - preview"),
    )

    # menu
    # ################################################################################################

    self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "Woodworking"), loadMenu.getItems())

  def Activated(self):
    # not needed now, maybe in the future
    return

  def Deactivated(self):
    # not needed now, maybe in the future
    return

  def ContextMenu(self, recipient):
    # not needed now, maybe in the future
    return

  def GetClassName(self):
    return "Gui::PythonWorkbench"


Gui.addWorkbench(WoodworkingWorkbench())
