AR_TEMPLATE_TEX_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "AR_tex_template.tex"
)

with open(AR_TEMPLATE_TEX_FILE, "r") as arinfile:
    AR_TEMPLATE_TEXT_FILE_BODY = arinfile.read()
    AR_TEMPLATE_TEX_FILE_BODY = AR_TEMPLATE_TEXT_FILE_BODY.replace(
        TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{align*}",
    )



class ARTextMobject(TexMobject):
    CONFIG = {
        "template_tex_file_body": AR_TEMPLATE_TEXT_FILE_BODY,
        "alignment": "\\centering",
        "arg_separator": "",
    }

    def __init__(self, *args, **kwargs):
        TexMobject.__init__(self, *args, **kwargs)
        self.submobjects[0].submobjects = list(reversed(self.submobjects[0].submobjects))
