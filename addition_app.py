import gradio as gr


def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2


# Create a Gradio interface for the add_numbers function using the updated API
interface = gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(label="Number 1"), gr.Number(label="Number 2")],
    outputs=gr.Text(label="Result"),
    title="Addition Calculator",
    description="A simple Gradio app to add two numbers. Enter two numbers and see the result."
)

# Launch the application
if __name__ == "__main__":
    interface.launch()
