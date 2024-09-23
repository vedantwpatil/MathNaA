from manim import *


class DirectionalDerivative(ThreeDScene):
    def construct(self):
        # Introduction text
        intro_text = Text("Directional Derivatives", font_size=72)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Setup the 3D coordinate axes
        axes = ThreeDAxes()
        self.play(Create(axes))
        self.wait(1)

        # Define the function f(x, y) = x^2 + y^2
        def func(x, y):
            return x**2 + y**2

        # Plot the function
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        self.play(Create(surface))
        self.wait(1)

        # Example function
        example_func = Text("Example: f(x, y) = x^2 + y^2", font_size=36)
        example_func.to_edge(UP)
        self.play(Write(example_func))
        self.wait(1)

        # Define a point (1, 1) and a direction vector (1/sqrt(2), 1/sqrt(2))
        point = np.array([1, 1, func(1, 1)])
        direction = np.array([1 / np.sqrt(2), 1 / np.sqrt(2), 0])
        point_marker = Dot3D(point, color=RED)
        self.play(Create(point_marker))
        self.wait(1)

        direction_vector = Arrow3D(point, point + direction, color=GREEN)
        self.play(Create(direction_vector))
        self.wait(1)

        # Display the directional derivative formula
        dir_deriv_formula = MathTex(
            r"D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}"
        ).next_to(example_func, DOWN)
        self.play(Write(dir_deriv_formula))
        self.wait(2)

        # Calculate the gradient
        gradient_calc = MathTex(
            r"\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)",
            r"= (2x, 2y)",
        ).next_to(dir_deriv_formula, DOWN)
        self.play(Write(gradient_calc))
        self.wait(3)

        gradient_at_point = MathTex(
            r"\nabla f(1, 1) = (2 \cdot 1, 2 \cdot 1) = (2, 2)"
        ).next_to(gradient_calc, DOWN)
        self.play(Write(gradient_at_point))
        self.wait(3)

        # Display the direction vector
        direction_vector_text = MathTex(
            r"\mathbf{u} = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)"
        ).next_to(gradient_at_point, DOWN)
        self.play(Write(direction_vector_text))
        self.wait(3)

        # Calculate the dot product
        dot_product_calc = MathTex(
            r"D_{\mathbf{u}} f = (2, 2) \cdot \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)",
            r"= 2 \cdot \frac{1}{\sqrt{2}} + 2 \cdot \frac{1}{\sqrt{2}}",
            r"= 2\sqrt{2}",
        ).next_to(direction_vector_text, DOWN)
        self.play(Write(dot_product_calc))
        self.wait(3)

        # Summary text
        summary_text = Text(
            "The directional derivative of f at (1, 1) in the direction of (1/sqrt(2), 1/sqrt(2)) is 2sqrt(2)",
            font_size=36,
        ).next_to(dot_product_calc, DOWN)
        self.play(Write(summary_text))
        self.wait(3)

        self.play(
            FadeOut(summary_text),
            FadeOut(dot_product_calc),
            FadeOut(direction_vector_text),
            FadeOut(gradient_at_point),
            FadeOut(gradient_calc),
            FadeOut(dir_deriv_formula),
            FadeOut(example_func),
            FadeOut(surface),
            FadeOut(axes),
            FadeOut(point_marker),
            FadeOut(direction_vector),
        )
        self.wait(1)
