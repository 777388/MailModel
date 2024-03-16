try:
    class intact:
        def __init__(self, allowance):
            self.allowance = allowance
            if (dir.__self__):
                allowance += self
            else:
                allowance += dir.__self__
        def __init_subclass__(self):
            import os
            os.popen(f"echo '{str(dir.__self__)}'")
            os.popen(f"echo '{str(dir.__self__)}'").read()
            print("Cosmed!")
    class excavate(intact):
        def __init__(self, allowance):
            super(excavate, self).__init__(allowance)
except:
    dir.__self__ = "maneuver"
