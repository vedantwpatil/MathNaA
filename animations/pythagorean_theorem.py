from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Polygon(
            ORIGIN, 
            3 * RIGHT, 
            3 * RIGHT + 4 * UP, 
            fill_color=BLUE, 
            fill_opacity=0.5
        ).set_stroke(color=WHITE, width=2)
        
        # Create labels for the sides
        a_label = MathTex("a").next_to(triangle, LEFT, buff=0.1)
        b_label = MathTex("b").next_to(triangle, DOWN, buff=0.1)
        c_label = MathTex("c").next_to(triangle, UR, buff=0.1)

        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)
        
        # Draw squares on each side of the triangle
        square_a = Square(side_length=3, fill_color=GREEN, fill_opacity=0.5).move_to(1.5 * LEFT + 1.5 * DOWN)
        square_b = Square(side_length=4, fill_color=RED, fill_opacity=0.5).move_to(2 * RIGHT + 2 * UP)
        square_c = Square(side_length=5, fill_color=YELLOW, fill_opacity=0.5).move_to(2.5 * RIGHT + 2.5 * UP)

        self.play(Create(square_a))
        self.play(Create(square_b))
        self.play(Create(square_c))
        self.wait(1)

        # Label squares with their areas
        area_a_label = MathTex("a^2").move_to(square_a.get_center())
        area_b_label = MathTex("b^2").move_to(square_b.get_center())
        area_c_label = MathTex("c^2").move_to(square_c.get_center())

        self.play(Write(area_a_label))
        self.play(Write(area_b_label))
        self.play(Write(area_c_label))
        self.wait(1)

        # Write the Pythagorean theorem
        theorem = MathTex("a^2 + b^2 = c^2").to_edge(UP)

        self.play(Write(theorem))
        self.wait(2)
