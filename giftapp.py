import kivy
import webbrowser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Rectangle,Color,Canvas
from kivy.animation import Animation
from kivy.core.text import LabelBase

LabelBase.register(name="alex",fn_regular="AlexBrush-Regular.ttf")
LabelBase.register(name="great",fn_regular="GreatVibes-Regular.otf")
LabelBase.register(name="jack",fn_regular="blackjack.otf")
LabelBase.register(name="lob",fn_regular="Lobster_1.3.otf")
LabelBase.register(name="paci",fn_regular="Pacifico.ttf")
LabelBase.register(name="quick",fn_regular="Quicksand-Regular.otf")

class MainWindow(Screen):
    def next(self):
        sm.current="second"

class SecondWindow(Screen):
    def back(self):
        sm.current="main"
    def birth(self):
        sm.current="birth"
    def wed(self):
        sm.current="wed"
    def anni(self):
        sm.current="anni"

class BirthWindow(Screen):
    def ocas(self):
        sm.current="second"

    def b15(self):
        sm.current="b1-5"

    def b510(self):
        sm.current="b5-10"

    def b1015(self):
        sm.current="b10-15"

    def b1620(self):
        sm.current="b16-20"

    def b2040(self):
        sm.current="b20-40"
    
    def b4060(self):
        sm.current="b40-60"

    def b60(self):
        sm.current="b60+"


class b10to15Window(Screen):
    def findschoolkit(self):
        webbrowser.open('https://www.amazon.in/s?k=school+kit&ref=nb_sb_noss_1')

    def findschoolbag(self):
        webbrowser.open('https://www.amazon.in/s?k=school+bag&ref=nb_sb_noss_1')

    def findwaterbottle(self):
        webbrowser.open('https://www.amazon.in/s?k=water+bottle&ref=nb_sb_noss_2')

    def findrccar(self):
        webbrowser.open('https://www.amazon.in/s?k=rc+car&ref=nb_sb_noss_2')

    def backto(self):
        sm.current="birth"

class b1to5Window(Screen):
    def findteddy(self):
        webbrowser.open('https://www.amazon.in/Stuffed-Animals-Teddy-Bear-Soft-Toys/s?rh=n%3A1378446031%2Cp_lbr_characters_browse-bin%3ATeddy+Bear')

    def findtoycycle(self):
        webbrowser.open('https://www.amazon.in/s?k=toy+cycle&ref=nb_sb_noss_2')

    def finddoll(self):
        webbrowser.open('https://www.amazon.in/s?k=doll&ref=nb_sb_noss')

    def findbooks(self):
        webbrowser.open('https://www.amazon.in/s?k=story+books+for+5+year+old+children&ref=nb_sb_noss_1')

    def backto(self):
        sm.current="birth"

class b5to10Window(Screen):
    def findtricycle(self):
        webbrowser.open('https://www.amazon.in/s?k=tricycle&ref=nb_sb_noss_1')

    def findcolorbook(self):
        webbrowser.open('https://www.amazon.in/s?k=color+book&ref=nb_sb_noss_2')

    def findwaterbottle(self):
        webbrowser.open('https://www.amazon.in/s?k=water+bottle&crid=2WRJDYRE2UN7Y&sprefix=water%2Caps%2C324&ref=nb_sb_ss_i_1_5')

    def findbooks(self):
        webbrowser.open('https://www.amazon.in/s?k=story+books+for+10+year+old+children&crid=2FWSFIUXC8R36&sprefix=story+%2Caps%2C349&ref=nb_sb_ss_i_3_6')

    def backto(self):
        sm.current="birth"

class b16to20Window(Screen):
    def findsunglass(self):
        webbrowser.open('https://www.amazon.in/s?k=sun+glasses&ref=nb_sb_noss_2')

    def findphonecase(self):
        webbrowser.open('https://www.amazon.in/s?k=phone+case&ref=nb_sb_noss_2')

    def findshoes(self):
        webbrowser.open('https://www.amazon.in/s?k=shoes&ref=nb_sb_noss_2')

    def findrccar(self):
        webbrowser.open('https://www.amazon.in/s?k=rc+car&ref=nb_sb_noss_2')

    def backto(self):
        sm.current="birth"

class b20to40Window(Screen):
    def findsunglass(self):
        webbrowser.open('https://www.amazon.in/s?k=sun+glasses&ref=nb_sb_noss_2')

    def findwatch(self):
        webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=watch')

    def findjacket(self):
        webbrowser.open('https://www.amazon.in/s?i=aps&k=leather%20jacket%20&ref=nb_sb_noss&url=search-alias%3Daps')

    def findtravel(self):
        webbrowser.open('https://www.amazon.in/s?k=travel+kit&ref=nb_sb_noss')

    def findheadphones(self):
        webbrowser.open('https://www.amazon.in/s?field-keywords=headphones&i=aps&ref=nb_sb_noss&url=search-alias%3Daps')

    def backto(self):
        sm.current="birth"

class b40to60Window(Screen):
    def findshaving(self):
        webbrowser.open('https://www.amazon.in/s?i=aps&k=shaving%20kit&ref=nb_sb_noss&url=search-alias%3Daps')

    def findspeaker(self):
        webbrowser.open('https://www.amazon.in/s?k=phone+case&ref=nb_sb_noss_2')

    def findshoes(self):
        webbrowser.open('https://www.amazon.in/s?k=shoes&ref=nb_sb_noss_2')

    def findsmart(self):
        webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=smart+watch')

    def backto(self):
        sm.current="birth"

class b20to40Window(Screen):
    def findsunglass(self):
        webbrowser.open('https://www.amazon.in/s?k=sun+glasses&ref=nb_sb_noss_2')

    def findwatch(self):
        webbrowser.open('https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=watch')

    def findjacket(self):
        webbrowser.open('https://www.amazon.in/s?i=aps&k=leather%20jacket%20&ref=nb_sb_noss&url=search-alias%3Daps')

    def findtravel(self):
        webbrowser.open('https://www.amazon.in/s?k=travel+kit&ref=nb_sb_noss')

    def findheadphones(self):
        webbrowser.open('https://www.amazon.in/s?field-keywords=headphones&i=aps&ref=nb_sb_noss&url=search-alias%3Daps')

    def backto(self):
        sm.current="birth"

class b60toaboveWindow(Screen):
    def findshaving(self):
        webbrowser.open('https://www.amazon.in/s?i=aps&k=shaving%20kit&ref=nb_sb_noss&url=search-alias%3Daps')

    def findspeaker(self):
        webbrowser.open('https://www.amazon.in/s?k=home+speaker&sprefix=home+spea&ref=nb_sb_ss_i_1_9 ')

    def findrocking(self):
        webbrowser.open('https://www.amazon.in/s?k=rocking+chair+for+adults+for+home&sprefix=rocking+&ref=nb_sb_ss_i_1_8')

    def findsupport(self):
        webbrowser.open('https://www.amazon.in/s?k=support+stick+for+old+people&sprefix=support+&ref=nb_sb_ss_i_1_8 ')

    def backto(self):
        sm.current="birth"


class AnniversaryWindow(Screen):
    def ocas(self):
        sm.current="second"
    def wood(self):
        sm.current="wood"

    def tin(self):
        sm.current="tin"

    def crys(self):
        sm.current="crys"

class an1to10(Screen):
    def findphoto(self):
        webbrowser.open('https://www.amazon.in/s?k=clock+with+photo&sprefix=clock+wi&ref=nb_sb_ss_i_2_8')

    def findframe(self):
        webbrowser.open('https://www.amazon.in/s?k=photo+frames+for+wall&sprefix=phot&ref=nb_sb_ss_i_1_4')

    def findchoc(self):
        webbrowser.open('https://www.amazon.in/s?k=choclates&ref=nb_sb_noss')

    def backto(self):
        sm.current="anni"
class an10to30(Screen):
    def findshirt(self):
        webbrowser.open('https://www.amazon.in/s?k=couple+tshirts+for+lovers&sprefix=couple+tshi&ref=nb_sb_ss_i_4_11')

    def findcard(self):
        webbrowser.open('https://www.amazon.in/s?k=anniversary+card+for+couple&sprefix=anniversary+car&ref=nb_sb_ss_i_5_15')

    def findshow(self):
        webbrowser.open('https://www.amazon.in/s?k=showpiece+for+couple+anniversary&sprefix=showp&ref=nb_sb_ss_i_2_5')

    def backto(self):
        sm.current="anni"

class an30toabove(Screen):
    def findframe(self):
        webbrowser.open('https://www.amazon.in/s?k=photo+frames+for+wall&sprefix=phot&ref=nb_sb_ss_i_1_4')

    def findcard(self):
        webbrowser.open('https://www.amazon.in/s?k=anniversary+card+for+couple&sprefix=anniversary+car&ref=nb_sb_ss_i_5_15')

    def findshow(self):
        webbrowser.open('https://www.amazon.in/s?k=showpiece+for+couple+anniversary&sprefix=showp&ref=nb_sb_ss_i_2_5')

    def backto(self):
        sm.current="anni"

class WedingWindow(Screen):
    def findsmaspe(self):
        webbrowser.open('https://www.amazon.in/s?k=smart+speakers&sprefix=smart+spea&ref=nb_sb_ss_i_1_10')
    
    def findframe(self):
        webbrowser.open('https://www.amazon.in/s?k=photo+frames+for+wall&sprefix=phot&ref=nb_sb_ss_i_1_4')

    def findshow(self):
        webbrowser.open('https://www.amazon.in/s?k=showpiece+for+couple+anniversary&sprefix=showp&ref=nb_sb_ss_i_2_5')

    def findknife(self):
        webbrowser.open('https://www.amazon.in/s?k=knife+set&sprefix=knife+&ref=nb_sb_ss_i_1_6')

    def findclock(self):
        webbrowser.open('https://www.amazon.in/s?k=clock&ref=nb_sb_noss')

    def findcouwatch(self):
        webbrowser.open('https://www.amazon.in/s?k=couple+watches+set+for+wedding&sprefix=couple+&ref=nb_sb_ss_i_1_7')

    def findchain(self):
        webbrowser.open('https://www.amazon.in/s?k=matching+chains&ref=nb_sb_noss')

    def findsheet(self):
        webbrowser.open('https://www.amazon.in/s?k=bed+sheet&ref=nb_sb_noss')

    def backto(self):
        sm.current="second"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("gisd.kv")
sm = WindowManager()

screens = [MainWindow(name="main"), SecondWindow(name="second"),BirthWindow(name="birth"),WedingWindow(name="wed"),AnniversaryWindow(name="anni"),b1to5Window(name="b1-5"),b5to10Window(name="b5-10"),b10to15Window(name="b10-15"),b16to20Window(name="b16-20"),b20to40Window(name="b20-40"),b40to60Window(name="b40-60"),b60toaboveWindow(name="b60+"),an10to30(name="wood"),an1to10(name="tin"),an30toabove(name="crys")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"
class giftApp(App):
    def build(self):
        return sm


if __name__=="__main__":
    giftApp().run()