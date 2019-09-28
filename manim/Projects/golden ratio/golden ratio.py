from manimlib.imports import *
import numpy as np


class Octa(RegularPolygon):
    def __init__(self, **kwargs):
        RegularPolygon.__init__(self, n=10, **kwargs)


class besm(Scene):
    def construct(self):
        image05 = SVGMobject("Basmala01",height= 1.5)
        image06 = SVGMobject("drawings",height= 1)
        image07 = SVGMobject("teen",height= .5)

        self.play(Write(image05),run_time=2)
        self.wait(1)
        self.play(FadeOut(image05))

        #besmel=bes()
        #self.play(Write(bes().submobjects[0]),run_time=1)
        #self.play(Write(bes().submobjects[1]),run_time=2)


        text01=TextMobject("We have certainly created man in the best of stature")
        text02=TextMobject("Quran 95:4")



        text01.shift(DOWN*1.5)
        text02.set_height=.5
        text02.next_to(text01,DOWN)
        text02.shift(RIGHT*4.6)
        image06.shift(UP*1.5)
        image07.next_to(image06,DOWN)
        image07.shift(LEFT*2.6)


        enaya=VGroup(text01,text02)
        araya=VGroup(image06,image07)

        #self.play(Write(image06))
        #self.play(Write(text01))
        #self.play(Write(text02))

        #self.play(Write(image06),Write(image07),Write(text01),Write(text02))
        self.play(Write(araya),Write(enaya))
        self.wait(1)
        self.play(VFadeOut(araya),VFadeOut(enaya))

class phived(Scene):
    def construct(self):
        text01 = SVGMobject("goldenratio",height= .4)
        text02 = TextMobject("From Line To The Human Face")
        text03 = TextMobject("Animated By") #Muhammad Yamani
        myname = SVGMobject("myname",height= .4)
        myname01 = SVGMobject("myname",height= .4)
        myname02 = SVGMobject("myname",height= .2)
        text03.shift(LEFT*3)



        text01.shift(UP*1.5)
        text02.shift(UP*.5)
        #text02.shift(RIGHT*.7)
        text03.shift(DOWN*.5)
        text03.shift(RIGHT*.1)
        #text04.next_to(text03,RIGHT)
        myname01.next_to(text03,RIGHT)
        myname01.shift(UP*.06)
        myname02.to_edge(DR)

        self.play(Write(text01))
        self.play(Write(text02))
        self.play(Write(text03))
        self.play(Write(myname01))
        self.wait()
        #alltext =VGroups(text01,text02,text03)
        #alltext.add(text01,text02,text03)

        self.play(FadeOut(text01),FadeOut(text02),FadeOut(text03),ReplacementTransform(myname01,myname02),run_time=.5,rate_func=smooth)

class phicreate(Scene):
    def  construct(self):



        decimal00 = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False,
        )
        square = Square().to_edge(UP)

        decimal01 = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False,
        )
        square = Square().to_edge(UP)

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)

        circle = Circle().move_to(ORIGIN)
        circle.set_width(6)

        circle.rotate(PI/2)

        a = octa.get_vertices()



        a_scale=[0,0,0,0,0,0,0,0,0,0]
        scale_value=2

        a_scale=scale_value*a

        line00=Line(a_scale[2],a_scale[4]).set_stroke(RED, opacity=1)
        line01=Line(a_scale[4],a_scale[6]).set_stroke(RED, opacity=1)
        line02=Line(a_scale[6],a_scale[8]).set_stroke(RED, opacity=1)
        line03=Line(a_scale[8],a_scale[0]).set_stroke(RED, opacity=1)
        line04=Line(a_scale[0],a_scale[2]).set_stroke(RED, opacity=1)

        line05=Line(a_scale[1],a_scale[3]).set_stroke( width=1)
        line06=Line(a_scale[3],a_scale[5]).set_stroke( width=1)
        line07=Line(a_scale[5],a_scale[7]).set_stroke( width=1)
        line08=Line(a_scale[7],a_scale[9]).set_stroke( width=1)
        line09=Line(a_scale[9],a_scale[1]).set_stroke( width=1)

        line10=Line(a_scale[2],a_scale[6]).set_stroke(BLUE, opacity=1)
        line11=Line(a_scale[6],a_scale[0]).set_stroke(BLUE, opacity=1)
        line12=Line(a_scale[0],a_scale[4]).set_stroke(BLUE, opacity=1)
        line13=Line(a_scale[4],a_scale[8]).set_stroke(BLUE, opacity=1)
        line14=Line(a_scale[8],a_scale[2]).set_stroke(BLUE, opacity=1)

        line15=Line(a_scale[1],a_scale[5]).set_stroke( width=1)
        line16=Line(a_scale[5],a_scale[9]).set_stroke( width=1)
        line17=Line(a_scale[9],a_scale[3]).set_stroke( width=1)
        line18=Line(a_scale[3],a_scale[7]).set_stroke( width=1)
        line19=Line(a_scale[7],a_scale[1]).set_stroke( width=1)


        line20=Line(a_scale[3],a_scale[6]).set_stroke( width=1)
        line21=Line(a_scale[6],a_scale[9]).set_stroke( width=1)
        line22=Line(a_scale[9],a_scale[2]).set_stroke( width=1)
        line23=Line(a_scale[2],a_scale[5]).set_stroke( width=1)
        line24=Line(a_scale[5],a_scale[8]).set_stroke( width=1)

        line25=Line(a_scale[8],a_scale[1]).set_stroke( width=1)
        line26=Line(a_scale[1],a_scale[4]).set_stroke( width=1)
        line27=Line(a_scale[4],a_scale[7]).set_stroke( width=1)
        line28=Line(a_scale[7],a_scale[0]).set_stroke( width=1)
        line29=Line(a_scale[0],a_scale[3]).set_stroke( width=1)

        line30=Line(a_scale[2],a_scale[7]).set_stroke( width=1)
        line31=Line(a_scale[3],a_scale[8]).set_stroke( width=1)
        line32=Line(a_scale[4],a_scale[9]).set_stroke( width=1)
        line33=Line(a_scale[5],a_scale[0]).set_stroke( width=1)
        line34=Line(a_scale[6],a_scale[1]).set_stroke( width=1)

        #line35=Line(a_scale[7],a_scale[2])
        #line36=Line(a_scale[8],a_scale[3])
        #line37=Line(a_scale[9],a_scale[4])
        #line38=Line(a_scale[0],a_scale[5])
        #line39=Line(a_scale[1],a_scale[6])



        #self.play(ShowCreation(circle))



        text000=TextMobject(".4").move_to(a_scale[0])
        text001=TextMobject("1").move_to(a_scale[1])
        text002=TextMobject("2").move_to(a_scale[2])
        text003=TextMobject("3").move_to(a_scale[3])
        text004=TextMobject("4").move_to(a_scale[4])

        text005=TextMobject("5").move_to(a_scale[5])
        text006=TextMobject("6").move_to(a_scale[6])
        text007=TextMobject("7").move_to(a_scale[7])
        text008=TextMobject("8").move_to(a_scale[8])
        text009=TextMobject("9").move_to(a_scale[9])









        #self.add(text000,text001,text002,text003,text004,text005,text006,text007,text008,text009)


        penta01 = VGroup()
        penta01.add(line00)
        penta01.add(line01)
        penta01.add(line02)
        penta01.add(line03)
        penta01.add(line04)

        penta02 = VGroup()
        penta02.add(line05)
        penta02.add(line06)
        penta02.add(line07)
        penta02.add(line08)
        penta02.add(line09)

        penta01in = VGroup()
        penta01in.add(line10)
        penta01in.add(line11)
        penta01in.add(line12)
        penta01in.add(line13)
        penta01in.add(line14)

        penta02in = VGroup()
        penta02in.add(line15)
        penta02in.add(line16)
        penta02in.add(line17)
        penta02in.add(line18)
        penta02in.add(line19)

        octalines = VGroup()
        octalines.add(line20)
        octalines.add(line21)
        octalines.add(line22)
        octalines.add(line23)
        octalines.add(line24)
        octalines.add(line25)
        octalines.add(line26)
        octalines.add(line27)
        octalines.add(line28)
        octalines.add(line29)
        octalines.add(line30)
        octalines.add(line31)
        octalines.add(line32)
        octalines.add(line33)
        octalines.add(line34)

        penta01v=VGroup()
        penta01v.add(penta01)
        penta01v.add(penta01in)

        line14f=Line().set_stroke(BLUE, opacity=1)
        line14f.set_length(line14.get_length())
        line14f.move_to(a_scale[8])
        line14f.shift(RIGHT*(line14f.get_length()/2))

        line00c=line00.copy()
        line01c=line01.copy()
        line02c=line02.copy()
        line04c=line04.copy()
        line02f=line02.copy()
        #line02f.move_to(a_scale[6])

        line02f.set_stroke(width=4)

        brace01 = Brace(line02f , UP, buff = SMALL_BUFF)
        brace02 = Brace(line02f , UP, buff = SMALL_BUFF)
        brace02.shift(RIGHT*line02f.get_length())

        brace03 = Brace(line14f , UP, buff = SMALL_BUFF)
        brace04 = Brace(line14f , DOWN, buff = SMALL_BUFF)
        brace05 = Brace(VGroup(line02f,line14f) , DOWN, buff = SMALL_BUFF)

        text010=TextMobject("1").next_to(brace01,UP)
        text011=TextMobject("1").next_to(brace03,UP)
        text012=TextMobject("1.000...").next_to(brace03,UP)
        text013=TextMobject("The Golden Line").next_to(line02f,DOWN)
        text014=TextMobject("The Golden Acute Triangle").next_to(line02f,DOWN)
        text015=TextMobject("The Golden Obtuse Triangle").next_to(line02f,DOWN)
        decimal00.next_to(brace03,UP)
        decimal01.next_to(brace05,DOWN)



        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)





        self.play(ShowCreation(line02f))
        self.play(ShowCreation(line14f))

        self.play(GrowFromCenter(brace01))

        self.play(GrowFromCenter(brace02))

        decimal00.add_updater(lambda d: d.next_to(brace03, UP))
        decimal00.add_updater(lambda d: d.set_value((brace02.get_width()/brace01.get_width())))

        self.add(decimal00,text010)

        #

        self.play(ReplacementTransform(brace02,brace03),run_time=2)

        #decimal00.remove_updater(lambda d: d.next_to(brace03, UP))
        #decimal00.remove_updater(lambda d: d.set_value((brace02.get_width()/brace01.get_width())))
        #self.add(decimal00.copy())

        self.play(Indicate(decimal00))
        self.wait()

        self.play(FadeOut(brace03),FadeOut(text010))


        #

        self.play(ReplacementTransform(brace01,brace03))

        self.play(GrowFromCenter(brace04))


        self.remove(decimal00)
        self.play(ReplacementTransform(text012,text011))

        decimal01.add_updater(lambda d: d.next_to(brace05, DOWN))
        decimal01.add_updater(lambda d: d.set_value((brace04.get_width()/brace03.get_width())))
        self.add(decimal01,text011)

        self.play(ReplacementTransform(brace04,brace05),run_time=2)
        #
        self.play(Indicate(decimal01))
        self.wait()



        self.play(FadeOut(brace05),FadeOut(decimal01),FadeOut(text011),FadeOut(brace03))


        self.play(Write(text013))
        self.wait()
        self.play(Indicate(VGroup(line02f,line14f)))
        self.play(FadeOut(text013))


        oblic=VGroup(line02f,line14f,line14)
        aqute01=VGroup(line00,line01,line14)
        aqute02=VGroup(line03,line04,line14f)
        aqute03=VGroup(line01,line02,line13)
        aqute04=VGroup(line02,line03,line11)
        aqute05=VGroup(line00,line04,line12)


        oblic01=VGroup(line03,line12,line13)
        oblic02=VGroup(line10,line11,line04)







        self.play(
            Rotating(
                line14f,
                radians=108*DEGREES,
                about_point=line02f.end,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )


        self.play(
            Rotating(
                line14,
                radians=-36*DEGREES,
                about_point=line14.end,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )

        self.play(Write(text014))
        self.wait()
        self.play(Indicate(oblic))
        self.play(FadeOut(text014))

        self.play(
            Rotating(
                line02c,
                radians=108*DEGREES,
                about_point=line02.start,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )

        self.play(
            Rotating(
                line01c,
                radians=108*DEGREES,
                about_point=line01.start,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )



        self.play(Write(text015))
        self.wait()
        self.play(Indicate(VGroup(line01c,line02c,line14)))
        self.play(FadeOut(text015))


        self.play(
            Rotating(
                line00c,
                radians=108*DEGREES,
                about_point=line00.start,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )
        self.play(
            Rotating(
                line04c,
                radians=108*DEGREES,
                about_point=line04.start,
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )


        t=line02.get_length()
        r=t/(2*np.tan(PI/5))

        radline=Line()
        radline.set_length(r*2)
        radline.move_to(a_scale[6])
        radline.rotate(54*DEGREES)



        self.add(oblic)
        self.add(aqute01)
        self.add(aqute02)
        #self.remove(line14f,line02f,line14,line02c,line01c,line00c,line04c)


        self.play(
            Rotating(
                aqute01.copy(),
                radians=72*DEGREES,
                about_point=octa.get_center(),
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )
        self.play(
            Rotating(
                aqute03.copy(),
                radians=72*DEGREES,
                about_point=octa.get_center(),
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )
        self.play(
            Rotating(
                aqute02.copy(),
                radians=72*DEGREES,
                about_point=octa.get_center(),
                rate_func=linear
                ),
            run_time=1, rate_func=smooth
            )
        #self.play(ShowCreation(line01))


        #self.play(Indicate(aqute01))
        #self.play(Indicate(aqute03))
        #self.play(Indicate(aqute04))
        #self.play(Indicate(aqute02))
        #self.play(Indicate(aqute05))

        #self.play(Indicate(oblic))
        #self.play(Indicate(oblic01))
        #self.play(Indicate(oblic02))

        #self.play(Indicate(penta01))
        #self.wait()


# first 6   , 3.7    ,   2.3   , 1.4   ,   .9   , .5 ,.4


        self.wait()

class tri(Scene):
    def  construct(self):



        decimal00 = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False,
        )
        square = Square().to_edge(UP)

        decimal01 = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=False,
        )
        square = Square().to_edge(UP)

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)

        circle = Circle().move_to(ORIGIN)
        circle.set_width(6)

        circle.rotate(PI/2)

        a = octa.get_vertices()

        a_scale=[0,0,0,0,0,0,0,0,0,0]
        scale_value=2

        a_scale=scale_value*a

        line00=Line(a_scale[2],a_scale[4]).set_stroke(RED, opacity=1)
        line01=Line(a_scale[4],a_scale[6]).set_stroke(RED, opacity=1)
        line02=Line(a_scale[6],a_scale[8]).set_stroke(RED, opacity=1)
        line03=Line(a_scale[8],a_scale[0]).set_stroke(RED, opacity=1)
        line04=Line(a_scale[0],a_scale[2]).set_stroke(RED, opacity=1)

        line05=Line(a_scale[1],a_scale[3]).set_stroke( width=2)
        line06=Line(a_scale[3],a_scale[5]).set_stroke( width=2)
        line07=Line(a_scale[5],a_scale[7]).set_stroke( width=2)
        line08=Line(a_scale[7],a_scale[9]).set_stroke( width=2)
        line09=Line(a_scale[9],a_scale[1]).set_stroke( width=2)

        line10=Line(a_scale[2],a_scale[6]).set_stroke(BLUE, opacity=1)
        line11=Line(a_scale[6],a_scale[0]).set_stroke(BLUE, opacity=1)
        line12=Line(a_scale[0],a_scale[4]).set_stroke(BLUE, opacity=1)
        line13=Line(a_scale[4],a_scale[8]).set_stroke(BLUE, opacity=1)
        line14=Line(a_scale[8],a_scale[2]).set_stroke(BLUE, opacity=1)

        line15=Line(a_scale[1],a_scale[5]).set_stroke( width=2)
        line16=Line(a_scale[5],a_scale[9]).set_stroke( width=2)
        line17=Line(a_scale[9],a_scale[3]).set_stroke( width=2)
        line18=Line(a_scale[3],a_scale[7]).set_stroke( width=2)
        line19=Line(a_scale[7],a_scale[1]).set_stroke( width=2)


        line20=Line(a_scale[3],a_scale[6]).set_stroke( width=1)
        line21=Line(a_scale[6],a_scale[9]).set_stroke( width=1)
        line22=Line(a_scale[9],a_scale[2]).set_stroke( width=1)
        line23=Line(a_scale[2],a_scale[5]).set_stroke( width=1)
        line24=Line(a_scale[5],a_scale[8]).set_stroke( width=1)

        line25=Line(a_scale[8],a_scale[1]).set_stroke( width=1)
        line26=Line(a_scale[1],a_scale[4]).set_stroke( width=1)
        line27=Line(a_scale[4],a_scale[7]).set_stroke( width=1)
        line28=Line(a_scale[7],a_scale[0]).set_stroke( width=1)
        line29=Line(a_scale[0],a_scale[3]).set_stroke( width=1)

        line30=Line(a_scale[2],a_scale[7]).set_stroke( width=1)
        line31=Line(a_scale[3],a_scale[8]).set_stroke( width=1)
        line32=Line(a_scale[4],a_scale[9]).set_stroke( width=1)
        line33=Line(a_scale[5],a_scale[0]).set_stroke( width=1)
        line34=Line(a_scale[6],a_scale[1]).set_stroke( width=1)

        #line35=Line(a_scale[7],a_scale[2])
        #line36=Line(a_scale[8],a_scale[3])
        #line37=Line(a_scale[9],a_scale[4])
        #line38=Line(a_scale[0],a_scale[5])
        #line39=Line(a_scale[1],a_scale[6])




        penta01 = VGroup()
        penta01.add(line00)
        penta01.add(line01)
        penta01.add(line02)
        penta01.add(line03)
        penta01.add(line04)

        penta02 = VGroup()
        penta02.add(line05)
        penta02.add(line06)
        penta02.add(line07)
        penta02.add(line08)
        penta02.add(line09)

        penta01in = VGroup()
        penta01in.add(line10)
        penta01in.add(line11)
        penta01in.add(line12)
        penta01in.add(line13)
        penta01in.add(line14)

        penta02in = VGroup()
        penta02in.add(line15)
        penta02in.add(line16)
        penta02in.add(line17)
        penta02in.add(line18)
        penta02in.add(line19)

        octalines = VGroup()
        octalines.add(line20)
        octalines.add(line21)
        octalines.add(line22)
        octalines.add(line23)
        octalines.add(line24)
        octalines.add(line25)
        octalines.add(line26)
        octalines.add(line27)
        octalines.add(line28)
        octalines.add(line29)
        octalines.add(line30)
        octalines.add(line31)
        octalines.add(line32)
        octalines.add(line33)
        octalines.add(line34)

        penta01v=VGroup()
        penta01v.add(penta01)
        penta01v.add(penta01in)

        line14f=Line().set_stroke(BLUE, opacity=1)
        line14f.set_length(line14.get_length())
        line14f.move_to(a_scale[8])
        line14f.shift(RIGHT*(line14f.get_length()/2))

        line00c=line00.copy()
        line01c=line01.copy()
        line02c=line02.copy()
        line04c=line04.copy()
        line02f=line02.copy()
        #line02f.move_to(a_scale[6])

        line02f.set_stroke(width=4)





        oblic01=VGroup(line02,line14,line10)
        aqute01=VGroup(line00,line01,line10)
        aqute02=VGroup(line03,line04,line14)
        aqute03=VGroup(line01,line02,line13)
        aqute04=VGroup(line02,line03,line11)
        aqute05=VGroup(line00,line04,line12)


        oblic02=VGroup(line03,line12,line13)
        oblic03=VGroup(line10,line11,line04)
        oblic04=VGroup(line00,line13,line14)
        text016=TextMobject("Regular Pentagon").next_to(line02f,DOWN)

        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)

        self.add(oblic01)
        self.add(aqute01)
        self.add(aqute02)
        self.add(aqute03)
        self.add(aqute04)
        self.add(aqute05)

        self.play(Write(text016))
        self.wait()
        #self.play(Indicate(VGroup(line01c,line02c,line14)))

        self.play(Indicate(penta01))

        self.play(FadeOut(text016))
        self.wait()

        self.play(Indicate_y(oblic01),run_time=.5)
        self.play(Indicate_y(oblic02),run_time=.5)
        self.play(Indicate_y(oblic03),run_time=.5)
        self.play(Indicate_y(oblic04),run_time=.5)
        self.play(Indicate_y(aqute01),run_time=.5)
        self.play(Indicate_y(aqute03),run_time=.5)
        self.play(Indicate_y(aqute04),run_time=.5)
        self.play(Indicate_y(aqute02),run_time=.5)
        self.play(Indicate_y(aqute05),run_time=.5)




        #self.play(Indicate(penta01in),run_time=.5)

        firstpenta=penta01v.copy()
        firstpenta.set_color(WHITE)
        firstpenta.set_height(5.42)
        firstpenta.set_stroke(width=2)
        firstpenta.shift(UP*.1)



        self.play(ReplacementTransform(penta01v,firstpenta))

        #self.wait()





        self.wait()

class face(Scene):
    def construct(self):

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)
        octasize=6
        octa.set_height(octasize)
        octa.set_stroke(width=3,color=WHITE)

        a = octa.get_vertices()


        line00=Line(a[2],a[4]).set_stroke( width=2)
        line01=Line(a[4],a[6]).set_stroke( width=2)
        line02=Line(a[6],a[8]).set_stroke( width=2)
        line03=Line(a[8],a[0]).set_stroke( width=2)
        line04=Line(a[0],a[2]).set_stroke( width=2)

        line05=Line(a[1],a[3]).set_stroke( width=2)
        line06=Line(a[3],a[5]).set_stroke( width=2)
        line07=Line(a[5],a[7]).set_stroke( width=2)
        line08=Line(a[7],a[9]).set_stroke( width=2)
        line09=Line(a[9],a[1]).set_stroke( width=2)

        line10=Line(a[2],a[6]).set_stroke( width=2)
        line11=Line(a[6],a[0]).set_stroke( width=2)
        line12=Line(a[0],a[4]).set_stroke( width=2)
        line13=Line(a[4],a[8]).set_stroke( width=2)
        line14=Line(a[8],a[2]).set_stroke( width=2)

        line15=Line(a[1],a[5]).set_stroke( width=2)
        line16=Line(a[5],a[9]).set_stroke( width=2)
        line17=Line(a[9],a[3]).set_stroke( width=2)
        line18=Line(a[3],a[7]).set_stroke( width=2)
        line19=Line(a[7],a[1]).set_stroke( width=2)


        line20=Line(a[3],a[6]).set_stroke( width=2)
        line21=Line(a[6],a[9]).set_stroke( width=2)
        line22=Line(a[9],a[2]).set_stroke( width=2)
        line23=Line(a[2],a[5]).set_stroke( width=2)
        line24=Line(a[5],a[8]).set_stroke( width=2)

        line25=Line(a[8],a[1]).set_stroke( width=2)
        line26=Line(a[1],a[4]).set_stroke( width=2)
        line27=Line(a[4],a[7]).set_stroke( width=2)
        line28=Line(a[7],a[0]).set_stroke( width=2)
        line29=Line(a[0],a[3]).set_stroke( width=2)

        line30=Line(a[2],a[7]).set_stroke( width=2)
        line31=Line(a[3],a[8]).set_stroke( width=2)
        line32=Line(a[4],a[9]).set_stroke( width=2)
        line33=Line(a[5],a[0]).set_stroke( width=2)
        line34=Line(a[6],a[1]).set_stroke( width=2)

        #line35=Line(a[7],a[2])
        #line36=Line(a[8],a[3])
        #line37=Line(a[9],a[4])
        #line38=Line(a[0],a[5])
        #line39=Line(a[1],a[6])




        penta01 = VGroup()
        penta01.add(line00)
        penta01.add(line01)
        penta01.add(line02)
        penta01.add(line03)
        penta01.add(line04)

        penta02 = VGroup()
        penta02.add(line05)
        penta02.add(line06)
        penta02.add(line07)
        penta02.add(line08)
        penta02.add(line09)

        penta01in = VGroup()
        penta01in.add(line10)
        penta01in.add(line11)
        penta01in.add(line12)
        penta01in.add(line13)
        penta01in.add(line14)

        penta02in = VGroup()
        penta02in.add(line15)
        penta02in.add(line16)
        penta02in.add(line17)
        penta02in.add(line18)
        penta02in.add(line19)

        octalines = VGroup()
        octalines.add(line20)
        octalines.add(line21)
        octalines.add(line22)
        octalines.add(line23)
        octalines.add(line24)
        octalines.add(line25)
        octalines.add(line26)
        octalines.add(line27)
        octalines.add(line28)
        octalines.add(line29)
        octalines.add(line30)
        octalines.add(line31)
        octalines.add(line32)
        octalines.add(line33)
        octalines.add(line34)

        pentastar01=VGroup()
        pentastar01.add(penta01)
        pentastar01.add(penta01in)

        pentastar02=VGroup()
        pentastar02.add(penta02)
        pentastar02.add(penta02in)


        decagonmatrix=VGroup()
        decagonmatrix.add(pentastar01)
        decagonmatrix.add(pentastar02)
        decagonmatrix.add(octa)



        decagonmatrix01=decagonmatrix.copy()
        decagonmatrix01.set_height(octasize/(phi*phi))
        decagonmatrix01.shift(a[7])
        decagonmatrix01.shift(UP*1.15)
        decagonmatrix01.set_stroke(color=RED)#, width=1)

        decagonmatrix02=decagonmatrix.copy()
        decagonmatrix02.set_height(1.65)
        decagonmatrix02.shift(a[4])
        decagonmatrix02.rotate(np.pi/10)
        decagonmatrix02.shift(RIGHT*1.77)
        decagonmatrix02.shift(DOWN*.84)
        decagonmatrix02.set_stroke(color=RED)#, width=1) #eye borrows

        decagonmatrix03=decagonmatrix.copy()
        decagonmatrix03.set_height(octasize/(phi*phi*phi))
        decagonmatrix03.shift(a[0])
        decagonmatrix03.shift(DOWN*.62)
        decagonmatrix03.shift(LEFT*1.92)
        decagonmatrix03.set_stroke(color=YELLOW)#, width=1) #eye pit

        decagonmatrix04=decagonmatrix.copy()
        decagonmatrix04.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix04.shift(a[0])
        decagonmatrix04.shift(DOWN*.63)
        decagonmatrix04.shift(LEFT*3.78)
        decagonmatrix04.set_stroke(color=RED)#, width=1) #eyes


        #decagonmatrix05=decagonmatrix.copy()
        #decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        #decagonmatrix05.shift(a[7])
        #decagonmatrix05.shift(UP*2.)
        ##penta07v.shift(LEFT*3.79)
        #decagonmatrix05.set_stroke(color=YELLOW)#, width=1) #nose tip


        decagonmatrix05=decagonmatrix.copy()
        decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix05.shift(a[7])
        decagonmatrix05.shift(UP*2.16) #2.25
        #penta07v.shift(LEFT*3.79)
        decagonmatrix05.set_stroke(color=YELLOW)#, width=1) #nose tip




        decagonmatrix06=decagonmatrix.copy()
        decagonmatrix06.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix06.shift(a[0])
        decagonmatrix06.shift(DOWN*.62)
        decagonmatrix06.shift(LEFT*1.93)
        decagonmatrix06.set_stroke(color=YELLOW)#, width=1) # pupils

        decagonmatrix07=decagonmatrix.copy()
        decagonmatrix07.set_height(octasize/(phi))
        decagonmatrix07.shift(a[7])
        decagonmatrix07.shift(UP*1.58) #1.58 #1.86
        decagonmatrix07.set_stroke(color=YELLOW)#, width=1) # second


        decagonmatrix08=decagonmatrix.copy()
        decagonmatrix08.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix08.shift(decagonmatrix07.get_center())
        decagonmatrix08.shift(UP*.03)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix08.set_stroke(color=RED)#, width=1) #upper lips

        decagonmatrix09=decagonmatrix.copy()
        decagonmatrix09.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix09.shift(decagonmatrix05.get_center())
        decagonmatrix09.shift(UP*.08)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix09.set_stroke(color=RED)#, width=1) #nose outside

        decagonmatrix10=decagonmatrix.copy()
        decagonmatrix10.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix10.shift(a[7])
        decagonmatrix10.shift(UP*1.29)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix10.set_stroke(color=YELLOW)#, width=1) #lips tip


        decagonmatrix11=decagonmatrix.copy()
        decagonmatrix11.set_height(octasize/(phi*phi*phi))
        decagonmatrix11.shift(a[7])
        decagonmatrix11.shift(UP*1.55) #1.13
        #decagonmatrix11.shift(LEFT*1.92)
        decagonmatrix11.set_stroke(color=YELLOW)#, width=1) #eye pit


        decagonmatrix12=decagonmatrix.copy()
        decagonmatrix12.set_height(octasize/(phi*phi*phi)*.95)
        decagonmatrix12.shift(a[7])
        decagonmatrix12.shift(UP*1.355) #1.355
        decagonmatrix12.rotate(np.pi/10)
        decagonmatrix12.set_stroke(color=YELLOW)#, width=1) #eye pit

        decagonmatrix13=decagonmatrix.copy()
        decagonmatrix13.set_height(1.65)
        decagonmatrix13.shift(a[0])
        decagonmatrix13.rotate(np.pi/10)
        decagonmatrix13.shift(LEFT*1.77)
        decagonmatrix13.shift(DOWN*.84)
        decagonmatrix13.set_stroke(color=RED)#, width=1) #eye borrows right


        decagonmatrix14=decagonmatrix.copy()
        decagonmatrix14.set_height(octasize/(phi*phi*phi))
        decagonmatrix14.shift(a[4])
        decagonmatrix14.shift(DOWN*.62)
        decagonmatrix14.shift(RIGHT*1.92)
        decagonmatrix14.set_stroke(color=YELLOW)#, width=1) #eye pit left

        decagonmatrix15=decagonmatrix.copy()
        decagonmatrix15.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix15.shift(a[4])
        decagonmatrix15.shift(DOWN*.63)
        decagonmatrix15.shift(RIGHT*3.78)
        decagonmatrix15.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix16=decagonmatrix.copy()
        decagonmatrix16.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix16.shift(a[4])
        decagonmatrix16.shift(DOWN*.62)
        decagonmatrix16.shift(RIGHT*1.93)
        decagonmatrix16.set_stroke(color=YELLOW)#, width=1) # pupils


        decagonmatrix17=decagonmatrix.copy()
        decagonmatrix17.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix17.shift(a[7])
        decagonmatrix17.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix17.set_stroke(color=YELLOW)#, width=1) #eyes

        decagonmatrix18=decagonmatrix.copy()
        decagonmatrix18.set_height(octasize/(phi*phi*phi)*.84)
        decagonmatrix18.shift(a[7])
        decagonmatrix18.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix18.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix19=decagonmatrix.copy()
        decagonmatrix19.set_height(octasize/(phi*phi*phi)*1.15)
        decagonmatrix19.shift(a[7])
        decagonmatrix19.shift(UP*.51)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix19.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix20=decagonmatrix.copy()
        decagonmatrix20.set_height(octasize/(phi*phi))
        decagonmatrix20.shift(a[7])
        decagonmatrix20.shift(UP*3)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix20.set_stroke(color=RED)#, width=1) #eyes


        decagonmatrix21=decagonmatrix.copy()
        decagonmatrix21.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix21.shift(a[7])
        decagonmatrix21.shift(UP*2.2)
        #decagonmatrix21.shift(LEFT*1.93)
        decagonmatrix21.set_stroke(color=RED)#, width=1) # pupils

        line14f=Line()
        line14f.set_length(line14.get_length())

        line14f.shift(a[8])
        line14f.shift(RIGHT*(line14.get_height()/2))

        line02f=line02.copy()
        line02f.set_stroke(width=4)

        image05 = ImageMobject("octapaths02",height= 8)
        #self.add(image05)

        image06 = ImageMobject("octapaths04",height= 8)
        #self.add(image06)
        #self.add(decagonmatrix)
        #self.add(octalines)
        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)

        self.add(pentastar01)
        self.play(TransformFromCopy(pentastar01,pentastar02))
        self.play(ShowCreation(octa))
        self.play(ShowCreation(octalines))

        #self.add(decagonmatrix01) #smile .
        #self.add(decagonmatrix02)   #eyes borrows .
        #self.add(decagonmatrix03)  #eyes pit .
        #self.add(decagonmatrix04)  #right eye .
        #self.add(decagonmatrix05)  #nose tip .
        #self.add(decagonmatrix06)  #pupil .
        #self.add(decagonmatrix07)  #seconed .
        #self.add(decagonmatrix08)   #nose under.
        #self.add(decagonmatrix09)  #nose.
        #self.add(decagonmatrix10)   #lips.
        #self.add(decagonmatrix11) #mouth .
        #self.add(decagonmatrix12)  #mouth .
        #self.add(decagonmatrix13)   # right eye borrow .
        #self.add(decagonmatrix14)  # eye left pit .
        #self.add(decagonmatrix15) # eye right .
        #self.add(decagonmatrix16)  # pupil left .
        #self.add(decagonmatrix17)  # chin .
        #self.add(decagonmatrix18)  # chin1
        #self.add(decagonmatrix19) #chin2
        #self.add(decagonmatrix20)  #cinter .
        #self.add(penta02)

        self.play(TransformFromCopy(decagonmatrix,decagonmatrix07))
        self.play(TransformFromCopy(decagonmatrix07,decagonmatrix01),TransformFromCopy(decagonmatrix07,decagonmatrix20))
        self.play(TransformFromCopy(decagonmatrix01,decagonmatrix02),TransformFromCopy(decagonmatrix01,decagonmatrix13))
        self.play(TransformFromCopy(decagonmatrix02,decagonmatrix14),TransformFromCopy(decagonmatrix13,decagonmatrix03))

        self.play(TransformFromCopy(decagonmatrix14,decagonmatrix04),TransformFromCopy(decagonmatrix03,decagonmatrix15))
        self.play(TransformFromCopy(decagonmatrix04,decagonmatrix16),TransformFromCopy(decagonmatrix15,decagonmatrix06))

        self.play(TransformFromCopy(decagonmatrix03,decagonmatrix11),TransformFromCopy(decagonmatrix14,decagonmatrix12))

        self.play(TransformFromCopy(decagonmatrix12,decagonmatrix18))
        self.play(TransformFromCopy(decagonmatrix04,decagonmatrix08),TransformFromCopy(decagonmatrix15,decagonmatrix09))

        self.play(TransformFromCopy(decagonmatrix08,decagonmatrix17))
        self.play(TransformFromCopy(decagonmatrix09,decagonmatrix05),TransformFromCopy(decagonmatrix08,decagonmatrix10))  # to be edited

        #self.play(FadeIn(image05))
        self.wait(2)

class images(Scene):
    def construct(self):

        #image01 = ImageMobject("octapaths",height= 8)
        image02 = ImageMobject("octapaths01",height= 8)
        image03 = ImageMobject("octapaths02",height= 8)
        image04 = ImageMobject("octapaths03",height= 8)
        image05 = ImageMobject("octapaths04",height= 8)
        self.add(image02)
        #self.play(FadeIn(image02))
        #self.wait()
        self.play(FadeIn(image03))
        self.wait()
        self.play(FadeIn(image04))

        self.wait()

        self.play(FadeIn(image05),run_time=2)
        self.wait()

class onface(Scene):
    def construct(self):


        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)
        octasize=6
        octa.set_height(octasize)
        octa.set_stroke(width=3,color=WHITE)

        a = octa.get_vertices()

        line02=Line(a[6],a[8]).set_stroke( width=4)
        line14=Line(a[8],a[2]).set_stroke( width=4)


        line14f=Line().set_stroke(BLUE, opacity=1,width=5)
        line14f.set_length(line14.get_length())
        line14f.move_to(a[8])
        line14f.shift(RIGHT*(line14f.get_length()/2))

        line02f=line02.copy()
        line02f.set_stroke(RED,width=5)

        decagonmatrix=VGroup()
        decagonmatrix.add(line02f)
        decagonmatrix.add(line14f)

        decagonmatrix01=decagonmatrix.copy()
        decagonmatrix01.set_width(octasize/(phi*phi))
        decagonmatrix01.move_to(a[7])
        decagonmatrix01.shift(UP*1.35)
        decagonmatrix01.shift(LEFT*.37)

        decagonmatrix02=decagonmatrix.copy()
        decagonmatrix02.set_width(1.65)
        decagonmatrix02.move_to(a[4])
        decagonmatrix02.shift(RIGHT*1.77)
        decagonmatrix02.shift(DOWN*.855)

        decagonmatrix03=decagonmatrix.copy()
        decagonmatrix03.set_width(octasize/(phi*phi*phi))
        decagonmatrix03.move_to(a[0])
        decagonmatrix03.shift(DOWN*.62)
        decagonmatrix03.shift(LEFT*1.92)

        decagonmatrix04=decagonmatrix.copy()
        decagonmatrix04.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix04.move_to(a[0])
        decagonmatrix04.shift(DOWN*.64)
        decagonmatrix04.shift(LEFT*3.82)

        decagonmatrix05=decagonmatrix.copy()
        decagonmatrix05.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix05.move_to(a[7])
        decagonmatrix05.shift(UP*2.16) #2.25
        decagonmatrix05.set_stroke(color=RED)#, width=1) #nose tip

        decagonmatrix06=decagonmatrix.copy()
        decagonmatrix06.set_width(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix06.move_to(a[0])
        decagonmatrix06.shift(DOWN*.62)
        decagonmatrix06.shift(LEFT*1.93)

        decagonmatrix07=decagonmatrix.copy()
        decagonmatrix07.set_width(octasize/(phi)*.98)
        decagonmatrix07.move_to(a[7])
        decagonmatrix07.shift(UP*2.1) #1.58 #1.86

        decagonmatrix08=decagonmatrix.copy()
        decagonmatrix08.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix08.shift(UP*.03)

        decagonmatrix09=decagonmatrix.copy()
        decagonmatrix09.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix09.shift(decagonmatrix05.get_center())
        decagonmatrix09.shift(UP*.08)

        decagonmatrix10=decagonmatrix.copy()
        decagonmatrix10.set_width(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix10.move_to(a[7])
        decagonmatrix10.shift(UP*1.29)

        decagonmatrix11=decagonmatrix.copy()
        decagonmatrix11.set_width(octasize/(phi*phi*phi))
        decagonmatrix11.move_to(a[7])
        decagonmatrix11.shift(UP*1.55) #1.13

        decagonmatrix12=decagonmatrix.copy()
        decagonmatrix12.set_width(octasize/(phi*phi*phi)*.95)
        decagonmatrix12.move_to(a[7])
        decagonmatrix12.shift(UP*1.355) #1.355

        decagonmatrix13=decagonmatrix.copy()
        decagonmatrix13.set_width(1.65)
        decagonmatrix13.move_to(a[0])
        decagonmatrix13.shift(LEFT*1.77)
        decagonmatrix13.shift(DOWN*.84)

        decagonmatrix14=decagonmatrix.copy()
        decagonmatrix14.set_width(octasize/(phi*phi*phi))
        decagonmatrix14.move_to(a[4])
        decagonmatrix14.shift(DOWN*.64)
        decagonmatrix14.shift(RIGHT*1.92)

        decagonmatrix15=decagonmatrix.copy()
        decagonmatrix15.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix15.move_to(a[4])
        decagonmatrix15.shift(DOWN*.64)
        decagonmatrix15.shift(RIGHT*3.73)

        decagonmatrix16=decagonmatrix.copy()
        decagonmatrix16.set_width(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix16.move_to(a[4])
        decagonmatrix16.shift(DOWN*.62)
        decagonmatrix16.shift(RIGHT*1.93)

        decagonmatrix17=decagonmatrix.copy()
        decagonmatrix17.set_width(octasize/(phi*phi*phi*phi))
        decagonmatrix17.move_to(a[7])
        decagonmatrix17.shift(UP*.4)

        decagonmatrix18=decagonmatrix.copy()
        decagonmatrix18.set_width(octasize/(phi*phi*phi)*.84)
        decagonmatrix18.move_to(a[7])
        decagonmatrix18.shift(UP*.4)

        decagonmatrix19=decagonmatrix.copy()
        decagonmatrix19.set_width(octasize/(phi*phi*phi)*1.15)
        decagonmatrix19.move_to(a[7])
        decagonmatrix19.shift(UP*.51)

        decagonmatrix20=decagonmatrix.copy()
        decagonmatrix20.set_width(octasize/(phi*phi))
        decagonmatrix20.move_to(a[7])
        decagonmatrix20.shift(UP*3)

        decagonmatrix21=decagonmatrix.copy()
        decagonmatrix21.set_width(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix21.move_to(a[7])
        decagonmatrix21.shift(UP*2.2)

        decagonmatrix22=decagonmatrix.copy()
        decagonmatrix22.set_width(1.65)
        decagonmatrix22.rotate(-np.pi/2)
        decagonmatrix22.move_to(a[7])
        decagonmatrix22.shift(UP*1.09)

        decagonmatrix23=decagonmatrix.copy()
        decagonmatrix23.set_width(.43)
        decagonmatrix23.rotate(-np.pi/2)
        decagonmatrix23.move_to(a[7])
        decagonmatrix23.shift(UP*1.26)

        decagonmatrix24=decagonmatrix.copy()
        decagonmatrix24.set_width(5.15)
        decagonmatrix24.rotate(-np.pi/2)
        decagonmatrix24.move_to(a[7])
        decagonmatrix24.shift(UP*2.84)

        decagonmatrix25=decagonmatrix.copy()
        decagonmatrix25.set_width(octasize*1.05/(phi))
        decagonmatrix25.move_to(a[7])
        decagonmatrix25.shift(UP*3.07) #1.58 #1.86

        decagonmatrix26=decagonmatrix.copy()
        decagonmatrix26.set_width(octasize/(phi*phi))
        decagonmatrix26.move_to(a[7])
        decagonmatrix26.shift(UP*3.47) #3.07
        decagonmatrix26.shift(RIGHT*.7) #1.58 #1.86

        #image05 = ImageMobject("octapaths02",height= 8)
        #self.add(image05)

        image06 = ImageMobject("octapaths04",height= 8)
        #self.add(image06)
        #self.add(decagonmatrix)
        #self.add(octalines)

        image05 = ImageMobject("octapaths04",height= 8)
        self.add(image05)


        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)

        #self.add(decagonmatrix01) #smile .
        #self.add(decagonmatrix02)   #eyes borrows
        #self.add(decagonmatrix07)  #seconed .
        #self.add(decagonmatrix10)   # inner lips.
        #self.add(decagonmatrix11) #mouth .
        #self.add(decagonmatrix13)   # right eye borrow .  to delete
        #self.add(decagonmatrix14)  # eye left pit .
        #self.add(decagonmatrix15) # eye right .
        #self.add(decagonmatrix16)  # pupil left .
        #self.add(decagonmatrix20)  #cinter .
        #self.add(decagonmatrix22) #vertical
        #self.add(decagonmatrix23)   #vertical
        #self.add(decagonmatrix24)    #vertical
        #self.add(decagonmatrix25)
        #self.add(decagonmatrix26)
        #self.add(penta02)
#        self.play(ShowCreation(decagonmatrix24))
#        self.play(FadeOut(decagonmatrix24),run_time=.5)
#        self.play(ShowCreation(decagonmatrix22))
#        self.play(FadeOut(decagonmatrix22),run_time=.5)
#        self.play(ShowCreation(decagonmatrix23))
#        self.play(FadeOut(decagonmatrix23),run_time=.5)
#        self.play(ShowCreation(decagonmatrix07))
#        self.play(FadeOut(decagonmatrix07),run_time=.5)
#        self.play(ShowCreation(decagonmatrix20))  #cinter .
#        self.play(FadeOut(decagonmatrix20),run_time=.5)
#        self.play(ShowCreation(decagonmatrix26))
#        self.play(FadeOut(decagonmatrix26),run_time=.5)
#        self.play(ShowCreation(decagonmatrix01)) #smile .
#        self.play(FadeOut(decagonmatrix01),run_time=.5)
#        self.play(ShowCreation(decagonmatrix02))   #eyes borrows .
#        self.play(FadeOut(decagonmatrix02),run_time=.5)
#        self.play(ShowCreation(decagonmatrix03))  #eyes pit .
#        self.play(FadeOut(decagonmatrix03),run_time=.5)
#        self.play(ShowCreation(decagonmatrix04))  #right eye . to shift lift
#        self.play(FadeOut(decagonmatrix04),run_time=.5)
#        self.play(ShowCreation(decagonmatrix05))  #nose tip . single
#        self.play(FadeOut(decagonmatrix05),run_time=.5)
#        self.play(ShowCreation(decagonmatrix11)) #mouth .
#        self.play(FadeOut(decagonmatrix11),run_time=.5)
#        self.play(ShowCreation(decagonmatrix13))   # right eye borrow .
#        self.play(FadeOut(decagonmatrix13),run_time=.5)
#        self.play(ShowCreation(decagonmatrix14))  # eye left pit .
#        self.play(FadeOut(decagonmatrix14),run_time=.5)
#        self.play(ShowCreation(decagonmatrix15)) # eye right .
#        self.play(FadeOut(decagonmatrix15),run_time=.5)
#        self.play(ShowCreation(decagonmatrix16))  # pupil left .
#        self.play(FadeOut(decagonmatrix16),run_time=.5)

        self.play(Indicate_y(decagonmatrix23))
        self.play(Indicate_y(decagonmatrix22))
        self.play(Indicate_y(decagonmatrix24))
        self.play(Indicate_y(decagonmatrix07))
        #self.play(Indicate_y(decagonmatrix20))
        self.play(Indicate_y(decagonmatrix26))
        self.play(Indicate_y(decagonmatrix01))
        self.play(Indicate_y(decagonmatrix02))
        self.play(Indicate_y(decagonmatrix03))
        self.play(Indicate_y(decagonmatrix04))
        #self.play(Indicate_y(decagonmatrix05))
        self.play(Indicate_y(decagonmatrix11))
        self.play(Indicate_y(decagonmatrix25))
        #self.play(Indicate_y(decagonmatrix26))

        self.wait(2)

        image07 = ImageMobject("octapaths04",height= 8)
        self.play(FadeIn(image07))

class tri01face(Scene):
    def construct(self):

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)
        octasize=6
        octa.set_height(octasize)
        octa.set_stroke(width=3,color=WHITE)

        a = octa.get_vertices()


        line00=Line(a[2],a[4]).set_stroke( width=4)
        line01=Line(a[4],a[6]).set_stroke( width=2)
        line02=Line(a[6],a[8]).set_stroke( width=2)
        line03=Line(a[8],a[0]).set_stroke( width=2)
        line04=Line(a[0],a[2]).set_stroke( width=4)

        line05=Line(a[1],a[3]).set_stroke( width=4)
        line06=Line(a[3],a[5]).set_stroke( width=2)
        line07=Line(a[5],a[7]).set_stroke( width=2)
        line08=Line(a[7],a[9]).set_stroke( width=2)
        line09=Line(a[9],a[1]).set_stroke( width=2)

        line10=Line(a[2],a[6]).set_stroke( width=2)
        line11=Line(a[6],a[0]).set_stroke( width=2)
        line12=Line(a[0],a[4]).set_stroke( width=4)
        line13=Line(a[4],a[8]).set_stroke( width=2)
        line14=Line(a[8],a[2]).set_stroke( width=2)

        line15=Line(a[1],a[5]).set_stroke( width=2)
        line16=Line(a[5],a[9]).set_stroke( width=2)
        line17=Line(a[9],a[3]).set_stroke( width=2)
        line18=Line(a[3],a[7]).set_stroke( width=4)
        line19=Line(a[7],a[1]).set_stroke( width=4)


        line20=Line(a[3],a[6]).set_stroke( width=2)
        line21=Line(a[6],a[9]).set_stroke( width=2)
        line22=Line(a[9],a[2]).set_stroke( width=2)
        line23=Line(a[2],a[5]).set_stroke( width=2)
        line24=Line(a[5],a[8]).set_stroke( width=2)

        line25=Line(a[8],a[1]).set_stroke( width=2)
        line26=Line(a[1],a[4]).set_stroke( width=2)
        line27=Line(a[4],a[7]).set_stroke( width=2)
        line28=Line(a[7],a[0]).set_stroke( width=2)
        line29=Line(a[0],a[3]).set_stroke( width=2)

        line30=Line(a[2],a[7]).set_stroke( width=2)
        line31=Line(a[3],a[8]).set_stroke( width=2)
        line32=Line(a[4],a[9]).set_stroke( width=2)
        line33=Line(a[5],a[0]).set_stroke( width=2)
        line34=Line(a[6],a[1]).set_stroke( width=2)


        penta01 = VGroup()
        penta01.add(line00)
        penta01.add(line04)

        penta02 = VGroup()
        penta02.add(line05)

        penta01in = VGroup()
        penta01in.add(line12)


        penta02in = VGroup()
        penta02in.add(line18)
        penta02in.add(line19)

        pentastar01=VGroup()
        pentastar01.add(penta01)
        pentastar01.add(penta01in)

        pentastar02=VGroup()
        pentastar02.add(penta02)
        pentastar02.add(penta02in)


        decagonmatrix=VGroup()
        decagonmatrix.add(pentastar01)
        decagonmatrix.add(pentastar02)


        decagonmatrix01=decagonmatrix.copy()
        decagonmatrix01.set_height(octasize/(phi*phi))
        decagonmatrix01.rotate(np.pi)
        decagonmatrix01.shift(a[7])
        decagonmatrix01.shift(UP*2.28)

        decagonmatrix01.set_stroke(color=RED)#, width=1)

        decagonmatrix02=decagonmatrix.copy()
        decagonmatrix02.set_height(1.65)
        decagonmatrix02.shift(a[4])
        decagonmatrix02.rotate(np.pi/10)
        decagonmatrix02.shift(RIGHT*1.77)
        decagonmatrix02.shift(DOWN*.84)
        decagonmatrix02.set_stroke(color=RED)#, width=1) #eye borrows


        decagonmatrix04=decagonmatrix.copy()
        decagonmatrix04.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix04.shift(a[0])
        decagonmatrix04.shift(DOWN*.9)
        decagonmatrix04.shift(LEFT*3.78)
        decagonmatrix04.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix05=decagonmatrix.copy()
        decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix05.shift(a[7])
        decagonmatrix05.shift(UP*2.16) #2.25
        decagonmatrix05.rotate(np.pi)
        decagonmatrix05.set_stroke(color=RED)#, width=1) #nose tip


        decagonmatrix07=decagonmatrix.copy()
        decagonmatrix07.set_height(octasize/(phi))
        decagonmatrix07.shift(a[7])
        decagonmatrix07.shift(UP*1.58) #1.58 #1.86
        decagonmatrix07.set_stroke(color=RED)#, width=1) # second


        decagonmatrix09=decagonmatrix.copy()
        decagonmatrix09.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix09.shift(a[7])
        decagonmatrix09.shift(UP*1.4)
        decagonmatrix09.rotate(np.pi)

        decagonmatrix09.set_stroke(color=RED)#, width=1) #nose outside

        decagonmatrix10=decagonmatrix.copy()
        decagonmatrix10.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix10.shift(a[7])
        decagonmatrix10.shift(UP*1.29)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix10.set_stroke(color=RED)#, width=1) #lips tip


        decagonmatrix11=decagonmatrix.copy()
        decagonmatrix11.set_height(octasize/(phi*phi*phi))
        decagonmatrix11.shift(a[7])
        decagonmatrix11.shift(UP*1.55) #1.13
        #decagonmatrix11.shift(LEFT*1.92)
        decagonmatrix11.set_stroke(color=RED)#, width=1) #eye pit


        decagonmatrix12=decagonmatrix.copy()
        decagonmatrix12.set_width(.35)
        decagonmatrix12.move_to(a[7])
        decagonmatrix12.shift(UP*.2)
        decagonmatrix12.set_stroke(color=RED)#, width=1) #eye borrows right

        decagonmatrix13=decagonmatrix.copy()
        decagonmatrix13.set_height(1.65)
        decagonmatrix13.shift(a[0])
        decagonmatrix13.rotate(-np.pi/10)
        decagonmatrix13.shift(LEFT*1.77)
        decagonmatrix13.shift(DOWN*.84)
        decagonmatrix13.set_stroke(color=RED)#, width=1) #eye borrows right

        decagonmatrix15=decagonmatrix.copy()
        decagonmatrix15.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix15.shift(a[4])
        decagonmatrix15.shift(DOWN*.9)
        decagonmatrix15.shift(RIGHT*3.78)
        decagonmatrix15.set_stroke(color=RED)#, width=1) #eyes
        decagonmatrix16=decagonmatrix.copy()

        decagonmatrix16.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix16.shift(a[4])
        decagonmatrix16.shift(DOWN*.68)
        decagonmatrix16.shift(RIGHT*2.08)
        decagonmatrix16.set_stroke(color=RED)#, width=1) #eyes
        decagonmatrix16.rotate(np.pi/2)
        decagonmatrix16.rotate(-18*DEGREES)


        decagonmatrix17=decagonmatrix.copy()
        decagonmatrix17.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix17.shift(a[0])
        #decagonmatrix17.flip()

        decagonmatrix17.shift(DOWN*.68) #2.25
        decagonmatrix17.shift(LEFT*2.08)
        decagonmatrix17.set_stroke(color=RED)#, width=1) #nose tip
        decagonmatrix17.rotate(-np.pi/2)
        decagonmatrix17.rotate(18*DEGREES)

        decagonmatrix21=decagonmatrix11.copy()
        decagonmatrix21.shift(DOWN*.42)
        decagonmatrix22=decagonmatrix11.copy()
        decagonmatrix22.rotate(np.pi)
        decagonmatrix22.shift(UP*.02)


        line14f=Line()
        line14f.set_length(line14.get_length())

        line14f.shift(a[8])
        line14f.shift(RIGHT*(line14.get_height()/2))

        line02f=line02.copy()
        line02f.set_stroke(width=4)

        image05 = ImageMobject("octapaths02",height= 8)
        #self.add(image05)

        image06 = ImageMobject("octapaths04",height= 8)
        self.add(image06)




        #self.add(decagonmatrix)
        #self.add(octalines)
        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)



        #self.add(decagonmatrix01.submobjects[1]) #nose lips Triangle
        #self.add(decagonmatrix02.submobjects[0])   #eyes borrows .
        #self.add(decagonmatrix04.submobjects[0])  #right eye .
        #self.add(decagonmatrix05.submobjects[0])  #nose tip .
        #self.add(decagonmatrix07.submobjects[0])  #seconed .
        #self.add(decagonmatrix09.submobjects[1])  #nose.
        #self.add(decagonmatrix10.submobjects[1])   #lips.
        #self.add(decagonmatrix21.submobjects[0]) #mouth .
        #self.add(decagonmatrix12.submobjects[0])  #chin .
        #self.add(decagonmatrix13.submobjects[0])   # right eye borrow .
        #self.add(decagonmatrix15.submobjects[0]) # eye right .
        #self.add(decagonmatrix16.submobjects[1])  # pupil left .
        #self.add(decagonmatrix17.submobjects[1])  # chin .
        #self.add(decagonmatrix22.submobjects[0])  #under lips
        self.play(Indicate_y(decagonmatrix07.submobjects[0]))  #seconed .
        self.play(Indicate_y(decagonmatrix01.submobjects[1])) #nose lips Triangle
        self.play(Indicate_y(decagonmatrix02.submobjects[0]),Indicate_y(decagonmatrix13.submobjects[0]))   #eyes borrows .
        self.play(Indicate_y(decagonmatrix04.submobjects[0]),Indicate_y(decagonmatrix15.submobjects[0]))  # eyes .
        self.play(Indicate_y(decagonmatrix16.submobjects[1]),Indicate_y(decagonmatrix17.submobjects[1]))  # pupil left .
        self.play(Indicate_y(decagonmatrix05.submobjects[0]))  #nose tip .

        self.play(Indicate_y(decagonmatrix09.submobjects[1]))  #nose.
        self.play(Indicate_y(decagonmatrix10.submobjects[1]))   #lips.
        self.play(Indicate_y(decagonmatrix21.submobjects[0])) #mouth .
        self.play(Indicate_y(decagonmatrix22.submobjects[0]))  #under lips
        self.play(Indicate_y(decagonmatrix12.submobjects[0]))  #chin .

        self.wait(2)

        image07 = ImageMobject("octapaths04",height= 8)
        self.play(FadeIn(image07))

class pentaface(Scene):
    def construct(self):

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)
        octasize=6
        octa.set_height(octasize)
        octa.set_stroke(width=3,color=WHITE)

        a = octa.get_vertices()


        line00=Line(a[2],a[4]).set_stroke( width=2)
        line01=Line(a[4],a[6]).set_stroke( width=2)
        line02=Line(a[6],a[8]).set_stroke( width=2)
        line03=Line(a[8],a[0]).set_stroke( width=2)
        line04=Line(a[0],a[2]).set_stroke( width=2)

        line05=Line(a[1],a[3]).set_stroke( width=2)
        line06=Line(a[3],a[5]).set_stroke( width=2)
        line07=Line(a[5],a[7]).set_stroke( width=2)
        line08=Line(a[7],a[9]).set_stroke( width=2)
        line09=Line(a[9],a[1]).set_stroke( width=2)

        line10=Line(a[2],a[6]).set_stroke( width=2)
        line11=Line(a[6],a[0]).set_stroke( width=2)
        line12=Line(a[0],a[4]).set_stroke( width=2)
        line13=Line(a[4],a[8]).set_stroke( width=2)
        line14=Line(a[8],a[2]).set_stroke( width=2)

        line15=Line(a[1],a[5]).set_stroke( width=2)
        line16=Line(a[5],a[9]).set_stroke( width=2)
        line17=Line(a[9],a[3]).set_stroke( width=2)
        line18=Line(a[3],a[7]).set_stroke( width=2)
        line19=Line(a[7],a[1]).set_stroke( width=2)


        line20=Line(a[3],a[6]).set_stroke( width=2)
        line21=Line(a[6],a[9]).set_stroke( width=2)
        line22=Line(a[9],a[2]).set_stroke( width=2)
        line23=Line(a[2],a[5]).set_stroke( width=2)
        line24=Line(a[5],a[8]).set_stroke( width=2)

        line25=Line(a[8],a[1]).set_stroke( width=2)
        line26=Line(a[1],a[4]).set_stroke( width=2)
        line27=Line(a[4],a[7]).set_stroke( width=2)
        line28=Line(a[7],a[0]).set_stroke( width=2)
        line29=Line(a[0],a[3]).set_stroke( width=2)

        line30=Line(a[2],a[7]).set_stroke( width=2)
        line31=Line(a[3],a[8]).set_stroke( width=2)
        line32=Line(a[4],a[9]).set_stroke( width=2)
        line33=Line(a[5],a[0]).set_stroke( width=2)
        line34=Line(a[6],a[1]).set_stroke( width=2)



        penta01 = VGroup()
        penta01.add(line00)
        penta01.add(line01)
        penta01.add(line02)
        penta01.add(line03)
        penta01.add(line04)

        penta02 = VGroup()
        penta02.add(line05)
        penta02.add(line06)
        penta02.add(line07)
        penta02.add(line08)
        penta02.add(line09)

        penta01in = VGroup()
        penta01in.add(line10)
        penta01in.add(line11)
        penta01in.add(line12)
        penta01in.add(line13)
        penta01in.add(line14)

        penta02in = VGroup()
        penta02in.add(line15)
        penta02in.add(line16)
        penta02in.add(line17)
        penta02in.add(line18)
        penta02in.add(line19)



        pentastar01=VGroup()
        pentastar01.add(penta01)
        #pentastar01.add(penta01in)
        pentastar01.set_stroke(width=4)

        pentastar02=VGroup()
        pentastar02.add(penta02)
        #pentastar02.add(penta02in)
        pentastar02.set_stroke(width=4)


        decagonmatrix=VGroup()
        decagonmatrix.add(pentastar01)
        decagonmatrix.add(pentastar02)
        #decagonmatrix.add(octa)



        decagonmatrix01=decagonmatrix.copy()
        decagonmatrix01.set_height(octasize/(phi*phi))
        decagonmatrix01.shift(a[7])
        decagonmatrix01.shift(UP*1.15)
        decagonmatrix01.set_stroke(color=RED)#, width=1)

        decagonmatrix02=decagonmatrix.copy()
        decagonmatrix02.set_height(1.65)
        decagonmatrix02.shift(a[4])
        decagonmatrix02.rotate(np.pi/10)
        decagonmatrix02.shift(RIGHT*1.77)
        decagonmatrix02.shift(DOWN*.84)
        decagonmatrix02.set_stroke(color=RED)#, width=1) #eye borrows

        decagonmatrix03=decagonmatrix.copy()
        decagonmatrix03.set_height(octasize/(phi*phi*phi))
        decagonmatrix03.shift(a[0])
        decagonmatrix03.shift(DOWN*.62)
        decagonmatrix03.shift(LEFT*1.92)
        decagonmatrix03.set_stroke(color=RED)#, width=1) #eye pit

        decagonmatrix04=decagonmatrix.copy()
        decagonmatrix04.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix04.shift(a[0])
        decagonmatrix04.shift(DOWN*.63)
        decagonmatrix04.shift(LEFT*3.78)
        decagonmatrix04.set_stroke(color=RED)#, width=1) #eyes


        #decagonmatrix05=decagonmatrix.copy()
        #decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        #decagonmatrix05.shift(a[7])
        #decagonmatrix05.shift(UP*2.)
        ##penta07v.shift(LEFT*3.79)
        #decagonmatrix05.set_stroke(color=YELLOW)#, width=1) #nose tip


        decagonmatrix05=decagonmatrix.copy()
        decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix05.shift(a[7])
        decagonmatrix05.shift(UP*2.16) #2.25
        #penta07v.shift(LEFT*3.79)
        decagonmatrix05.set_stroke(color=RED)#, width=1) #nose tip




        decagonmatrix06=decagonmatrix.copy()
        decagonmatrix06.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix06.shift(a[0])
        decagonmatrix06.shift(DOWN*.62)
        decagonmatrix06.shift(LEFT*1.93)
        decagonmatrix06.set_stroke(color=RED)#, width=1) # pupils

        decagonmatrix07=decagonmatrix.copy()
        decagonmatrix07.set_height(octasize/(phi))
        decagonmatrix07.shift(a[7])
        decagonmatrix07.shift(UP*1.58) #1.58 #1.86
        decagonmatrix07.set_stroke(color=RED)#, width=1) # second


        decagonmatrix08=decagonmatrix.copy()
        decagonmatrix08.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix08.shift(decagonmatrix07.get_center())
        decagonmatrix08.shift(UP*.03)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix08.set_stroke(color=RED)#, width=1) #upper lips

        decagonmatrix09=decagonmatrix.copy()
        decagonmatrix09.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix09.shift(decagonmatrix05.get_center())
        decagonmatrix09.shift(UP*.08)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix09.set_stroke(color=RED)#, width=1) #nose outside

        decagonmatrix10=decagonmatrix.copy()
        decagonmatrix10.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix10.shift(a[7])
        decagonmatrix10.shift(UP*1.29)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix10.set_stroke(color=RED)#, width=1) #lips tip


        decagonmatrix11=decagonmatrix.copy()
        decagonmatrix11.set_height(octasize/(phi*phi*phi))
        decagonmatrix11.shift(a[7])
        decagonmatrix11.shift(UP*1.55) #1.13
        #decagonmatrix11.shift(LEFT*1.92)
        decagonmatrix11.set_stroke(color=RED)#, width=1) #eye pit


        decagonmatrix12=decagonmatrix.copy()
        decagonmatrix12.set_height(octasize/(phi*phi*phi)*.95)
        decagonmatrix12.shift(a[7])
        decagonmatrix12.shift(UP*1.355) #1.355
        decagonmatrix12.rotate(np.pi/10)
        decagonmatrix12.set_stroke(color=RED)#, width=1) #eye pit

        decagonmatrix13=decagonmatrix.copy()
        decagonmatrix13.set_height(1.65)
        decagonmatrix13.shift(a[0])
        decagonmatrix13.rotate(np.pi/10)
        decagonmatrix13.shift(LEFT*1.77)
        decagonmatrix13.shift(DOWN*.84)
        decagonmatrix13.set_stroke(color=RED)#, width=1) #eye borrows right


        decagonmatrix14=decagonmatrix.copy()
        decagonmatrix14.set_height(octasize/(phi*phi*phi))
        decagonmatrix14.shift(a[4])
        decagonmatrix14.shift(DOWN*.62)
        decagonmatrix14.shift(RIGHT*1.92)
        decagonmatrix14.set_stroke(color=RED)#, width=1) #eye pit left

        decagonmatrix15=decagonmatrix.copy()
        decagonmatrix15.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix15.shift(a[4])
        decagonmatrix15.shift(DOWN*.63)
        decagonmatrix15.shift(RIGHT*3.78)
        decagonmatrix15.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix16=decagonmatrix.copy()
        decagonmatrix16.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix16.shift(a[4])
        decagonmatrix16.shift(DOWN*.62)
        decagonmatrix16.shift(RIGHT*1.93)
        decagonmatrix16.set_stroke(color=RED)#, width=1) # pupils


        decagonmatrix17=decagonmatrix.copy()
        decagonmatrix17.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix17.shift(a[7])
        decagonmatrix17.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix17.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix18=decagonmatrix.copy()
        decagonmatrix18.set_height(octasize/(phi*phi*phi)*.84)
        decagonmatrix18.shift(a[7])
        decagonmatrix18.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix18.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix19=decagonmatrix.copy()
        decagonmatrix19.set_height(octasize/(phi*phi*phi)*1.15)
        decagonmatrix19.shift(a[7])
        decagonmatrix19.shift(UP*.51)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix19.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix20=decagonmatrix.copy()
        decagonmatrix20.set_height(octasize/(phi*phi))
        decagonmatrix20.shift(a[7])
        decagonmatrix20.shift(UP*3)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix20.set_stroke(color=RED)#, width=1) #eyes


        decagonmatrix21=decagonmatrix11.copy()

        #decagonmatrix21.shift(a[7])
        decagonmatrix21.shift(DOWN*.38)
        decagonmatrix21.set_stroke(color=RED)


        line14f=Line()
        line14f.set_length(line14.get_length())

        line14f.shift(a[8])
        line14f.shift(RIGHT*(line14.get_height()/2))

        line02f=line02.copy()
        line02f.set_stroke(width=4)

        image05 = ImageMobject("octapaths02",height= 8)
        self.add(image05)

        image06 = ImageMobject("octapaths04",height= 8)
        self.add(image06)
        #self.add(decagonmatrix)
        #self.add(octalines)
        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)



        #self.add(decagonmatrix01.submobjects[0]) #smile .
        #self.add(decagonmatrix02.submobjects[0])   #eyes borrows .
        #self.add(decagonmatrix03.submobjects[1])  #eyes pit .
        #self.add(decagonmatrix04.submobjects[0])  #right eye .
        #self.add(decagonmatrix05.submobjects[1])  #nose tip .
        #self.add(decagonmatrix09.submobjects[1])  #nose.
        #self.add(decagonmatrix10.submobjects[1])   #lips.
        #self.add(decagonmatrix11.submobjects[1]) #mouth .
        #self.add(decagonmatrix21.submobjects[0]) #mouth .
        #self.add(decagonmatrix13.submobjects[1])   # right eye borrow .
        #self.add(decagonmatrix14.submobjects[1])  # eye left pit .
        #self.add(decagonmatrix15.submobjects[1]) # eye right .

        self.play(Indicate_y(decagonmatrix01.submobjects[0])) #smile .
        self.play(Indicate_y(decagonmatrix02.submobjects[0]),Indicate_y(decagonmatrix13.submobjects[1]))   #eyes borrows .
        self.play(Indicate_y(decagonmatrix03.submobjects[1]),Indicate_y(decagonmatrix14.submobjects[1]))  #eyes pit .
        self.play(Indicate_y(decagonmatrix04.submobjects[0]),Indicate_y(decagonmatrix15.submobjects[1]))  #right eye .

        self.play(Indicate_y(decagonmatrix09.submobjects[1]))  #nose.
        self.play(Indicate_y(decagonmatrix05.submobjects[1]))  #nose tip .
        self.play(Indicate_y(decagonmatrix10.submobjects[1]))   #lips.
        self.play(Indicate_y(decagonmatrix11.submobjects[1])) #mouth .
        self.play(Indicate_y(decagonmatrix21.submobjects[0])) #mouth .







        self.wait(2)
        image07 = ImageMobject("octapaths04",height= 8)
        self.play(FadeIn(image07))

class octaface(Scene):
    def construct(self):

        phi=1.618033988749895
        octa=Octa().rotate(np.pi/10)
        octasize=6
        octa.set_height(octasize)
        octa.set_stroke(width=3,color=WHITE)

        a = octa.get_vertices()




        decagonmatrix=VGroup()

        decagonmatrix.add(octa)



        decagonmatrix01=decagonmatrix.copy()
        decagonmatrix01.set_height(octasize/(phi*phi))
        decagonmatrix01.shift(a[7])
        decagonmatrix01.shift(UP*1.15)
        decagonmatrix01.set_stroke(color=RED)#, width=1)

        decagonmatrix02=decagonmatrix.copy()
        decagonmatrix02.set_height(1.65)
        decagonmatrix02.shift(a[4])
        decagonmatrix02.rotate(np.pi/10)
        decagonmatrix02.shift(RIGHT*1.77)
        decagonmatrix02.shift(DOWN*.84)
        decagonmatrix02.set_stroke(color=RED)#, width=1) #eye borrows

        decagonmatrix03=decagonmatrix.copy()
        decagonmatrix03.set_height(octasize/(phi*phi*phi))
        decagonmatrix03.shift(a[0])
        decagonmatrix03.shift(DOWN*.62)
        decagonmatrix03.shift(LEFT*1.92)
        decagonmatrix03.set_stroke(color=RED)#, width=1) #eye pit

        decagonmatrix04=decagonmatrix.copy()
        decagonmatrix04.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix04.shift(a[0])
        decagonmatrix04.shift(DOWN*.63)
        decagonmatrix04.shift(LEFT*3.78)
        decagonmatrix04.set_stroke(color=RED)#, width=1) #eyes


        #decagonmatrix05=decagonmatrix.copy()
        #decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        #decagonmatrix05.shift(a[7])
        #decagonmatrix05.shift(UP*2.)
        ##penta07v.shift(LEFT*3.79)
        #decagonmatrix05.set_stroke(color=YELLOW)#, width=1) #nose tip


        decagonmatrix05=decagonmatrix.copy()
        decagonmatrix05.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix05.shift(a[7])
        decagonmatrix05.shift(UP*2.16) #2.25
        #penta07v.shift(LEFT*3.79)
        decagonmatrix05.set_stroke(color=RED)#, width=1) #nose tip




        decagonmatrix06=decagonmatrix.copy()
        decagonmatrix06.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix06.shift(a[0])
        decagonmatrix06.shift(DOWN*.64)
        decagonmatrix06.shift(LEFT*1.93)
        decagonmatrix06.set_stroke(color=RED)#, width=1) # pupils

        decagonmatrix07=decagonmatrix.copy()
        decagonmatrix07.set_height(octasize/(phi))
        decagonmatrix07.shift(a[7])
        decagonmatrix07.shift(UP*1.58) #1.58 #1.86
        decagonmatrix07.set_stroke(color=RED)#, width=1) # second


        decagonmatrix08=decagonmatrix.copy()
        decagonmatrix08.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix08.shift(decagonmatrix07.get_center())
        decagonmatrix08.shift(UP*.03)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix08.set_stroke(color=RED)#, width=1) #upper lips

        decagonmatrix09=decagonmatrix.copy()
        decagonmatrix09.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix09.shift(decagonmatrix05.get_center())
        decagonmatrix09.set_stroke(color=RED)#, width=1) #nose outside

        decagonmatrix10=decagonmatrix.copy()
        decagonmatrix10.set_height(octasize/(phi*phi*phi*phi*phi))
        decagonmatrix10.shift(a[7])
        decagonmatrix10.shift(UP*1.29)
        #penta07v.shift(LEFT*3.79)
        decagonmatrix10.set_stroke(color=RED)#, width=1) #lips tip


        decagonmatrix11=decagonmatrix.copy()
        decagonmatrix11.set_height(octasize/(phi*phi*phi))
        decagonmatrix11.shift(a[7])
        decagonmatrix11.shift(UP*1.55) #1.13
        #decagonmatrix11.shift(LEFT*1.92)
        decagonmatrix11.set_stroke(color=RED)#, width=1) #eye pit


        decagonmatrix12=decagonmatrix.copy()
        decagonmatrix12.set_height(octasize/(phi*phi*phi)*.95)
        decagonmatrix12.shift(a[7])
        decagonmatrix12.shift(UP*1.355) #1.355
        decagonmatrix12.rotate(np.pi/10)
        decagonmatrix12.set_stroke(color=RED)#, width=1) #eye pit

        decagonmatrix13=decagonmatrix.copy()
        decagonmatrix13.set_height(1.65)
        decagonmatrix13.shift(a[0])
        decagonmatrix13.rotate(np.pi/10)
        decagonmatrix13.shift(LEFT*1.77)
        decagonmatrix13.shift(DOWN*.84)
        decagonmatrix13.set_stroke(color=RED)#, width=1) #eye borrows right


        decagonmatrix14=decagonmatrix.copy()
        decagonmatrix14.set_height(octasize/(phi*phi*phi))
        decagonmatrix14.shift(a[4])
        decagonmatrix14.shift(DOWN*.62)
        decagonmatrix14.shift(RIGHT*1.92)
        decagonmatrix14.set_stroke(color=RED)#, width=1) #eye pit left

        decagonmatrix15=decagonmatrix.copy()
        decagonmatrix15.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix15.shift(a[4])
        decagonmatrix15.shift(DOWN*.63)
        decagonmatrix15.shift(RIGHT*3.78)
        decagonmatrix15.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix16=decagonmatrix.copy()
        decagonmatrix16.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix16.shift(a[4])
        decagonmatrix16.shift(DOWN*.64)
        decagonmatrix16.shift(RIGHT*1.93)
        decagonmatrix16.set_stroke(color=RED)#, width=1) # pupils


        decagonmatrix17=decagonmatrix.copy()
        decagonmatrix17.set_height(octasize/(phi*phi*phi*phi))
        decagonmatrix17.shift(a[7])
        decagonmatrix17.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix17.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix18=decagonmatrix.copy()
        decagonmatrix18.set_height(octasize/(phi*phi*phi)*.84)
        decagonmatrix18.shift(a[7])
        decagonmatrix18.shift(UP*.4)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix18.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix19=decagonmatrix.copy()
        decagonmatrix19.set_height(octasize/(phi*phi*phi)*1.15)
        decagonmatrix19.shift(a[7])
        decagonmatrix19.shift(UP*.51)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix19.set_stroke(color=RED)#, width=1) #eyes

        decagonmatrix20=decagonmatrix.copy()
        decagonmatrix20.set_height(octasize/(phi*phi))
        decagonmatrix20.shift(a[7])
        decagonmatrix20.shift(UP*3)
        #decagonmatrix17.shift(LEFT*3.78)
        decagonmatrix20.set_stroke(color=RED)#, width=1) #eyes


        decagonmatrix21=decagonmatrix.copy()
        decagonmatrix21.set_height(octasize/(phi*phi*phi*phi*phi*phi))
        decagonmatrix21.shift(a[7])
        decagonmatrix21.shift(UP*2.2)
        #decagonmatrix21.shift(LEFT*1.93)
        decagonmatrix21.set_stroke(color=RED)#, width=1) # pupils

        image05 = ImageMobject("octapaths02",height= 8)
        #self.add(image05)

        image06 = ImageMobject("octapaths04",height= 8)
        self.add(image06)
        #self.add(decagonmatrix)
        #self.add(octalines)
        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)


        #self.add(decagonmatrix01) #smile .
        #self.add(decagonmatrix02)   #eyes borrows .
        #self.add(decagonmatrix03)  #eyes pit .
        #self.add(decagonmatrix04)  #right eye .
        #self.add(decagonmatrix05)  #nose tip .
        #self.add(decagonmatrix06)  #pupil .
        #self.add(decagonmatrix07)  #seconed .
        #self.add(decagonmatrix09)  #nose.
        #self.add(decagonmatrix10)   #lips.
        #self.add(decagonmatrix11) #mouth .
        #self.add(decagonmatrix12)  #mouth .
        #self.add(decagonmatrix13)   # right eye borrow .
        #self.add(decagonmatrix14)  # eye left pit .
        #self.add(decagonmatrix15) # eye right .
        #self.add(decagonmatrix16)  # pupil left .
        #self.add(decagonmatrix17)  # chin .
        #self.add(decagonmatrix18)  # chin1
        #self.add(decagonmatrix19) #chin2
        #self.add(decagonmatrix20)  #cinter .

        self.play(Indicate_y(decagonmatrix20))
        self.play(Indicate_y(decagonmatrix02),Indicate_y(decagonmatrix13))
        self.play(Indicate_y(decagonmatrix03),Indicate_y(decagonmatrix14))
        self.play(Indicate_y(decagonmatrix04),Indicate_y(decagonmatrix15))

        self.play(Indicate_y(decagonmatrix06),Indicate_y(decagonmatrix16))
        self.play(Indicate_y(decagonmatrix09))
        self.play(Indicate_y(decagonmatrix05))
        self.play(Indicate_y(decagonmatrix10))







        self.wait(2)
        image07 = ImageMobject("octapaths04",height= 8)
        self.play(FadeIn(image07))

class closing(Scene):
    def construct(self):

        myname02 = SVGMobject("myname",height= .2)
        myname02.to_edge(DR)
        self.add(myname02)

        myname03 = SVGMobject("myname",height= .35)
        #text00=TextMobject("Rferance : ")
        text01=TextMobject("Reference : www.beautyanalysis.com")
        text02=TextMobject("Artwork By")
        text01.shift(UP*.5)
        text02.next_to(text01,DOWN)
        text02.shift(LEFT*2.35)
        myname03.next_to(text02,RIGHT)
        myname03.shift(UP*.04)


        image07 = ImageMobject("octapaths04",height= 8)
        self.add(image07)
        self.wait(2)
        self.play(FadeOut(image07))#,FadeOut(myname02))
        self.play(Write(text01))
        self.play(Write(text02))
        self.play(ReplacementTransform(myname02,myname03))
        self.wait()
