from manimlib.imports import *
from yamanilib.ArduinoUno import *
from yamanilib.ResistorCreature import *

scolor="#e4b143"
tcolor="#b4bc61"
ecolor="#7abfc7"
mcolor="#ca709a"
acolor="#62b57e"
class Steamword(Scene):
    def construct(self):
        stemmatrix=SVGMobject("drawingsteam1",height=6)
        steam=VGroup()
        steam.add(stemmatrix.submobjects[0])
        steam.add(stemmatrix.submobjects[1])
        steam.add(stemmatrix.submobjects[2])
        steam.add(stemmatrix.submobjects[3])
        steam.add(stemmatrix.submobjects[4])

        steam.submobjects[0].set_fill(scolor)
        steam.submobjects[1].set_fill(tcolor)
        steam.submobjects[2].set_fill(ecolor)
        steam.submobjects[3].set_fill(mcolor)
        steam.submobjects[4].set_fill(acolor)


        since=VGroup()
        for loop1 in range(5, 11):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            since.add(stemmatrix.submobjects[loop1])
        since.set_fill(scolor)

        tech=VGroup()
        for loop2 in range(11, 20):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            tech.add(stemmatrix.submobjects[loop2])
        tech.set_fill(tcolor)

        eng=VGroup()
        for loop3 in range(20, 30):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            eng.add(stemmatrix.submobjects[loop3])
        eng.set_fill(ecolor)

        art=VGroup()
        for loop4 in range(30, 32):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            art.add(stemmatrix.submobjects[loop4])
        art.set_fill(acolor)

        math=VGroup()
        for loop5 in range(32, 35):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            math.add(stemmatrix.submobjects[loop5])
        math.set_fill(mcolor)

        bigsteam=steam.copy()
        bigsteam.set_height(2)
        bigsteam.move_to([0,0,0])


        stema=steam.copy()

        stema.submobjects[4].next_to(stema.submobjects[2],RIGHT)
        stema.submobjects[3].next_to(stema.submobjects[4],RIGHT)

        cenra=VGroup()
        cenra.add(stemmatrix.submobjects[5])
        cenra.add(stemmatrix.submobjects[11])
        cenra.add(stemmatrix.submobjects[20])

        cenra.add(stemmatrix.submobjects[31])
        cenra.add(stemmatrix.submobjects[11].copy())
        cenra.add(stemmatrix.submobjects[30])


        center_word=cenra.copy()


        center_word.submobjects[3].next_to(center_word.submobjects[2],RIGHT)
        center_word.submobjects[4].next_to(center_word.submobjects[3],RIGHT)
        center_word.submobjects[5].next_to(center_word.submobjects[4],RIGHT)
        center_word.submobjects[3].shift(UP*.02)

        random_letters=VGroup()

        for loop6 in range(6, 11):
            random_letters.add(stemmatrix.submobjects[loop6])

        for loop7 in range(12, 20):
            random_letters.add(stemmatrix.submobjects[loop7])

        for loop8 in range(21, 30):
            random_letters.add(stemmatrix.submobjects[loop8])


        for loop10 in range(33, 35):
            random_letters.add(stemmatrix.submobjects[loop10])



        self.play(Write(bigsteam))

        self.play(ReplacementTransform(bigsteam,steam))
        self.play(Write(since))
        self.play(Write(tech),since.fade,.5)
        self.play(Write(eng),tech.fade,.5)
        self.play(Write(art),eng.fade,.5)
        self.play(Write(math),art.fade,.5)



        #self.play(Write(stema))


        self.play(ReplacementTransform(steam,stema),ReplacementTransform(cenra,center_word),FadeOut(stemmatrix.submobjects[32]),VFadeOut(random_letters))
        #self.play(Indicate(cenra))

        #self.play()
        #self.play()
        self.play(stema.shift,LEFT*2,center_word.next_to,stema.get_center(),RIGHT,.1)

class LED(SVGMobject):
    CONFIG = {
        "file_name": "LEDSVG",
        "height": 1,
        "stroke_color": WHITE,
        "stroke_width": 0,
        "fill_color": WHITE,
        "fill_opacity": 1,
    }
    def init_colors(self):
        SVGMobject.init_colors(self)
        self.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        self.submobjects[1].set_fill("#b3b3b3", opacity=1)
        self.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        self.submobjects[3].set_fill("#b3b3b3", opacity=1)
        self.submobjects[4].set_fill("#ff4e4e", opacity=.7)


Body_color="#0154a4"      #"#0f7391"
Gray="#4d4d4d"
Yellow_f="#948f72"
Black_a="#333333"
Silver="#b3b3b3"

class redled(Scene):
    def construct(self):
        ledred=SVGMobject("LEDSVG",height=2)

        ledred.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        ledred.submobjects[1].set_fill("#b3b3b3", opacity=1)
        ledred.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        ledred.submobjects[3].set_fill("#b3b3b3", opacity=1)
        ledred.submobjects[4].set_fill("#ff4e4e", opacity=.7)


        yellowled=SVGMobject("LEDSVG",height=2)

        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("phototrSVG",height=2)

        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[5].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)


        self.add(opamp)

class usedcomponents(Scene):
    def construct(self):
        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        yellowled=SVGMobject("LEDSVG",height=2)
        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)

        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")
        text03=TextMobject("\\textsf{Phototransistor}")
        text04=TextMobject("\\textsf{OpAmp Breakout}")
        text05=TextMobject("\\textsf{Arduino Uno}")
        text01.shift(DOWN*2)
        text02.shift(DOWN*2)
        text03.shift(DOWN*2)
        text04.shift(DOWN*2)


        image02 = ArduinoUno()
        image02.set_height(3)
        image02.to_edge(RIGHT)
        text05.next_to(image02,DOWN)

        self.play(GrowFromCenter(greenled),run_time=.5)
        self.play(Write(text01))
        self.wait()
        self.play(FadeOut(text01))
        self.play(greenled.to_edge,LEFT)


        self.play(GrowFromCenter(redled))
        self.play(Write(text02))
        self.wait()
        self.play(FadeOut(text02))
        self.play(redled.next_to,greenled,RIGHT,1)

        self.play(GrowFromCenter(phototr))
        self.play(Write(text03))
        self.wait()
        self.play(FadeOut(text03))
        self.play(phototr.next_to,redled,RIGHT,1)

        self.play(GrowFromCenter(opamp))
        self.play(Write(text04))
        self.wait()
        self.play(FadeOut(text04))
        self.play(opamp.next_to,phototr,RIGHT,1)

        self.play(GrowFromCenter(image02))
        self.play(Write(text05))
        self.wait()
        self.play(FadeOut(text05))
        #self.play()

#        self.play(image02.to_edge,DL)
#        self.play(greenled.to_edge,RIGHT,greenled.shift,DOWN)
#        self.play(redled.to_edge,LEFT,redled.shift,UP)
#        self.play(phototr.flip,LEFT,phototr.next_to,greenled,UP,1)

#        self.play(opamp.next_to,image02,RIGHT)


        self.play(image02.to_edge,DL,greenled.to_edge,RIGHT,redled.to_edge,LEFT)
        self.play(greenled.shift,DOWN)
        self.play(redled.shift,UP)
        self.play(phototr.flip,LEFT,phototr.next_to,greenled,UP,1)
        self.play(opamp.next_to,image02,RIGHT)

class usedcomponentsfast(Scene):
    def construct(self):
        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        yellowled=SVGMobject("LEDSVG",height=2)
        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)


        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")
        text03=TextMobject("\\textsf{Phototransistor}")
        text04=TextMobject("\\textsf{OpAmp Breakout}")
        text05=TextMobject("\\textsf{Arduino Uno}")
        text01.shift(DOWN*2)
        text02.shift(DOWN*2)
        text03.shift(DOWN*2)
        text04.shift(DOWN*2)


        image02 = ArduinoUno()
        image02.set_height(3)
        image02.to_edge(RIGHT)



        text05.next_to(image02,DOWN)

        self.play(GrowFromCenter(greenled),Write(text01),run_time=.5)

        #self.wait()
        self.play(FadeOut(text01),run_time=.5)
        self.play(greenled.to_edge,LEFT,run_time=.5)


        self.play(GrowFromCenter(redled),Write(text02),run_time=.5)

#        self.wait()
        self.play(FadeOut(text02),run_time=.5)
        self.play(redled.next_to,greenled,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(phototr),Write(text03),run_time=.5)

#        self.wait()
        self.play(FadeOut(text03),run_time=.5)
        self.play(phototr.next_to,redled,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(opamp),Write(text04))

#        self.wait()
        self.play(FadeOut(text04),run_time=.5)
        self.play(opamp.next_to,phototr,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(image02),Write(text05))

        #self.wait()
        self.play(FadeOut(text05),run_time=.5)
        #self.play()

#        self.play(image02.to_edge,DL)
#        self.play(greenled.to_edge,RIGHT,greenled.shift,DOWN)
#        self.play(redled.to_edge,LEFT,redled.shift,UP)
#        self.play(phototr.flip,LEFT,phototr.next_to,greenled,UP,1)

#        self.play(opamp.next_to,image02,RIGHT)


        self.play(image02.to_edge,DL,greenled.to_edge,RIGHT,redled.to_edge,LEFT,run_time=.5)
        self.play(greenled.shift,DOWN,run_time=.5)
        self.play(redled.shift,UP,run_time=.5)
        self.play(phototr.flip,LEFT,phototr.next_to,greenled,UP,1,run_time=.5)
        self.play(opamp.next_to,image02,RIGHT,run_time=.5)


class usedcomponentsfast01(Scene):
    def construct(self):


        redledc=SVGMobject("LEDSVG",height=2)
        redledc.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redledc.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redledc.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redledc.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redledc.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenledc=SVGMobject("LEDSVG",height=2)
        greenledc.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenledc.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenledc.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenledc.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenledc.submobjects[4].set_fill(GREEN, opacity=.7)

        yellowledc=SVGMobject("LEDSVG",height=2)
        yellowledc.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowledc.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowledc.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowledc.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowledc.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototrc=SVGMobject("LEDSVG",height=2)
        phototrc.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototrc.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototrc.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototrc.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototrc.submobjects[4].set_fill(WHITE, opacity=.9)


        opampc=SVGMobject("OpAmp",height=2)

        opampc.submobjects[0].set_fill(RED, opacity=1)
        opampc.submobjects[13].set_fill(Black_a, opacity=1)
        opampc.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opampc.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opampc.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opampc.submobjects[opholes].set_fill(BLACK, opacity=1)
        image02c = ArduinoUno()
        image02c.set_height(3)
        image02c.to_edge(RIGHT)

        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        yellowled=SVGMobject("LEDSVG",height=2)
        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)

        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")
        text03=TextMobject("\\textsf{Phototransistor}")
        text04=TextMobject("\\textsf{OpAmp Breakout}")
        text05=TextMobject("\\textsf{Arduino Uno}")
        text01.shift(DOWN*2)
        text02.shift(DOWN*2)
        text03.shift(DOWN*2)
        text04.shift(DOWN*2)


        image02 = ArduinoUno()
        image02.set_height(3)
        image02.to_edge(RIGHT)
        text05.next_to(image02,DOWN)

        self.play(GrowFromCenter(greenled),Write(text01),run_time=.5)

        #self.wait()
        self.play(FadeOut(text01),run_time=.5)
        self.play(greenled.to_edge,LEFT,run_time=.5)


        self.play(GrowFromCenter(redled),Write(text02),run_time=.5)

#        self.wait()
        self.play(FadeOut(text02),run_time=.5)
        self.play(redled.next_to,greenled,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(phototr),Write(text03),run_time=.5)

#        self.wait()
        self.play(FadeOut(text03),run_time=.5)
        self.play(phototr.next_to,redled,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(opamp),Write(text04))

#        self.wait()
        self.play(FadeOut(text04),run_time=.5)
        self.play(opamp.next_to,phototr,RIGHT,1,run_time=.5)

        self.play(GrowFromCenter(image02),Write(text05))

        #self.wait()
        self.play(FadeOut(text05),run_time=.5)
        #self.play()

#        self.play(image02.to_edge,DL)
#        self.play(greenled.to_edge,RIGHT,greenled.shift,DOWN)
#        self.play(redled.to_edge,LEFT,redled.shift,UP)
#        self.play(phototr.flip,LEFT,phototr.next_to,greenled,UP,1)

#        self.play(opamp.next_to,image02,RIGHT)
        image02c.to_edge(DL),
        greenledc.to_edge(RIGHT)
        redledc.to_edge(LEFT)
        greenledc.shift(DOWN)
        redledc.shift(UP)
        phototrc.flip(LEFT)
        phototrc.next_to(greenledc,UP,1)
        opampc.next_to(image02c,RIGHT)



        self.play(
        ReplacementTransform(image02,image02c)
        ,ReplacementTransform(greenled,greenledc)
        ,ReplacementTransform(redled,redledc)
        ,ReplacementTransform(phototr,phototrc)
        ,ReplacementTransform(opamp,opampc)




        )
class diyheartratesensor(Scene):
    def construct(self):
        text01=TextMobject("\\textsf{DIY Heart Rate Sensor}")
        text01.set_height(.5)
        text01.shift(UP*2.5)
        self.play(Write(text01))
        imageheart=ImageMobject("heartrate",height=5)
        imageheart.next_to(text01,DOWN)
        self.play(FadeIn(imageheart))
        self.wait()
        self.play(FadeOut(text01),FadeOut(imageheart))



class principle(Scene):
    def construct(self):

        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")




        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)

        #fingerb=ImageMobject("principle",height=8)ff6009
        finger=SVGMobject("finger",height=3)
        finger.submobjects[0].set_fill("#ffccaa", opacity=1)
        finger.submobjects[0].set_fill("#ffccaa", opacity=1)
        finger.submobjects[0].set_stroke("#ffccaa",width=3, opacity=1)
        finger.rotate(PI/2)

        fingerb=SVGMobject("finger",height=3)
        fingerb.submobjects[0].set_fill("#ff6009", opacity=1)
        fingerb.submobjects[0].set_fill("#ff6009", opacity=1)
        fingerb.submobjects[0].set_stroke("#ff6009",width=3, opacity=1)
        fingerb.rotate(PI/2)

        redledglowing=ImageMobject("principle01",height=8)
        redledglowingb=ImageMobject("principle02",height=8)
        greenledglowing=ImageMobject("principle03",height=8)
        greenledglowingb=ImageMobject("principle04",height=8)



        redled.rotate(PI/2)
        redled.shift(UP*2)
        redled.shift(RIGHT*1.1)

        redled2=redled.copy()
        redled2.to_edge(RIGHT)

        redled3=redled.copy()
        redled3.shift(UP*5)

        phototr.rotate(-PI/2)
        phototr.shift(UP*2)
        phototr.shift(LEFT*2)

        phototr2=phototr.copy()
        phototr2.to_edge(LEFT)


        greenled.rotate(PI/2)
        greenled.shift(UP*2)
        greenled.shift(RIGHT*1.1)

        greenled2=greenled.copy()
        greenled2.to_edge(RIGHT)



        self.add(finger)
#        self.add(redled)
#        self.add(phototr)
        self.wait(6)

        self.play(FadeIn(fingerb))
        self.play(FadeOut(fingerb))
        self.play(FadeIn(fingerb))
        self.play(FadeOut(fingerb))
        self.play(FadeIn(fingerb))
        self.play(FadeOut(fingerb))

        self.play(ReplacementTransform(phototr2,phototr))
        self.play(ReplacementTransform(redled2,redled))



        self.play(FadeIn(redledglowing))
        #self.play(FadeOut(redledglowing))
        self.play(FadeIn(redledglowingb))
        self.play(FadeOut(redledglowingb))
        self.play(FadeIn(redledglowingb))
        self.play(FadeOut(redledglowingb))
        self.play(FadeIn(redledglowingb))
        self.play(FadeOut(redledglowingb))
        self.play(FadeOut(redledglowing))

        self.wait(3)

        self.play(ReplacementTransform(redled,redled3))
        #self.pla

        self.play(ReplacementTransform(greenled2,greenled))

        self.play(FadeIn(greenledglowing))

        self.play(FadeIn(greenledglowingb))
        self.play(FadeOut(greenledglowingb))
        self.play(FadeIn(greenledglowingb))
        self.play(FadeOut(greenledglowingb))
        self.play(FadeIn(greenledglowingb))
        self.play(FadeOut(greenledglowingb))
        self.play(FadeOut(greenledglowing))

class principlefadeout(Scene):
    def construct(self):


        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")




        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)

        #fingerb=ImageMobject("principle",height=8)ff6009
        finger=SVGMobject("finger",height=3)
        finger.submobjects[0].set_fill("#ffccaa", opacity=1)
        finger.submobjects[0].set_fill("#ffccaa", opacity=1)
        finger.submobjects[0].set_stroke("#ffccaa",width=3, opacity=1)
        finger.rotate(PI/2)

        fingerb=SVGMobject("finger",height=3)
        fingerb.submobjects[0].set_fill("#ff6009", opacity=1)
        fingerb.submobjects[0].set_fill("#ff6009", opacity=1)
        fingerb.submobjects[0].set_stroke("#ff6009",width=3, opacity=1)
        fingerb.rotate(PI/2)

        redledglowing=ImageMobject("principle01",height=8)
        redledglowingb=ImageMobject("principle02",height=8)
        greenledglowing=ImageMobject("principle03",height=8)
        greenledglowingb=ImageMobject("principle04",height=8)



        redled.rotate(PI/2)
        redled.shift(UP*2)
        redled.shift(RIGHT*1.1)

        redled2=redled.copy()
        redled2.to_edge(RIGHT)

        redled3=redled.copy()
        redled3.shift(UP*5)

        phototr.rotate(-PI/2)
        phototr.shift(UP*2)
        phototr.shift(LEFT*2)

        phototr2=phototr.copy()
        phototr2.to_edge(LEFT)


        greenled.rotate(PI/2)
        greenled.shift(UP*2)
        greenled.shift(RIGHT*1.1)

        greenled2=greenled.copy()
        greenled2.to_edge(RIGHT)



        self.add(finger)
        self.add(greenled)
        self.add(phototr)
        self.play(VFadeOut(VGroup(finger,greenled,phototr)))

        self.wait()







class wondering(Scene):
    def construct(self):

        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)
        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)

        text01=TextMobject("\\textsf{Green LED}")
        text02=TextMobject("\\textsf{Red LED}")
        text03=TextMobject("\\textsf{Phototransistor}")



        greenled.shift(LEFT*2)
        phototr.shift(RIGHT*2)

        text01.next_to(greenled,DOWN)
        text02.next_to(redled,DOWN)
        text03.next_to(phototr,DOWN)

        self.play(GrowFromCenter(greenled))
        self.play(Write(text01))
        self.wait()
        self.play(FadeOut(text01))



        self.play(GrowFromCenter(redled))
        self.play(Write(text02))
        self.wait()
        self.play(FadeOut(text02))
        #self.play(redled.next_to,greenled,RIGHT,1)

        self.play(GrowFromCenter(phototr))
        self.play(Write(text03))
        self.wait()
        self.play(FadeOut(text03))


        self.wait(3)
        self.play(FadeOut(VGroup(greenled,redled,phototr)))





class working(Scene):
    def construct(self):
        prossnobeat=ImageMobject("prossnobeat",height=8)
        prossbeat=ImageMobject("prossbeat",height=8)
        self.add(prossnobeat)
        self.play(FadeIn(prossbeat))
        self.play(FadeOut(prossbeat))
        self.play(FadeIn(prossbeat))
        self.play(FadeOut(prossbeat))
        self.play(FadeIn(prossbeat))
        self.play(FadeOut(prossbeat))
        self.play(FadeIn(prossbeat))
        self.play(FadeOut(prossbeat))


class pross(Scene):
    def construct(self):
        ledred=SVGMobject("LEDSVG",height=2)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)


        yellowled=SVGMobject("LEDSVG",height=2)

        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)

        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)
        #phototr.submobjects[5].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)

        finger=SVGMobject("finger",height=3)

        finger.submobjects[0].set_fill("#ffccaa", opacity=1) #buttonred
        #finger.shift(UP*.5)




        image = ImageMobject("pross",height= 8)

        code = ImageMobject("code",height= 8)
        #code.shift(DOWN)




        image02 = ArduinoUno()
        image02.set_height(3)

        greenled.to_edge(RIGHT)
        greenled.shift(DOWN)
        redled.to_edge(LEFT)
        redled.shift(UP)
        phototr.flip(LEFT)
        phototr.next_to(greenled,UP,1)

        image02.to_edge(DL)
        opamp.next_to(image02,RIGHT)





        self.add(redled)
        self.add(greenled)
        self.add(phototr)
        self.add(opamp)
        self.add(image02)
        self.play(FadeIn(image))
        self.wait(6)
        self.play(FadeIn(code))
        self.wait(6)
        self.play(FadeOut(code))
        self.add(finger)
        self.wait(2)
        self.play(finger.shift,RIGHT*4.5)

        #self.add(linesconnections)
        #self.play(ShowCreation(connection01))
class prossfast(Scene):
    def construct(self):
        ledred=SVGMobject("LEDSVG",height=2)

        greenled=SVGMobject("LEDSVG",height=2)
        greenled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        greenled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        greenled.submobjects[4].set_fill(GREEN, opacity=.7)

        redled=SVGMobject("LEDSVG",height=2)
        redled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        redled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        redled.submobjects[4].set_fill("#ff4e4e", opacity=.7)


        yellowled=SVGMobject("LEDSVG",height=2)

        yellowled.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[1].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        yellowled.submobjects[3].set_fill("#b3b3b3", opacity=1)
        yellowled.submobjects[4].set_fill(YELLOW, opacity=.7)

        phototr=SVGMobject("LEDSVG",height=2)

        phototr.submobjects[0].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[1].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[2].set_fill("#b3b3b3", opacity=1) #buttonred
        phototr.submobjects[3].set_fill("#b3b3b3", opacity=1)
        phototr.submobjects[4].set_fill(WHITE, opacity=.9)
        #phototr.submobjects[5].set_fill(WHITE, opacity=.9)


        opamp=SVGMobject("OpAmp",height=2)

        opamp.submobjects[0].set_fill(RED, opacity=1)
        opamp.submobjects[13].set_fill(Black_a, opacity=1)
        opamp.submobjects[14].set_fill(Body_color, opacity=1)
        for optexts in range(1, 13):
            opamp.submobjects[optexts].set_fill(WHITE, opacity=1)


        for opholes in range(16, 20):
            opamp.submobjects[opholes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            opamp.submobjects[opholes].set_fill(BLACK, opacity=1)

        finger=SVGMobject("finger",height=3)

        finger.submobjects[0].set_fill("#ffccaa", opacity=1) #buttonred
        #finger.shift(UP*.5)




        image = ImageMobject("pross",height= 8)

        code = ImageMobject("code",height= 8)
        #code.shift(DOWN)




        image02 = ArduinoUno()
        image02.set_height(3)

        greenled.to_edge(RIGHT)
        greenled.shift(DOWN)
        redled.to_edge(LEFT)
        redled.shift(UP)
        phototr.flip(LEFT)
        phototr.next_to(greenled,UP,1)

        image02.to_edge(DL)
        opamp.next_to(image02,RIGHT)





        self.add(redled)
        self.add(greenled)
        self.add(phototr)
        self.add(opamp)
        self.add(image02)
        self.play(FadeIn(image))
        #self.wait(6)
        #self.play(FadeIn(code))
        #self.wait(6)
        #self.play(FadeOut(code))
        self.add(finger)
        #self.wait(2)
        self.play(finger.shift,RIGHT*4.5)

class Steamwordmoving(MovingCameraScene):
    def construct(self):
        stemmatrix=SVGMobject("drawingsteam1",height=6)
        steam=VGroup()
        steam.add(stemmatrix.submobjects[0])
        steam.add(stemmatrix.submobjects[1])
        steam.add(stemmatrix.submobjects[2])
        steam.add(stemmatrix.submobjects[3])
        steam.add(stemmatrix.submobjects[4])

        steam.submobjects[0].set_fill(scolor)
        steam.submobjects[1].set_fill(tcolor)
        steam.submobjects[2].set_fill(ecolor)
        steam.submobjects[3].set_fill(mcolor)
        steam.submobjects[4].set_fill(acolor)


        since=VGroup()
        for loop1 in range(5, 11):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            since.add(stemmatrix.submobjects[loop1])
        since.set_fill(scolor)

        tech=VGroup()
        for loop2 in range(11, 20):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            tech.add(stemmatrix.submobjects[loop2])
        tech.set_fill(tcolor)

        eng=VGroup()
        for loop3 in range(20, 30):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            eng.add(stemmatrix.submobjects[loop3])
        eng.set_fill(ecolor)

        art=VGroup()
        for loop4 in range(30, 32):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            art.add(stemmatrix.submobjects[loop4])
        art.set_fill(acolor)

        math=VGroup()
        for loop5 in range(32, 35):
            #self.submobjects[texts].set_fill(WHITE, opacity=1)
            math.add(stemmatrix.submobjects[loop5])
        math.set_fill(mcolor)

        bigsteam=steam.copy()
        bigsteam.set_height(2)
        bigsteam.move_to([0,0,0])


        stema=steam.copy()

        stema.submobjects[4].next_to(stema.submobjects[2],RIGHT)
        stema.submobjects[3].next_to(stema.submobjects[4],RIGHT)

        cenra=VGroup()
        cenra.add(stemmatrix.submobjects[5])
        cenra.add(stemmatrix.submobjects[11])
        cenra.add(stemmatrix.submobjects[20])

        cenra.add(stemmatrix.submobjects[31])
        cenra.add(stemmatrix.submobjects[11].copy())
        cenra.add(stemmatrix.submobjects[30])


        center_word=cenra.copy()


        center_word.submobjects[3].next_to(center_word.submobjects[2],RIGHT)
        center_word.submobjects[4].next_to(center_word.submobjects[3],RIGHT)
        center_word.submobjects[5].next_to(center_word.submobjects[4],RIGHT)
        center_word.submobjects[3].shift(UP*.02)

        random_letters=VGroup()

        for loop6 in range(6, 11):
            random_letters.add(stemmatrix.submobjects[loop6])

        for loop7 in range(12, 20):
            random_letters.add(stemmatrix.submobjects[loop7])

        for loop8 in range(21, 30):
            random_letters.add(stemmatrix.submobjects[loop8])


        for loop10 in range(33, 35):
            random_letters.add(stemmatrix.submobjects[loop10])



        self.play(Write(bigsteam))

        self.play(ReplacementTransform(bigsteam,steam))
        self.play(Write(since))
        self.play(Write(tech),since.fade,.5)
        self.play(Write(eng),tech.fade,.5)
        self.play(Write(art),eng.fade,.5)
        self.play(Write(math),art.fade,.5)



        #self.play(Write(stema))


        self.play(ReplacementTransform(steam,stema),ReplacementTransform(cenra,center_word),FadeOut(stemmatrix.submobjects[32]),VFadeOut(random_letters),self.camera_frame.move_to,stema,self.camera_frame.set_height, 5)
        #self.play(Indicate(cenra))

        #self.play()
        #self.play()
        #self.play()
        self.play(stema.shift,LEFT*2,center_word.next_to,stema.get_center(),RIGHT,.1)


class Steamwordmovingh(Scene):
    def construct(self):
        steameord=TextMobject("\\textsf{STEAM}")
        science=TextMobject("\\textsf{Science}")
        technology=TextMobject("\\textsf{Technology}")
        engineering=TextMobject("\\textsf{Engineering}")
        art=TextMobject("\\textsf{Art}")
        #atr=TextMobject("\\textsf{Atr}")
        math=TextMobject("\\textsf{Math}")
        mtr=TextMobject("\\textsf{Mtr}")
        Aeth=TextMobject("\\textsf{Aeth}")
        stema=TextMobject("\\textsf{STEMA}")
        center=TextMobject("\\textsf{Center}")



        steameord.scale(4)
        science.scale(1.5)
        stema.scale(3)
        technology.scale(1.5)
        engineering.scale(1.5)
        art.scale(1.5)
        Aeth.scale(1.5)
        math.scale(1.5)
        mtr.scale(1.5)
        center.scale(2)

        stema.shift(UP*2)
        #center.shift(UP)


        science.shift(LEFT*2)
        science.shift(UP*2.5)




        technology.next_to(science,DOWN,.5)
        technology.shift(RIGHT*.6)
        engineering.next_to(technology,DOWN,.5)
        engineering.shift(RIGHT*.1)
        art.next_to(engineering,DOWN,.5)
        art.shift(LEFT*1.3)
        math.next_to(art,DOWN,.5)
        math.shift(RIGHT*.3)

        Aeth.move_to(math)
        mtr.move_to(art)
        Aeth.shift(LEFT*.1)



        steameord.submobjects[0].submobjects[0].set_fill(scolor)
        steameord.submobjects[0].submobjects[1].set_fill(tcolor)
        steameord.submobjects[0].submobjects[2].set_fill(ecolor)
        steameord.submobjects[0].submobjects[3].set_fill(acolor)
        steameord.submobjects[0].submobjects[4].set_fill(mcolor)

        science.set_fill(scolor)
        technology.set_fill(tcolor)
        engineering.set_fill(ecolor)
        art.set_fill(acolor)
        math.set_fill(mcolor)

        stema.submobjects[0].submobjects[0].set_fill(scolor)
        stema.submobjects[0].submobjects[1].set_fill(tcolor)
        stema.submobjects[0].submobjects[2].set_fill(ecolor)
        stema.submobjects[0].submobjects[3].set_fill(mcolor)
        stema.submobjects[0].submobjects[4].set_fill(acolor)


        #center.flip(LEFT)
        center.submobjects[0].submobjects[0].set_fill(scolor)
        center.submobjects[0].submobjects[1].set_fill(tcolor)
        center.submobjects[0].submobjects[2].set_fill(ecolor)
        center.submobjects[0].submobjects[3].set_fill(acolor)
        center.submobjects[0].submobjects[4].set_fill(tcolor)
        center.submobjects[0].submobjects[5].set_fill(acolor)



        cience=VGroup()
        for loop01 in range(1, 7):
            cience.add(science.submobjects[0].submobjects[loop01])

        echnology=VGroup()
        for loop02 in range(1, 10):
            echnology.add(technology.submobjects[0].submobjects[loop02])

        ngineering=VGroup()
        for loop03 in range(1, 11):
            ngineering.add(engineering.submobjects[0].submobjects[loop03])

        rt=VGroup()
        for loop04 in range(1, 3):
            rt.add(art.submobjects[0].submobjects[loop04])

        ath=VGroup()
        for loop05 in range(1, 4):
            ath.add(math.submobjects[0].submobjects[loop05])

        ience=VGroup()
        for loop06 in range(2, 7):
            ience.add(science.submobjects[0].submobjects[loop06])

        chnology=VGroup()
        for loop07 in range(2, 10):
            chnology.add(technology.submobjects[0].submobjects[loop07])

        gineering=VGroup()
        for loop08 in range(2, 11):
            gineering.add(engineering.submobjects[0].submobjects[loop08])

        self.play(Write(steameord))
        self.play(
        ReplacementTransform(steameord.submobjects[0].submobjects[0],science.submobjects[0].submobjects[0])
        ,ReplacementTransform(steameord.submobjects[0].submobjects[1],technology.submobjects[0].submobjects[0])
        ,ReplacementTransform(steameord.submobjects[0].submobjects[2],engineering.submobjects[0].submobjects[0])
        ,ReplacementTransform(steameord.submobjects[0].submobjects[3],art.submobjects[0].submobjects[0])
        ,ReplacementTransform(steameord.submobjects[0].submobjects[4],math.submobjects[0].submobjects[0])
        )

        self.play(Write(cience))
        self.play(Write(echnology))
        self.play(Write(ngineering))
        self.play(Write(rt))
        self.play(Write(ath))

#        self.play(ience.fade,.8
#        ,ath.fade,.8
#        ,chnology.fade,.8
#        ,gineering.fade,.8
#        )
        self.play(VFadeOut(VGroup(ience,ath,chnology,gineering)))
        self.play(

        ReplacementTransform(science.submobjects[0].submobjects[0],stema.submobjects[0].submobjects[0])
        ,ReplacementTransform(technology.submobjects[0].submobjects[0],stema.submobjects[0].submobjects[1])
        ,ReplacementTransform(engineering.submobjects[0].submobjects[0],stema.submobjects[0].submobjects[2])
        ,ReplacementTransform(art.submobjects[0].submobjects[0],stema.submobjects[0].submobjects[4])
        ,ReplacementTransform(math.submobjects[0].submobjects[0],stema.submobjects[0].submobjects[3])

        ,ReplacementTransform(science.submobjects[0].submobjects[1],center.submobjects[0].submobjects[0])
        ,ReplacementTransform(technology.submobjects[0].submobjects[1],center.submobjects[0].submobjects[1])
        ,ReplacementTransform(engineering.submobjects[0].submobjects[1],center.submobjects[0].submobjects[2])
        ,ReplacementTransform(art.submobjects[0].submobjects[2],center.submobjects[0].submobjects[3])
        ,TransformFromCopy(technology.submobjects[0].submobjects[1],center.submobjects[0].submobjects[4])
        ,ReplacementTransform(art.submobjects[0].submobjects[1],center.submobjects[0].submobjects[5])
        )

        self.wait(3)

        self.play(FadeOut(VGroup(stema,center)))

        #)

    #    self.play(ReplacementTransform(art.submobjects[0].submobjects[2],mtr.submobjects[0].submobjects[1])
    #    ,ReplacementTransform(art.submobjects[0].submobjects[1],mtr.submobjects[0].submobjects[2])
    #    )

    #    self.play(ReplacementTransform(art.submobjects[0].submobjects[0],Aeth.submobjects[0].submobjects[0])
    #    ,ReplacementTransform(math.submobjects[0].submobjects[0],mtr.submobjects[0].submobjects[0])
    #    )

    #    self.play(ReplacementTransform(engineering.submobjects[0].submobjects[5],Aeth.submobjects[0].submobjects[1])

    #    )
