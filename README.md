# Azure Function App for Background Removal

This is an Azure Function App that removes the background from images. It uses [rembg](https://github.com/danielgatis/rembg) to apply a transparent background to submitted files.

## Endpoint

### `api/http_trigger`
Submit an image and receive it back with a transparent background.
