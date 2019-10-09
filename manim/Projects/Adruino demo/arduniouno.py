from manimlib.imports import *
from yamanilib.ArduinoUno import *
from scipy import signal
from yamanilib.ResistorCreature import *


class NumberPlane1(NumberPlane):
    CONFIG = {
        "axis_config": {
            "stroke_color": BLACK,
            "stroke_width": 0,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "background_line_style": {
        "stroke_color": BLUE_D,
        "stroke_width": 2,
        "stroke_opacity": .8,
        }}
  
  class Ardemo(MovingCameraScene):
    def construct(self):

        image02 = ArduinoUno()
        myname=SVGMobject("mynamesf",height=(image02.get_height()/25))
        myname.next_to(image02.submobjects[69],DOWN,buff=SMALL_BUFF)

        myname.shift(RIGHT*.5*1.25)
        myname.shift(DOWN*.25*1.35)
        myname.set_fill(WHITE,opacity=.5)
        myname.set_stroke(Body_color,opacity=1)#,width=1)
        image02.add(myname)

        self.play(Write(image02))

        atmega=VGroup()
        atmega.add(image02.submobjects[253])
        atmega.add(image02.submobjects[270])

        for atmega_silver in range(271, 327):
            image02.submobjects[atmega_silver].set_fill(Silver, opacity=1)
            image02.submobjects[atmega_silver].set_stroke(Silver, opacity=1)
            atmega.add(image02.submobjects[atmega_silver])

        #self.add(image02)

        #self.play(self.camera_frame.set_height, 5)

        self.play(self.camera_frame.move_to,atmega,self.camera_frame.set_height, 3.5)

        self.play(WiggleOutThenIn(atmega))

        square01 =Rectangle(height=1)
        square02 =Rectangle(height=3)
        square01.set_stroke(RED, opacity=1)
        square02.set_stroke(RED, opacity=1)
        square01.stroke_width=5
        square02.stroke_width=5
        square01.surround(atmega)
        #square02.surround(unonomicro)
        text04=TexMobject("\\textsf{ATmega328}")
        text04.move_to(atmega)
        text04.set_height(.4)


        pwm=VGroup()
        pwm.add(image02.submobjects[190])
        pwm.add(image02.submobjects[189])
        pwm.add(image02.submobjects[188])
        pwm.add(image02.submobjects[187])
        pwm.add(image02.submobjects[191])
        pwm.add(image02.submobjects[192])

        circle01=Circle().set_stroke(width=7)

        circle02=circle01.copy()
        circle03=circle01.copy()
        circle04=circle01.copy()
        circle05=circle01.copy()
        circle06=circle01.copy()

        circle01.surround(pwm.submobjects[0])
        circle02.surround(pwm.submobjects[1])
        circle03.surround(pwm.submobjects[2])
        circle04.surround(pwm.submobjects[3])
        circle05.surround(pwm.submobjects[4])
        circle06.surround(pwm.submobjects[5])

        circle01.set_height(.2)
        circle02.set_height(.2)
        circle03.set_height(.2)
        circle04.set_height(.2)
        circle05.set_height(.2)
        circle06.set_height(.2)

        pwmcircles=VGroup()
        pwmcircles.add(circle01)
        pwmcircles.add(circle02)
        pwmcircles.add(circle03)
        pwmcircles.add(circle04)
        pwmcircles.add(circle05)
        pwmcircles.add(circle06)


        #self.play(ApplyMethod(image02.submobjects[0].fade, 0.7))
        self.play(ShowCreation(square01))
        self.play(Write(text04))
        self.play(VFadeOut(VGroup(text04,square01)))
        #self.play()
        #self.play(WiggleOutThenIn(unonomicro))

        self.play(self.camera_frame.move_to,pwm,self.camera_frame.set_height, 1.5)

        self.play(
        ShowCreation(circle01),
        ShowCreation(circle02),
        ShowCreation(circle03),
        ShowCreation(circle04),
        ShowCreation(circle05),
        ShowCreation(circle06)

        )

        self.play(
        FadeOut(circle01),
        FadeOut(circle02),
        FadeOut(circle03),
        FadeOut(circle04),
        FadeOut(circle05),
        FadeOut(circle06)

        )
        self.play(self.camera_frame.move_to,image02,self.camera_frame.set_height, 10)
        
  class Ardemo02(Scene):




    def get_pwm_wave(self,dx=0):
        def func01(x):

            ppwm = signal.square(4 *x, .1) + 1

            if dx <= 1:
                ppwm = signal.square(4 *x, dx) + 1




            #return y
            return ppwm
        return PWM(func01 ,x_min=0,x_max=10)

    def construct(self):
        pwm_function=self.get_pwm_wave()
        d_theta=ValueTracker(0)
        def update_wave(func):
            func.become(
                self.get_pwm_wave(dx=d_theta.get_value())
            )
            return func

        decimal = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=0,
            include_sign=False,
        )
        decimal.to_edge(UP)

        decimal01 = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=1,
            include_sign=False,
        )
        decimal01.next_to(decimal,DOWN)

        decimal.add_updater(lambda d: d.set_value(d_theta.get_value()*255))
        decimal01.add_updater(lambda d: d.set_value(d_theta.get_value()*5))
        plane=NumberPlane1()
        plane.move_to(RIGHT*4)
        plane.set_width(8)

        textvolt = TextMobject("Voltage")
        textvolt01= TextMobject("V")
        textanalog = TextMobject("AnalogWrite(")
        textanalog01=TextMobject(")")
        textvolt.next_to(decimal01,LEFT)
        textvolt01.next_to(decimal01,RIGHT)

        textanalog.next_to(decimal,LEFT)
        textanalog01.next_to(decimal,RIGHT,buff=.7)



        image02 = ArduinoUno()
        image02.set_height(4)

        myname=SVGMobject("mynamesf",height=.16)
        myname.next_to(image02.submobjects[69],DOWN,buff=SMALL_BUFF)
        myname.shift(RIGHT*.5)
        myname.shift(DOWN*.25)
        myname.set_fill(WHITE,opacity=.5)
        image02.add(myname)

        self.add(image02)


        self.play(image02.to_edge,LEFT*2)

        pwm_function.add_updater(update_wave)


        text01=TextMobject("0 V")
        text01.shift(DOWN)
        text02=TextMobject("2.5 V")
        text03=TextMobject("5 V")
        text03.shift(UP)

        text01.set_fill(WHITE ,opacity=1)
        text02.set_fill(WHITE ,opacity=1)
        text03.set_fill(WHITE ,opacity=1)
        text01.set_height(.25)
        text02.set_height(.25)
        text03.set_height(.25)

        text01.shift(LEFT*.35)
        text02.shift(LEFT*.35)
        text03.shift(LEFT*.35)




        res=Res().to_edge(DR)
        res.set_height(1.5)
        res.shift(UP)

        thought=SVGMobject("Bubbles_thought",height=3,width=3.5)
        thought.set_stroke(WHITE, opacity=1,width=2)
        thought.next_to(res,UP)
        thought.shift(RIGHT*1.5)
        thought.shift(DOWN*.3)
        thought.set_fill(BLACK)

        text05=TextMobject("Analog From Digital?")
        text05.move_to(thought)
        text05.shift(UP*.5)
        text05.set_height(.28)
        text05.set_stroke(WHITE)
        #text01.set_fill(BLACK)



        self.play(DrawBorderThenFill(res),run_time=1)
        self.play(res.change,"happy01",image02)
        self.play(res.change,"happy03",text05)
        self.play(ShowCreation(thought))
        self.play(Write(text05))
        self.play(Blink(res))
        self.play(VFadeOut(VGroup(res,thought,text05)))


        self.add(plane)
        self.add(decimal)
        self.add(decimal01)
        self.add(textvolt)
        self.add(textvolt01)
        self.add(textanalog)
        self.add(textanalog01)
        self.play(ShowCreation(pwm_function))
        self.play(d_theta.increment_value,1,rate_func=linear,run_time=3)
        self.wait()
        pwm_function.remove_updater(update_wave)
        self.play(VFadeOut(VGroup(image02,plane,decimal,decimal01,textvolt,textvolt01,textanalog,textanalog01,pwm_function)))
        
        
