import azure.functions as func
import logging
from PIL import Image
import io
from rembg import remove
import numpy as np

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Read the image data from the request
        image_data = req.get_body()
        if image_data:
            # Convert byte data to a PIL Image
            input_image = Image.open(io.BytesIO(image_data))

            # Remove the background
            output_image = remove(input_image)

            # Save the result to a byte buffer
            byte_io = io.BytesIO()
            output_image.save(byte_io, format="PNG")
            byte_io.seek(0)

            return func.HttpResponse(byte_io.getvalue(), mimetype="image/png")
        else:
            return func.HttpResponse("No image in request", status_code=400)
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

