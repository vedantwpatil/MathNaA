from manim import *


class PolarScene(Scene):
    def construct(self):
        # Create a ValueTracker to animate the functions
        e = ValueTracker(0.01)

        # Create the Polar Plane
        plane = PolarPlane(radius_max=3, size=6).add_coordinates()
        plane.shift(LEFT * 2)

        # Define the polar graph using ParametricFunction
        graph1 = always_redraw(
            lambda: ParametricFunction(
                lambda t: plane.polar_to_point(2 * np.sin(3 * t), t),
                t_range=[0, e.get_value()],
                color=GREEN,
                stroke_width=4,
            )
        )

        # Define the moving dot on the polar graph
        dot1 = always_redraw(
            lambda: Dot(color=GREEN).scale(0.5).move_to(graph1.get_end())
        )

        # Create the Cartesian Axes
        axes = Axes(
            x_range=[0, 4, 1], x_length=3, y_range=[-3, 3, 1], y_length=3
        ).shift(RIGHT * 4)
        axes.add_coordinates()

        # Define the Cartesian graph
        graph2 = always_redraw(
            lambda: axes.plot(
                lambda x: 2 * np.sin(3 * x), x_range=[0, e.get_value()], color=GREEN
            )
        )

        # Define the moving dot on the Cartesian graph
        dot2 = always_redraw(
            lambda: Dot(color=GREEN).scale(0.5).move_to(graph2.get_end())
        )

        # Add title text
        title = MathTex(r"f(\theta) = 2\sin(3\theta)", color=GREEN).next_to(
            axes, UP, buff=0.2
        )

        # Animate the creation of plane, axes, and title
        self.play(
            LaggedStart(
                Create(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5
            )
        )

        # Add the graphs and dots to the scene
        self.add(graph1, graph2, dot1, dot2)

        # Animate the ValueTracker to draw the graphs
        self.play(e.animate.set_value(PI), run_time=10, rate_func=linear)

        # Hold the final frame
        self.wait()
