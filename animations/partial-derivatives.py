from manim import *


class PartialDerivatives(ThreeDScene):
    def construct(self):
        # Introduction text
        intro_text = Text("Partial Derivatives", font_size=72)
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

        # Example 1: f(x, y) = x^2 + y^2
        example_1 = Text("Example 1: f(x, y) = x^2 + y^2", font_size=36)
        example_1.to_edge(UP)
        self.play(Write(example_1))
        self.wait(1)

        # Show partial derivative with respect to x
        fx_label = MathTex(r"\frac{\partial f}{\partial x} = 2x").next_to(
            example_1, DOWN
        )
        self.play(Write(fx_label))
        self.wait(1)

        # Visualize fx at y = 0
        y_val = 0
        fx_plane = Surface(
            lambda u, v: axes.c2p(u, y_val, func(u, y_val)),
            u_range=[-2, 2],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[RED, RED],
        )
        self.play(Create(fx_plane))
        self.wait(2)
        self.play(FadeOut(fx_plane))

        # Show partial derivative with respect to y
        fy_label = MathTex(r"\frac{\partial f}{\partial y} = 2y").next_to(
            fx_label, DOWN
        )
        self.play(Write(fy_label))
        self.wait(1)

        # Visualize fy at x = 0
        x_val = 0
        fy_plane = Surface(
            lambda u, v: axes.c2p(x_val, u, func(x_val, u)),
            u_range=[-2, 2],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Create(fy_plane))
        self.wait(2)
        self.play(FadeOut(fy_plane))

        self.play(FadeOut(fx_label), FadeOut(fy_label), FadeOut(example_1))
        self.wait(1)

        # Example 2: f(x, y) = sin(x) * cos(y)
        example_2 = Text("Example 2: f(x, y) = \\sin(x) \\cos(y)", font_size=36)
        example_2.to_edge(UP)
        self.play(Write(example_2))
        self.wait(1)

        # Show partial derivative with respect to x
        fx_label_2 = MathTex(
            r"\frac{\partial f}{\partial x} = \cos(x) \cos(y)"
        ).next_to(example_2, DOWN)
        self.play(Write(fx_label_2))
        self.wait(1)

        # Visualize fx_2 at y = 0
        fx_plane_2 = Surface(
            lambda u, v: axes.c2p(u, 0, np.cos(u)),
            u_range=[-PI, PI],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[RED, RED],
        )
        self.play(Create(fx_plane_2))
        self.wait(2)
        self.play(FadeOut(fx_plane_2))

        # Show partial derivative with respect to y
        fy_label_2 = MathTex(
            r"\frac{\partial f}{\partial y} = -\sin(x) \sin(y)"
        ).next_to(fx_label_2, DOWN)
        self.play(Write(fy_label_2))
        self.wait(1)

        # Visualize fy_2 at x = 0
        fy_plane_2 = Surface(
            lambda u, v: axes.c2p(0, u, -np.sin(u)),
            u_range=[-PI, PI],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Create(fy_plane_2))
        self.wait(2)
        self.play(FadeOut(fy_plane_2))

        self.play(FadeOut(fx_label_2), FadeOut(fy_label_2), FadeOut(example_2))
        self.wait(1)

        # Example 3: f(x, y) = e^(xy)
        example_3 = Text("Example 3: f(x, y) = e^{xy}", font_size=36)
        example_3.to_edge(UP)
        self.play(Write(example_3))
        self.wait(1)

        # Show partial derivative with respect to x
        fx_label_3 = MathTex(r"\frac{\partial f}{\partial x} = y e^{xy}").next_to(
            example_3, DOWN
        )
        self.play(Write(fx_label_3))
        self.wait(1)

        # Visualize fx_3 at y = 1
        fx_plane_3 = Surface(
            lambda u, v: axes.c2p(u, 1, np.exp(u)),
            u_range=[-2, 2],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[RED, RED],
        )
        self.play(Create(fx_plane_3))
        self.wait(2)
        self.play(FadeOut(fx_plane_3))

        # Show partial derivative with respect to y
        fy_label_3 = MathTex(r"\frac{\partial f}{\partial y} = x e^{xy}").next_to(
            fx_label_3, DOWN
        )
        self.play(Write(fy_label_3))
        self.wait(1)

        # Visualize fy_3 at x = 1
        fy_plane_3 = Surface(
            lambda u, v: axes.c2p(1, u, np.exp(u)),
            u_range=[-2, 2],
            v_range=[-0.1, 0.1],
            fill_opacity=0.75,
            checkerboard_colors=[YELLOW, YELLOW],
        )
        self.play(Create(fy_plane_3))
        self.wait(2)
        self.play(FadeOut(fy_plane_3))

        self.play(
            FadeOut(fx_label_3),
            FadeOut(fy_label_3),
            FadeOut(example_3),
            FadeOut(surface),
            FadeOut(axes),
        )
        self.wait(1)

        # Summary
        summary_text = Text("Summary", font_size=48)
        self.play(Write(summary_text))
        self.wait(1)

        summary_explanation = Text(
            "Partial derivatives represent the rate of change of a function\n"
            "with respect to one variable, keeping the other variables constant.\n\n"
            "For a function f(x, y), the partial derivatives are:\n"
            r"$\frac{\partial f}{\partial x}$: Rate of change with respect to x\n"
            r"$\frac{\partial f}{\partial y}$: Rate of change with respect to y",
            font_size=36,
            line_spacing=1.5,
        ).next_to(summary_text, DOWN)
        self.play(Write(summary_explanation))
        self.wait(3)

        self.play(FadeOut(summary_text), FadeOut(summary_explanation))
        self.wait(1)
