import reflex as rf

@rf.noup
class MyComponent(rf.Component):
    def render(self):
        return rf.div("This is a Reflex component.")
