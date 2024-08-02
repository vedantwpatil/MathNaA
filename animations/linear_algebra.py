from manim import *


class LinearAlgebraConcepts(Scene):
    def construct(self):
        # Setup the coordinate plane
        plane = NumberPlane()
        self.play(Create(plane))
        self.wait(1)

        # Define vectors
        vector_1 = Vector([2, 1], color=BLUE)
        vector_2 = Vector([1, 2], color=GREEN)
        vector_sum = Vector([3, 3], color=YELLOW)

        # Show vector addition
        vector_1_label = MathTex(r"\vec{v_1}").next_to(vector_1, UP)
        vector_2_label = MathTex(r"\vec{v_2}").next_to(vector_2, UP)
        vector_sum_label = MathTex(r"\vec{v_1} + \vec{v_2}").next_to(vector_sum, UP)

        self.play(GrowArrow(vector_1), Write(vector_1_label))
        self.play(GrowArrow(vector_2), Write(vector_2_label))
        self.wait(1)

        # Vector addition (parallelogram law)
        self.play(vector_2.animate.shift(vector_1.get_end()))
        self.play(GrowArrow(vector_sum), Write(vector_sum_label))
        self.wait(1)

        # Reset scene
        self.play(
            FadeOut(vector_1),
            FadeOut(vector_2),
            FadeOut(vector_sum),
            FadeOut(vector_1_label),
            FadeOut(vector_2_label),
            FadeOut(vector_sum_label),
        )
        self.wait(1)

        # Show scalar multiplication
        vector_3 = Vector([1, 1], color=RED)
        scalar = 2
        vector_scaled = Vector([2, 2], color=PURPLE)

        vector_3_label = MathTex(r"\vec{v}").next_to(vector_3, UP)
        vector_scaled_label = MathTex(r"2 \vec{v}").next_to(vector_scaled, UP)

        self.play(GrowArrow(vector_3), Write(vector_3_label))
        self.wait(1)
        self.play(
            Transform(vector_3, vector_scaled),
            Transform(vector_3_label, vector_scaled_label),
        )
        self.wait(1)

        # Reset scene
        self.play(FadeOut(vector_3), FadeOut(vector_3_label))
        self.wait(1)

        # Show matrix transformation
        matrix = [[1, 1], [0, 1]]
        vector_4 = Vector([1, 2], color=ORANGE)
        vector_transformed = Vector(
            [3, 2], color=PINK
        )  # Result of multiplying by the matrix

        vector_4_label = MathTex(r"\vec{v}").next_to(vector_4, UP)
        vector_transformed_label = MathTex(r"A \vec{v}").next_to(vector_transformed, UP)
        matrix_label = MathTex(
            r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}"
        ).to_edge(UP)

        self.play(GrowArrow(vector_4), Write(vector_4_label))
        self.play(Write(matrix_label))
        self.wait(1)
        self.play(
            Transform(vector_4, vector_transformed),
            Transform(vector_4_label, vector_transformed_label),
        )
        self.wait(2)

        self.play(
            FadeOut(plane),
            FadeOut(vector_4),
            FadeOut(vector_4_label),
            FadeOut(matrix_label),
        )
        self.wait(1)
