
import viz
import vizshape
import vizfx
viz.go()
viz.addChild('sky_day.osgb')
#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

showhouse = viz.addChild('house.osgb')

#viz.MainView.move([20,0,15.5])
viz.MainView.move([5,0,3])

light = vizfx.addDirectionalLight(euler=(0,90,0), color=viz.WHITE)
light.setIntensity(0.3)

#----------------gymroom-------------------
#add and set object position
gymball = viz.addChild('gymball.osgb')
gymball.setPosition([22.5, 0.2, 24.5])

gym1 = viz.addChild('gymone.osgb')
gym1.setPosition([22, 0.1, 22])

gym2 = viz.addChild('gymtwo.osgb')
gym2.setPosition([22.5, 0.13, 19])
gym2.setEuler(90,0,0)

gym3 = viz.addChild('gymthree.osgb')
gym3.setPosition([22.5, 0.2, 16.5])
gym3.setEuler(180,0,0)

table = viz.addChild('table.osgb')
table.setPosition([16.8, 0.6, 19.5])
table.setEuler(90,0,0)
table.setScale([2,2,3])

bench = viz.addChild('bench.osgb')
bench.setPosition([17, 0.24, 22.5])
bench.setEuler(90,0,0)
bench.setScale([1,0.5,0.5])

kettlebellrack = viz.addChild('kettlebellrack.osgb')
kettlebellrack.setPosition([21, 0.22, 15.8])
kettlebellrack.setEuler(180,0,0)

dumbbellrack = viz.addChild('dumbbellrack.osgb')
dumbbellrack.setPosition([19, 0.22, 15.8])
dumbbellrack.setEuler(180,0,0)

speaker = viz.addChild('speaker.osgb')
speaker.setPosition([18, 0.247, 24.5])

projector = viz.addChild('projector.osgb')
projector.setPosition([20.2, 0.2, 22.5])

towel = viz.addChild('towel.osgb')
towel.setPosition([17, 1.03, 20])
towel.setScale([1.5,1.5,1.5])

bottle = viz.addChild('bottle.osgb')
bottle.setPosition([17, 0.93, 19])
bottle.setScale([1.5,1.5,1.5])

kettlebell = viz.addChild('kettlebell.osgb')
kettlebell.setPosition([21.3, 0.241, 15.8])

dumbbell = viz.addChild('dumbbel15.osgb')
dumbbell.setPosition([19.2, 0, 15.8])
dumbbell.setScale([1.5,1.5,1.5])

#--------------Living Room----------------
sofa = viz.addChild('sofa new.osgb')
sofa.setPosition([7,0.3,13])
sofa.setEuler(-90,0,0)
#sofa.setScale([1,1,1])

lamp = viz.addChild('lamp.osgb')
lamp.setPosition([3,0.3,13])
lamp.setEuler(45,0,0)

table = viz.addChild('coffee table.osgb')
table.setPosition([4,0.35,14.5])

books = viz.addChild('books.osgb')
books.setPosition([4.5,0.58,15.4])
books.setEuler(45,0,0)

book = viz.addChild('book_01.osgb')
book.setPosition([4.8,0.74,15.2])
book.setScale([1.5,1.5,1.5])
book.setEuler(45,0,0)

pillow = viz.addChild('pillow6.osgb')
pillow.setPosition([5,0.9,13.2])
pillow.setEuler(0,30,0)
pillow.setScale([1.5,1.5,1.5])

tray = viz.addChild('tray.osgb')
tray.setPosition([5.5,0.58,15.3])
tray.setScale([1.5,1.5,1.5])

teapot = viz.addChild('teapot.osgb')
teapot.setPosition([5.5,0.6,15.3])

teacup1 = viz.addChild('teacup.osgb')
teacup1.setPosition([5.8,0.6,15.25])

teacup2 = viz.addChild('teacup.osgb')
teacup2.setPosition([5.8,0.6,15.45])

flower = viz.addChild('flower.osgb')
flower.setPosition([3.7,0.77,17])
flower.setScale([0.6,0.6,0.6])

tvliving = viz.addChild('tvliving.osgb')
tvliving.setPosition([4.6,0.78,17.55])
tvliving.setScale([0.95,0.8,0.95])

speaker1 = viz.addChild('speaker1.osgb')
speaker1.setPosition([6.5,0.78,17.5])
speaker1.setEuler(60,0,0)
speaker1.setScale([0.8,0.8,0.8])

laptop = viz.addChild('laptop.osgb')
laptop.setPosition([6.7,1.32,22])
laptop.setEuler(90,0,0)

#--------------Bedroom----------------
bed=viz.addChild('bed.osgb')
bed.setPosition([14.5,3.33,14])
bed.setEuler(180,0,0)
bed.setScale([1,1,1])

studytable=viz.addChild('studytable.osgb')
studytable.setPosition([11.6,3.33,16.1])
studytable.setEuler(0,0,0)
studytable.setScale([0.68,1,1])

standlamp=viz.addChild('standlamp.osgb')
standlamp.setPosition([11.6,3.33,2.3])
standlamp.setEuler(0,0,0)
standlamp.setScale([0.68,1,1])

cabinet=viz.addChild('cabinet.osgb')
cabinet.setPosition([10.48,3.33,12.5])
cabinet.setEuler(-90,0,0)
cabinet.setScale([1,1,1])

bear=viz.addChild('bear.osgb')
bear.setPosition([13.8,3.33,15])
bear.setEuler(180,0,0)
bear.setScale([0.34,0.23,0.27])

curtain=viz.addChild('curtain.osgb')
curtain.setPosition([10.47,3.33,12])
curtain.setEuler(0,0,0)
curtain.setScale([1.71,0.86,1])

blanket=viz.addChild('blanket.osgb')
blanket.setPosition([14.1,3.89,12.3])
blanket.setEuler(-91,0,0)
blanket.setScale([3.7,1,4.2])

clothing=viz.addChild('clothing.osgb')
clothing.setPosition([11,4.04,13])
clothing.setEuler(-91,0,0)
clothing.setScale([1,1,1])

books2=viz.addChild('books2.osgb')
books2.setPosition([10.8,4.04,13.02])
books2.setEuler(180,0,0)
books2.setScale([0.01,0.01,0.01])

bolsters=viz.addChild('bolsters.osgb')
bolsters.setPosition([12.8,3.664,13.8])
bolsters.setEuler(140,0,0)
bolsters.setScale([0.8,0.9,0.8])

radio=viz.addChild('radio.osgb')
radio.setPosition([12.7,4.052,13.1])
radio.setEuler(-90,0,0)
radio.setScale([1,1,1])

iPad=viz.addChild('iPad.osgb')
iPad.setPosition([11.6,4.039,15.53])
iPad.setEuler(0,0,0)
iPad.setScale([0.37,0.4,0.37])

laptop2=viz.addChild('laptop.osgb')
laptop2.setPosition([10.3,4.041,14.7])
laptop2.setEuler(0,0,0)

#--------------Backyard----------------
beachball = viz.addChild('BeachBall.osgb')
beachball.setPosition([8,0.35,30])
beachball.setEuler(180,0,0)
beachball.setScale([0.3,0.3,0.3])

firepit = viz.addChild('firepit.osgb')
firepit.setPosition([20,0.23,33])
firepit.setEuler(180,0,0)
firepit.setScale([1.5,1.5,1.5])

rubberduck = viz.addChild('rubberduck.osgb')
rubberduck.setPosition([5,0.2,30])
rubberduck.setEuler(180,0,0)
rubberduck.setScale([1.5,1.5,1.5])

rubberduck1 = viz.addChild('rubberduck.osgb')
rubberduck1.setPosition([4.5,0.2,30])
rubberduck1.setEuler(180,0,0)
rubberduck1.setScale([1.5,1.5,1.5])

rubberduck2 = viz.addChild('rubberduck.osgb')
rubberduck2.setPosition([4,0.2,28])
rubberduck2.setEuler(90,0,0)
rubberduck2.setScale([1.5,1.5,1.5])

sunglasses = viz.addChild('Sunglasses.osgb')
sunglasses.setPosition([10,1.15,33])
sunglasses.setEuler(90,0,0)
sunglasses.setScale([1.5,1.5,1.5])

beachradio = viz.addChild('beachradio.osgb')
beachradio.setPosition([11.5,0.33,36.6])
beachradio.setEuler(0,0,0)
beachradio.setScale([1.5,1.5,1.5])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([13.5,0.23,36.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([13.5,0.23,33.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([13.5,0.23,30.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([13.5,0.23,27.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([12,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([9,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([6,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([3,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([0,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3,0.23,38.3])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3.6,0.23,26.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3.6,0.23,29.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3.6,0.23,32.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3.6,0.23,35.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

bollard = viz.addChild('bollard.osgb')
bollard.setPosition([-3.6,0.23,23.6])
bollard.setEuler(0,0,0)
bollard.setScale([0.8,1,0.8])

sofa1 = viz.addChild('sofa1.osgb')
sofa1.setPosition([17,0.23,32])
sofa1.setEuler(270,0,0)
sofa1.setScale([1,1.5,1])

sofa2 = viz.addChild('sofa2.osgb')
sofa2.setPosition([20.5,0.23,33])
sofa2.setEuler(90,0,0)
sofa2.setScale([1,1.5,1])

sofa3 = viz.addChild('sofa3.osgb')
sofa3.setPosition([17,0.23,33.3])
sofa3.setEuler(360,0,0)
sofa3.setScale([1,1.5,1])

gardenswing = viz.addChild('gardenswing.osgb')
gardenswing.setPosition([20.5,0.23,31])
gardenswing.setEuler(90,0,0)
gardenswing.setScale([1,1.5,1])

grill = viz.addChild('grill6.osgb')
grill.setPosition([9,0.33,36])
grill.setEuler(0,0,0)
grill.setScale([1,1,1])

swimring = viz.addChild('RiverRat.osgb')
swimring.setPosition([5,0.33,27])
swimring.setEuler(0,0,0)
swimring.setScale([1,1,1])

projector2 = viz.addChild('projector2.osgb')
projector2.setPosition([20.5,0.23,27])
projector2.setEuler(180,0,0)
projector2.setScale([0.02,0.02,0.02])

phone = viz.addChild('phone.osgb')
phone.setPosition([10.5,1.15,31.4])
phone.setEuler(90,360,0)
phone.setScale([0.05,0.05,0.05])


#===========================Set Grabber==============================
#Initialize the Grabber and items that can be grabbed
#Change hightlight mode from default outline to box
usingPhysics=False
from tools import grabber
from tools import highlighter
#----------------gymroom------------------
tool = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
tool.setItems([bottle])
tool1 = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
tool1.setItems([gymball,towel,kettlebell])
tool2 = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
tool2.setItems([dumbbell])
#--------------Living Room----------------
toolPillow = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolPillow.setItems([pillow])
toolTable = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolTable.setItems([book,teapot,teacup1,teacup2])
toolFlower = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolFlower.setItems([flower])
#--------------Bedroom----------------
toolbook = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolbook.setItems([books2])
toolcloth = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolcloth.setItems([bolsters,clothing,blanket])
toolbear = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolbear.setItems([bear])
#--------------Backyard----------------
toolswimmingpool = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolswimmingpool.setItems([swimring])
toolfloor = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolfloor.setItems([beachball,beachradio])
toolbackyardtable = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolbackyardtable.setItems([sunglasses])
toolduck = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlighter.MODE_BOX)
toolduck.setItems([rubberduck,rubberduck1,rubberduck2])


#-----------------------------------------
#Link the grabber to an arrow in order to
#visualize it's position
from vizconnect.util import virtual_trackers
mouseTracker = virtual_trackers.ScrollWheel(followMouse = True)
mouseTracker.distance = 1.4
arrow = vizshape.addArrow(length=0.2,color=viz.BLUE)
arrowLink = viz.link(mouseTracker,arrow)
arrowLink.postMultLinkable(viz.MainView)

#----------------gymroom------------------
viz.link(arrowLink,tool)
viz.link(arrowLink,tool1)
viz.link(arrowLink,tool2)

fall = vizact.fall(0.125)
fall1 = vizact.fall(0.22)
fall2 = vizact.fall(0)

def onRelease(tool):
    tool.released.runAction(fall)
        
def onRelease1(tool1):
        tool1.released.runAction(fall1)

def onRelease2(tool2):
        tool2.released.runAction(fall2)

def updateGrabber(tool):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onRelease)
tool.setUpdateFunction(updateGrabber)


def updateGrabber1(tool1):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool1.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onRelease1)
tool1.setUpdateFunction(updateGrabber1)

def updateGrabber2(tool2):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        tool2.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onRelease2)
tool2.setUpdateFunction(updateGrabber2)

#--------------Living Room----------------
viz.link(arrowLink,toolPillow)
viz.link(arrowLink,toolTable)
viz.link(arrowLink,toolFlower)

def updateGrabberPillow(toolPillow):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolPillow.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleasePillow)
toolPillow.setUpdateFunction(updateGrabberPillow)

def updateGrabberTable(toolTable):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolTable.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseTable)
toolTable.setUpdateFunction(updateGrabberTable)

def updateGrabberFlower(toolFlower):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolFlower.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseFlower)
toolFlower.setUpdateFunction(updateGrabberFlower)

def onReleasePillow(toolPillow):
    toolPillow.released.runAction(fallPillow)

def onReleaseTable(toolTable):
    toolTable.released.runAction(fallTable)

def onReleaseFlower(toolFlower):
    toolFlower.released.runAction(fallFlower)

fallPillow = vizact.fall(0.9)
fallTable = vizact.fall(0.58)
fallFlower = vizact.fall(0.77)
    
#--------------Bedroom----------------
fallbook = vizact.fall(4.05)
fallcloth = vizact.fall(4.04)
fallbear = vizact.fall(3.33)


viz.link(arrowLink,toolbook)
viz.link(arrowLink,toolcloth)
viz.link(arrowLink,toolbear)

def updateGrabberBook(toolbook):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolbook.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseBook)
toolbook.setUpdateFunction(updateGrabberBook)

def updateGrabberCloth(toolcloth):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolcloth.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseCloth)
toolcloth.setUpdateFunction(updateGrabberCloth)

def updateGrabberBear(toolbear):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolbear.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseBear)
toolbear.setUpdateFunction(updateGrabberBear)

def onReleaseBook(toolbook):
    toolbook.released.runAction(fallbook)

def onReleaseCloth(toolcloth):
    toolcloth.released.runAction(fallcloth)

def onReleaseBear(toolbear):
    toolbear.released.runAction(fallbear)
    
#--------------Backyard----------------
fallswimmingpool = vizact.fall(0.25)
fallfloor = vizact.fall(0.33)
fallbackyardtable = vizact.fall(1.15)
fallducke = vizact.fall(0.2)


viz.link(arrowLink,toolswimmingpool)
viz.link(arrowLink,toolfloor)
viz.link(arrowLink,toolbackyardtable)
viz.link(arrowLink,toolduck)

def updateGrabberSwimmingpool(toolswimmingpool):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolswimmingpool.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseSwimmingpool)
toolswimmingpool.setUpdateFunction(updateGrabberSwimmingpool)

def updateGrabberFloor(toolfloor):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolfloor.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseFloor)
toolfloor.setUpdateFunction(updateGrabberFloor)

def updateGrabberBackyardTable(toolbackyardtable):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolbackyardtable.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseBackyardTable)
toolbackyardtable.setUpdateFunction(updateGrabberBackyardTable)

def updateGrabberDuck(toolduck):
    state = viz.mouse.getState()
    if state & viz. MOUSEBUTTON_LEFT:
        toolduck.grabAndHold()
    viz.callback(grabber.RELEASE_EVENT,onReleaseDuck)
toolduck.setUpdateFunction(updateGrabberDuck)

def onReleaseSwimmingpool(toolswimmingpool):
    toolswimmingpool.released.runAction(fallswimmingpool)

def onReleaseFloor(toolfloor):
    toolfloor.released.runAction(fallfloor)

def onReleaseBackyardTable(toolbackyardtable):
    toolbackyardtable.released.runAction(fallbackyardtable)

def onReleaseDuck(toolduck):
    toolduck.released.runAction(fallduck)


#===========================Additional Elements==============================
#Set Menu(Additional elements)
#Setup color schemes for menu
defaultTheme = viz.getTheme()

#Set in colors for dark theme
darkTheme = viz.Theme()
darkTheme.borderColor = (0.1,0.1,0.1,1)
darkTheme.backColor = (0.4,0.4,0.4,1)
darkTheme.lightBackColor = (0.6,0.6,0.6,1)
darkTheme.darkBackColor = (0.2,0.2,0.2,1)
darkTheme.highBackColor = (0.2,0.2,0.2,1)

#Set in colors for green theme
greenTheme = viz.Theme()
greenTheme.borderColor = (0.1,0.2,0.05,1)
greenTheme.backColor = (0.5,0.7,0.3,1)
greenTheme.lightBackColor = (0.6,0.8,0.4,1)
greenTheme.darkBackColor = (0.2,0.4,0.1,1)
greenTheme.highBackColor = (0.2,0.4,0.1,1)
greenTheme.highTextColor = (0.95,0.88,0.33,1)

themes = ( defaultTheme, darkTheme, greenTheme )

#Create main menu object
import vizmenu
menu = vizmenu.add()
menu.setAlignment(vizmenu.CENTER)


#Create three menu subjects
AppearanceMenu = menu.add( 'Appearance' )
gymballMenu = menu.add( 'Gym Ball' )
benchMenu = menu.add( 'Bench' )

pillowMenu = menu.add( 'Pillow' )
lampMenu = menu.add( 'Lamp' )

cabinetMenu=menu.add('Cabinet')
blanketMenu=menu.add('Blanket')
curtainMenu=menu.add('Curtain')

projector2Menu=menu.add('Projector')
swimringMenu=menu.add('Swim Ring')
beachradioMenu=menu.add('Backyard Radio')

#Appearance Menu

#Add dropdown list of theme options to Appearance menu
themeDropDown = AppearanceMenu.add( viz.DROPLIST, 'Theme' )
themeDropDown.addItems( ['Default','Dark','Green'] )

def onTheme( e ):
    #Change menu theme when new item in drop-down list is selected
    viz.setTheme( themes[e.newSel] )

#Call onTheme when themeDropDown is changed
vizact.onlist( themeDropDown, onTheme )

#Create a number of sub-menus with labels
fooMenu = AppearanceMenu.add( vizmenu.MENU, 'foo' )
barMenu = fooMenu.add( vizmenu.MENU, 'bar' )

#Add textbox to sub-sub-menu
messageBox = barMenu.add( viz.TEXTBOX, 'Textbox' )

#Add object to display what is in the textbox
onScreenText = viz.addText( '', viz.SCREEN )

def textChanged(e):
    #The GUI textbox e.object has been modified
    #e.newText is the new text
    #e.oldText is the previous text
    #e.key is the key that has just been pressed
    onScreenText.message( e.newText )

vizact.ontextbox(messageBox, textChanged)

#----------------gymroom-------------------
#Gym ball menu

#Create sub-menu to house ball color radio buttons
gymballcolorMenu = gymballMenu.add( vizmenu.MENU, 'Color' )

#Add ball color modifying radio buttons
gymballYellow = gymballMenu.add( viz.RADIO, 0, 'Yellow' )
gymballGreen = gymballMenu.add( viz.RADIO, 0, 'Green' )
gymballBlue = gymballMenu.add( viz.RADIO, 0, 'Blue' )

#Set inital selected radio button
gymballBlue.set( viz.DOWN )

#Set callbacks for changing ball color
vizact.onbuttondown( gymballYellow, gymball.color, viz.YELLOW )
vizact.onbuttondown( gymballGreen, gymball.color, viz.GREEN )
vizact.onbuttondown( gymballBlue, gymball.color, viz.BLUE )


#Bench menu

#Create sub-menu to house bench color radio buttons
benchcolorMenu = benchMenu.add( vizmenu.MENU, 'Color' )

#Add ball color modifying radio buttons
benchBlue = benchMenu.add( viz.RADIO, 0, 'Blue' )
benchWhite = benchMenu.add( viz.RADIO, 0, 'White' )
benchYellow = benchMenu.add( viz.RADIO, 0, 'Yellow' )

#Set inital selected radio button
benchWhite.set( viz.DOWN )

#Set callbacks for changing ball color
vizact.onbuttondown( benchBlue, bench.color, viz.BLUE )
vizact.onbuttondown( benchWhite, bench.color, viz.WHITE )
vizact.onbuttondown( benchYellow, bench.color, viz.YELLOW )

#--------------Living Room----------------
#Pilow Menu

#Create sub-menu to house pillow color radio buttons
PllowColorMenu = pillowMenu.add( vizmenu.MENU, 'Color' )

#Add pillow color modifying radio buttons
pillowRed = PllowColorMenu.add( viz.RADIO, 0, 'Red' )
pillowBlue = PllowColorMenu.add( viz.RADIO, 0, 'Blue' )
pillowBlack = PllowColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
pillowBlack.set( viz.DOWN )

#Set callbacks for changing ball color
vizact.onbuttondown( pillowRed, pillow.color, viz.RED )
vizact.onbuttondown( pillowBlue, pillow.color, viz.BLUE )
vizact.onbuttondown( pillowBlack, pillow.color, viz.BLACK )

#Lamp Menu

#Create sub-menu to house pillow color radio buttons
LampColorMenu = lampMenu.add( vizmenu.MENU, 'Color' )

#Add pillow color modifying radio buttons
lampRed = LampColorMenu.add( viz.RADIO, 0, 'Red' )
lampBlue = LampColorMenu.add( viz.RADIO, 0, 'Blue' )
lampBlack = LampColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
lampBlack.set( viz.DOWN )

#Set callbacks for changing ball color
vizact.onbuttondown( lampRed, lamp.color, viz.RED )
vizact.onbuttondown( lampBlue, lamp.color, viz.BLUE )
vizact.onbuttondown( lampBlack, lamp.color, viz.BLACK )

#--------------Bedroom----------------
#Cabinet Menu

#Create sub-menu to bedroom cabinet color radio buttons
cabinetColorMenu = cabinetMenu.add( vizmenu.MENU, 'Color' )

#Add cabinet color modifying radio buttons
cabinetRed = cabinetColorMenu.add( viz.RADIO, 0, 'Orange Red' )
cabinetPurple = cabinetColorMenu.add( viz.RADIO, 0, 'Purple' )
cabinetBlack = cabinetColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
cabinetBlack.set( viz.DOWN )

#Set callbacks for changing cabinet color
vizact.onbuttondown( cabinetRed, cabinet.color, viz.ORANGE_RED )
vizact.onbuttondown( cabinetPurple, cabinet.color, viz.PURPLE )
vizact.onbuttondown( cabinetBlack, cabinet.color, viz.BLACK )

#Curtain Menu

#Create sub-menu to bedroom curtain color radio buttons
curtainColorMenu = curtainMenu.add( vizmenu.MENU, 'Color' )

#Add curtain color modifying radio buttons
curtainGrey = curtainColorMenu.add( viz.RADIO, 0, 'Grey' )
curtainWhite = curtainColorMenu.add( viz.RADIO, 0, 'White' )
curtainBlack = curtainColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
curtainBlack.set( viz.DOWN )

#Set callbacks for changing curtain color
vizact.onbuttondown( curtainGrey, curtain.color, viz.GRAY )
vizact.onbuttondown( curtainWhite, curtain.color, viz.WHITE )
vizact.onbuttondown( curtainBlack, curtain.color, viz.BLACK )

#Blanket Menu

#Create sub-menu to bedroom blanket color radio buttons
blanketColorMenu = blanketMenu.add( vizmenu.MENU, 'Color' )

#Add cabinet color modifying radio buttons
blanketGreen = blanketColorMenu.add( viz.RADIO, 0, 'Green' )
blanketWhite = blanketColorMenu.add( viz.RADIO, 0, 'White' )
blanketBlack = blanketColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
blanketBlack.set( viz.DOWN )

#Set callbacks for changing cabinet color
vizact.onbuttondown( blanketGreen, blanket.color, viz.GREEN )
vizact.onbuttondown( blanketWhite, blanket.color, viz.WHITE )
vizact.onbuttondown( blanketBlack, blanket.color, viz.BLACK )

#--------------Backyard----------------
#Projector Menu

#Create sub-menu to backyard projector color radio buttons
projector2ColorMenu = projector2Menu.add( vizmenu.MENU, 'Color' )

#Add projector color modifying radio buttons
projector2Red = projector2ColorMenu.add( viz.RADIO, 0, 'Red' )
projector2Blue = projector2ColorMenu.add( viz.RADIO, 0, 'Blue' )
projector2Black = projector2ColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
projector2Blue.set( viz.DOWN )

#Set callbacks for changing projector color
vizact.onbuttondown( projector2Red, projector2.color, viz.RED )
vizact.onbuttondown( projector2Blue, projector2.color, viz.BLUE )
vizact.onbuttondown( projector2Black, projector2.color, viz.BLACK )

#swimring Menu

#Create sub-menu to backyard swimring color radio buttons
swimringColorMenu = swimringMenu.add( vizmenu.MENU, 'Color' )

#Add swing color modifying radio buttons
swimringRed = swimringColorMenu.add( viz.RADIO, 0, 'Red' )
swimringBlue = swimringColorMenu.add( viz.RADIO, 0, 'Blue' )
swimringYellow = swimringColorMenu.add( viz.RADIO, 0, 'Yellow' )

#Set inital selected radio button
swimringBlue.set( viz.DOWN )

#Set callbacks for changing swimring color
vizact.onbuttondown( swimringRed, swimring.color, viz.RED )
vizact.onbuttondown( swimringBlue, swimring.color, viz.BLUE )
vizact.onbuttondown( swimringYellow, swimring.color, viz.YELLOW )

#radio Menu

#Create sub-menu to backyard radio color radio buttons
beachradioColorMenu = beachradioMenu.add( vizmenu.MENU, 'Color' )

#Add radio color modifying radio buttons
beachradioRed = beachradioColorMenu.add( viz.RADIO, 0, 'Red' )
beachradioBlue = beachradioColorMenu.add( viz.RADIO, 0, 'Blue' )
beachradioBlack = beachradioColorMenu.add( viz.RADIO, 0, 'Black' )

#Set inital selected radio button
beachradioRed.set( viz.DOWN )

#Set callbacks for changing radio color
vizact.onbuttondown( beachradioRed, beachradio.color, viz.RED )
vizact.onbuttondown( beachradioBlue, beachradio.color, viz.BLUE )
vizact.onbuttondown( beachradioBlack, beachradio.color, viz.BLACK )





#----------------gymroom-------------------
#Set image TV(Additional elements)
tv = viz.addChild('tv.osgb')
tv.setPosition([23, 1.8, 21.6])
tv.setEuler(-90,0,0)

gymrule = viz.addTexture('gymrule.jpg')

rule = vizshape.addPlane(size=(1.0,0.7),
        axis=vizshape.AXIS_Y,
        cullFace=False)

rule.setPosition([22.7, 2.25, 22.3])
rule.setEuler(0,270,90)

#gymrule = viz.addVideo('gymrule.avi')
rule.texture(gymrule)
#gymrule.setFrame(1)
#gymrule.play()

#Set image Poster(Additional elements)
frame = viz.addChild('frame.osgb')
frame.setPosition([16.75, 2.2, 21.15])
frame.setEuler(-90,0,0)
frame.setScale([1.5, 1.5, 1.5])

poster = viz.addTexture('poster.jpg')

posterpanel = vizshape.addPlane(size=(0.81,0.45),
        axis=vizshape.AXIS_Y,
        cullFace=False)

posterpanel.setPosition([16.739, 2.5, 21.66])
posterpanel.setEuler(0,270,270)

#poster = viz.addVideo('poster.avi')
posterpanel.texture(poster)
#poster.setFrame(1)
#poster.play()

#--------------Living Room----------------
#Additional Elements - Video at laptop
movie_screen = vizshape.addPlane(size=(0.32,0.18),
        axis=vizshape.AXIS_Y,
        cullFace=True)
movie_screen.setPosition([7.79,1.445,20.11])
movie_screen.setEuler(90,293,0)

movie = viz.addVideo( 'mrbean.avi' )
movie_screen.texture(movie)
movie.setFrame(2.5)
movie.play()
movie.loop() 

#Additional Elements - Canvas Art on the wall
canvas = vizshape.addPlane(size=(0.5,0.65),
        axis=vizshape.AXIS_Y,
        cullFace=True)
canvas.setPosition([9,2,16.9])
canvas.setEuler(90,270,0)

canvaspic = viz.addTexture('canvaspic.jpg')
canvas.texture(canvaspic)

#--------------Bedroom----------------
#Additional Elements - Video at iPad
ballet_size = vizshape.addPlane(size=(0.5,0.5),
        axis=vizshape.AXIS_Y,
        cullFace=True)
ballet_size.setPosition([11.77,4.048,15.68])
ballet_size.setEuler(0,0,0)
ballet_size.setScale([0.67,0,0.54])

ballet = viz.addVideo('ballet.avi')
ballet_size.texture(ballet)
ballet.setFrame(2.5)
ballet.play()
ballet.loop() 

#Additional Elements - Painting on the wall
paint = vizshape.addPlane(size=(1,1),
        axis=vizshape.AXIS_Y,
        cullFace=True)
paint.setPosition([14.6,5.2,13.2])
paint.setEuler(90,270,0)

paintpic = viz.addTexture('painting.jpg')
paint.texture(paintpic)

#--------------Backyard----------------
#Additional Elements - Picture on the table
picture = vizshape.addPlane(size=(0.8,0.8),
        axis=vizshape.AXIS_Y,
        cullFace=True)
picture.setPosition([11,1.15,33])
picture.setEuler(90,360,0)

picturepic = viz.addTexture('beach.jpg')
picture.texture(picturepic)

#Additional Elements - Video at phone
phone_screen= vizshape.addPlane(size=(0.14,0.24),
        axis=vizshape.AXIS_Y,
        cullFace=True)
phone_screen.setPosition([10.5,1.172,31.4])
phone_screen.setEuler(90,360,0)

phone = viz.addVideo( 'movie.avi' )
phone_screen.texture(phone)
phone.setFrame(2.5)
phone.play()
phone.loop()



#===========================Additional Elements==============================
#----------------gymroom-------------------
#Set avatar and action(Event and Interaction)
gymavatar = viz.addAvatar('vcc_female.cfg')
gymavatar.setPosition([19.5, 0.234, 22])
gymavatar.state(1)

def sheDances():
    gymavatar.state(5)

def stopDances():
    gymavatar.state(1)

#This keypress will call the function sheDances
vizact.onkeydown('1', sheDances)
vizact.onkeydown('2', stopDances)


#Set video and action(Event and Interaction)
screen = viz.addChild('screen.osgb')
screen.setPosition([19, 1, 25])
screen.setEuler(90,0,0)

picwhite = viz.addTexture('white.png')

panel = vizshape.addPlane(size=(2.5,1.75),
        axis=vizshape.AXIS_Y,
        cullFace=True)

panel.setPosition([20.5, 2.0, 24.85])
panel.setEuler(0,270,0)

workout1 = viz.addVideo( 'workout1.avi' )
workout1.volume(.5)
workout1.loop(viz.ON) 
workout2 = viz.addVideo( 'workout2.avi' )
workout2.volume(.5)
workout2.loop(viz.ON) 

def playGymVideo1():
    
    workout2.stop()
    panel.texture(workout1)
    workout1.setFrame(2.5)
    workout1.play()
    
def playGymVideo2():
    
    workout1.stop()
    panel.texture(workout2)
    workout2.setFrame(2.5)
    workout2.play()
    
def stopGymVideo():
    workout1.stop()
    workout2.stop()
    panel.texture(picwhite)
    
vizact.onkeydown('6', playGymVideo1)
vizact.onkeydown('7', playGymVideo2)
vizact.onkeydown('8', stopGymVideo)

#Set music and event (Event and Interaction)
gymmusic1 = viz.addAudio('music1.wav')
gymmusic1.loop(viz.ON) 
gymmusic1.volume(.5)

gymmusic2 = viz.addAudio('music2.wav')
gymmusic2.loop(viz.ON) 
gymmusic2.volume(.5)

def playMusic1():
    gymmusic2.stop()
    gymmusic1.play()
    
def playMusic2():
    gymmusic1.stop()
    gymmusic2.play()

def stopMusic():
    gymmusic1.stop()
    gymmusic2.stop()

vizact.onkeydown('3', playMusic1)
vizact.onkeydown('4', playMusic2)
vizact.onkeydown('5', stopMusic)

#--------------Living Room----------------
#Events and Interaction (1)
fireplace_screen = vizshape.addPlane(size=(1.25,1.25),
        axis=vizshape.AXIS_Y,
        cullFace=True)
fireplace_screen.setPosition([5.5,1,17.2])
fireplace_screen.setEuler(0,270,0)

fireplace = viz.addVideo( 'fireplace.avi' )
fireplace_screen.texture(fireplace)
fireplace.setFrame(2.5)

def playFireplace():
        fireplace.play()
        fireplace.loop(viz.ON)  
def stopFireplace():
        fireplace.stop()

vizact.onkeydown('f', playFireplace)
vizact.onkeydown('g', stopFireplace)

#Events and Interaction (2)
tv_screen = vizshape.addPlane(size=(1.35,0.65),
        axis=vizshape.AXIS_Y,
        cullFace=True)
tv_screen.setPosition([5.35,1.2,17.8])
tv_screen.setEuler(180,270,0)

showhouseVid = viz.addVideo( 'showhouse.avi' )
tv_screen.texture(showhouseVid)

def playShowhouseVid():
        showhouseVid.play()
def stopShowhouseVid():
        showhouseVid.stop()

vizact.onkeydown('s', playShowhouseVid)
vizact.onkeydown('d', stopShowhouseVid)


#Events and Interaction (3) (4)
song1 = viz.addAudio('comethru.wav')
song2 = viz.addAudio('light switch.wav')

def playSong1():
        song2.stop()
        song1.play()
        song1.loop(viz.ON)
def playSong2():
        song1.stop()
        song2.play()
        song2.loop(viz.ON)
def stopSong():
        song1.stop()
        song2.stop()

vizact.onkeydown('c', playSong1)
vizact.onkeydown('l', playSong2)
vizact.onkeydown('w', stopSong)

#Events and Interaction (5)
livingrAvatar1 = viz.addAvatar('vcc_female.cfg')
livingrAvatar1.setPosition([4.33,0.35,20])
livingrAvatar1.setEuler([-50,0,0])
livingrAvatar1.state(1)

livingrAvatar2 = viz.addAvatar('vcc_male.cfg')
livingrAvatar2.setPosition([3.5,0.35,20.5])
livingrAvatar2.setEuler([140,0,0])
livingrAvatar2.state(1)

def avatarTalking():
        livingrAvatar1.state(14)
        livingrAvatar2.state(14)
def avatarIdle():
        livingrAvatar1.state(1)
        livingrAvatar2.state(1)

vizact.onkeydown('t', avatarTalking)
vizact.onkeydown('y', avatarIdle)


#--------------Bedroom----------------
#Events and Interaction (1)(2)

picwhite3 = viz.addTexture('white.png')
panel3 = vizshape.addPlane(size=(0.33,0.19),
        axis=vizshape.AXIS_Y,
        cullFace=True)
panel3.setPosition([12.195,4.17,15.78])
panel3.setEuler(0,293,0)


roomVideo1 = viz.addVideo( 'bedroom1.avi' )
roomVideo1.volume(.5)
roomVideo1.loop(viz.ON) 
roomVideo2 = viz.addVideo( 'bedroom2.avi' )
roomVideo2.volume(.5)
roomVideo2.loop(viz.ON) 


def playRoomVideo1():
    
    roomVideo2.stop()
    panel3.texture(roomVideo1)
    roomVideo1.setFrame(1)
    roomVideo1.play()
    
def playRoomVideo2():
    roomVideo1.stop()
    panel3.texture(roomVideo2)
    roomVideo2.setFrame(1)
    roomVideo2.play()
    
def stopRoomVideo():
    roomVideo1.stop()
    roomVideo2.stop()
    panel3.texture(picwhite3)
    
vizact.onkeydown('i', playRoomVideo1)
vizact.onkeydown('o', playRoomVideo2)
vizact.onkeydown('p', stopRoomVideo)



#Events and Interaction (3) (4)
bedroomSong1= viz.addAudio('monsters.wav')
bedroomSong2 = viz.addAudio('love is gone.wav')

def runBedroomSong1():
        bedroomSong2.stop()
        bedroomSong1.play()
        bedroomSong1.loop(viz.ON)
def runBedroomSong2():
        bedroomSong1.stop()
        bedroomSong2.play()
        bedroomSong2.loop(viz.ON)
def stopBedroomSong():
        bedroomSong1.stop()
        bedroomSong2.stop()

vizact.onkeydown('z', runBedroomSong1)
vizact.onkeydown('x', runBedroomSong2)
vizact.onkeydown('v', stopBedroomSong)


#Events and Interaction (5)
bedroomAvatar1 = viz.addAvatar('vcc_female.cfg')
bedroomAvatar1.setPosition([11.5,3.33,13.7])
bedroomAvatar1.setEuler([-50,0,0])
bedroomAvatar1.state(1)


def bedroomLook():
        bedroomAvatar1.state(9)
def bedroomStop():
        bedroomAvatar1.state(1)

vizact.onkeydown('n', bedroomLook)
vizact.onkeydown('m', bedroomStop)

#--------------Backyard----------------
#Events and Interaction (1)(2)

backyardsong1= viz.addAudio('hilarious.wav',loop=2)
backyardsong2= viz.addAudio('dandelion.wav')

def runBackyardSong1():
        backyardsong2.stop()
        backyardsong1.play()
        backyardsong1.loop(viz.ON)
def runBeackyardSong2():
        backyardsong1.stop()
        backyardsong2.play()
        backyardsong2.loop(viz.ON)
def stopBackyardSong():
        backyardsong1.stop()
        backyardsong2.stop()

vizact.onkeydown('h', runBackyardSong1)
vizact.onkeydown('d', runBeackyardSong2)
vizact.onkeydown('a',  stopBackyardSong)

#Events and Interaction (3)
avatar = viz.addAvatar('vcc_female.cfg')
avatar.setPosition([18.3,0.82,34.4])
avatar.setEuler([-90,0,0])
avatar.state(8)

avatar1 = viz.addAvatar('vcc_male.cfg')
avatar1.setPosition([20.3,0.23,32.1])
avatar1.setEuler([-90,0,0])
look_left = vizact.headto(-60,0,0)
avatar1.addAction(look_left)

def avatar1cheer():
        avatar1.state(3)
        avatar1.setPosition([20.3,0.23,32])
        avatar1.setEuler([-90,0,0])
        
def avatar1Stop():
        avatar1.setPosition([20.3,0.23,32])
        avatar1.setEuler([-90,0,0])
        look_left = vizact.headto(-60,0,0)
        avatar1.addAction(look_left)

vizact.onkeydown('b', avatar1cheer)
vizact.onkeydown('e', avatar1Stop)


#Events and Interaction (4)(5)

screen = viz.addTexture('white.png')
screenprojector = vizshape.addPlane(size=(3.1,1.85),
        axis=vizshape.AXIS_Y,
        cullFace=True)
screenprojector.setPosition(([18.95,1.5,27.15]))
screenprojector.setEuler(180,270,0)


projectorvideo1 = viz.addVideo( 'footballcompetition.avi' )
projectorvideo1.volume(.8)
projectorvideo1.loop(viz.ON) 
projectorvideo2 = viz.addVideo( 'basketball.avi' )
projectorvideo2.volume(.8)
projectorvideo2.loop(viz.ON) 


def playBackyardVideo1():
    
    projectorvideo2.stop()
    screenprojector.texture(projectorvideo1)
    projectorvideo1.setFrame(1)
    projectorvideo1.play()
    
def playBackyardVideo2():
    projectorvideo1.stop()
    screenprojector.texture(projectorvideo2)
    projectorvideo2.setFrame(1)
    projectorvideo2.play()
    
def stopBackyardVideo():
    projectorvideo1.stop()
    projectorvideo2.stop()
    screenprojector.texture(screen)
    
vizact.onkeydown('j', playBackyardVideo1)
vizact.onkeydown('k', playBackyardVideo2)
vizact.onkeydown('m', stopBackyardVideo)

