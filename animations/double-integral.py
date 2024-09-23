from manim import *


class DoubleIntegral(Scene):
    def construct(self):
        # Introduction text
        intro_text = Text("Double Integrals", font_size=72)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Setup the coordinate plane
        axes = ThreeDAxes()
        self.play(Create(axes))
        self.wait(1)

        # Define the function f(x, y) = x + y
        def func(x, y):
            return x + y

        # Plot the function
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[0, 2],
            v_range=[0, 2],
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        self.play(Create(surface))
        self.wait(1)

        # Show the region of integration
        region = Polygon(
            axes.c2p(0, 0, 0),
            axes.c2p(2, 0, 0),
            axes.c2p(2, 2, 0),
            axes.c2p(0, 2, 0),
            fill_color=GREEN,
            fill_opacity=0.5,
            stroke_color=GREEN,
        )
        self.play(Create(region))
        self.wait(1)

        # Animate the idea of summing up small rectangles
        dx = 0.2
        dy = 0.2
        rectangles = VGroup()
        for i in range(10):
            for j in range(10):
                rect = Polygon(
                    axes.c2p(i * dx, j * dy, 0),
                    axes.c2p((i + 1) * dx, j * dy, 0),
                    axes.c2p((i + 1) * dx, (j + 1) * dy, 0),
                    axes.c2p(i * dx, (j + 1) * dy, 0),
                    fill_color=YELLOW,
                    fill_opacity=0.5,
                    stroke_color=YELLOW,
                )
                rectangles.add(rect)

        self.play(Create(rectangles, run_time=4, lag_ratio=0.1))
        self.wait(1)

        # Label the integral
        integral_label = MathTex(r"\iint_R (x + y) \, dA", font_size=48).to_edge(UP)
        self.play(Write(integral_label))
        self.wait(2)

        # Transition to final result
        result_label = MathTex(
            r"\iint_R (x + y) \, dA = \int_0^2 \int_0^2 (x + y) \, dx \, dy",
            font_size=48,
        ).next_to(integral_label, DOWN, buff=0.5)
        self.play(Write(result_label))
        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(rectangles),
            FadeOut(surface),
            FadeOut(region),
            FadeOut(axes),
            FadeOut(integral_label),
            FadeOut(result_label),
        )
        self.wait(1)
