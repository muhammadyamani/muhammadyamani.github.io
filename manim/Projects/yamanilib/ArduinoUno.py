from manimlib.imports import *



Body_color="#0154a4"      #"#0f7391"
Gray="#4d4d4d"
Yellow_f="#948f72"
Black_a="#333333"
Silver="#b3b3b3"



class ArduinoUno(SVGMobject):
    CONFIG = {
        "file_name": "ungboard_plain v3",
        "height": 5,
        "stroke_color": WHITE,
        "stroke_width": 0,
        "fill_color": WHITE,
        "fill_opacity": 1,
    }
    def init_colors(self):
        SVGMobject.init_colors(self)
        self.submobjects[0].set_fill(Body_color, opacity=1) #body
        for holes in range(1, 45):
            self.submobjects[holes].set_stroke(Yellow_f, opacity=1, width=4) #holes
            self.submobjects[holes].set_fill(BLACK, opacity=1)

        for texts in range(45, 193):
            self.submobjects[texts].set_fill(WHITE, opacity=1)

        for lines in range(193, 196):
            self.submobjects[lines].set_stroke(WHITE, opacity=1, width=2)


        for gray_layer in range(196, 206):
                #self.submobjects[texts].set_fill(WHITE, opacity=1)
            self.submobjects[gray_layer].set_fill(Gray, opacity=1)
            self.submobjects[gray_layer].set_stroke(Gray, opacity=1)

        for yellow_layer in range(206, 218):
            self.submobjects[yellow_layer].set_fill(Yellow_f, opacity=1)
            self.submobjects[yellow_layer].set_stroke(Yellow_f, opacity=1)

        for black_layer in range(218, 256):
            self.submobjects[black_layer].set_fill(Black_a, opacity=1)
            self.submobjects[black_layer].set_stroke(Black_a, opacity=1)

        for sliver_layer in range(256, 265):
            self.submobjects[sliver_layer].set_fill(Silver, opacity=1)
            self.submobjects[sliver_layer].set_stroke(Silver, opacity=1)



        self.submobjects[265].set_fill(RED, opacity=1) #buttonred
        self.submobjects[265].set_stroke(RED, opacity=1)

        self.submobjects[266].set_fill(YELLOW, opacity=.4)
        self.submobjects[266].set_stroke(YELLOW, opacity=.4)

        self.submobjects[267].set_fill(YELLOW, opacity=.4)
        self.submobjects[267].set_stroke(YELLOW, opacity=.4)

        self.submobjects[268].set_fill(YELLOW, opacity=.4)
        self.submobjects[268].set_stroke(YELLOW, opacity=.4)

        self.submobjects[269].set_fill(YELLOW, opacity=1)
        self.submobjects[269].set_stroke(YELLOW, opacity=1)

        self.submobjects[270].set_fill(Gray, opacity=1)
        self.submobjects[270].set_stroke(Gray, opacity=1)

        atmega=VGroup()
        atmega.add(self.submobjects[253])
        atmega.add(self.submobjects[270])

        for atmega_silver in range(271, 327):
            self.submobjects[atmega_silver].set_fill(Silver, opacity=1)
            self.submobjects[atmega_silver].set_stroke(Silver, opacity=1)
            atmega.add(self.submobjects[atmega_silver])
