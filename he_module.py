
class HeModule:
    def __init__(self, jetana="เงียบ", axis="XYZ", collapse="mirror"):
        self.jetana = jetana
        self.axis = axis
        self.collapse_mode = collapse

    def analyze(self, input_state):
        return f"State {input_state} collapsed via {self.jetana} in axis {self.axis}"

    def mirror_reflection(self):
        return f"เจตนาในระบบ 'เขา' สะท้อนกลับมาที่คุณ: {self.jetana}"
