
import math
from io import BytesIO
from PIL import Image, ImageDraw
from supabase import create_client

# Supabase credentials
SUPABASE_URL = 'https://nftulfhbavdjqcqrqbwv.supabase.co'
# SUPABASE_KEY = 'sbp_3054fccf0069f110ef0a14466f14212296392889'
SUPABASE_KEY="D8DMKFRQLj/iWoDCV0a1G3mH7k9uECbaQdyYL8qdu7feiFqj2BZJ8On23BGDg3vrdHN83XxtefalOPHowCP8gQ=="

# Map settings
MAP_SIZE = (800, 600)
MAP_ZOOM = 13
MAP_TYPE = 'roadmap'

# Color and line settings
LINE_COLOR = (255, 0, 0)  # red
LINE_WIDTH = 5

def generate_map(coords):
    # Calculate map center and bounds
    latitudes = [coord[0] for coord in coords]
    longitudes = [coord[1] for coord in coords]
    center_lat = sum(latitudes) / len(coords)
    center_lon = sum(longitudes) / len(coords)
    north = max(latitudes)
    south = min(latitudes)
    east = max(longitudes)
    west = min(longitudes)

    # Calculate map image size and scale
    lat_scale = MAP_SIZE[1] / (north - south)
    lon_scale = MAP_SIZE[0] / (east - west)
    scale = min(lat_scale, lon_scale)

    # Calculate map image center and corner points
    img_center_x = int((west + east) / 2 * scale)
    img_center_y = int((north + south) / 2 * scale)
    img_corner_x = img_center_x - MAP_SIZE[0] // 2
    img_corner_y = img_center_y - MAP_SIZE[1] // 2

    # Generate map URL
    path = '|'.join([f'{coord[0]},{coord[1]}' for coord in coords])
    url = f'https://maps.googleapis.com/maps/api/staticmap?size={MAP_SIZE[0]}x{MAP_SIZE[1]}&zoom={MAP_ZOOM}&maptype={MAP_TYPE}&path=color:0x{LINE_COLOR[0]:02x}{LINE_COLOR[1]:02x}{LINE_COLOR[2]:02x}|weight:{LINE_WIDTH}|enc:{path}&key=<your-google-maps-api-key>'

    # Download map image
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGBA')

    # Create transparent overlay image
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Draw path line on overlay image
    draw = ImageDraw.Draw(overlay)
    xy = [(int((lon - west) * scale), int((north - lat) * scale)) for lat, lon in coords]
    draw.line(xy, fill=LINE_COLOR, width=LINE_WIDTH)

    # Combine map image and overlay image
    result = Image.alpha_composite(img, overlay)

    # Crop image to map bounds
    result = result.crop((img_corner_x, img_corner_y, img_corner_x + MAP_SIZE[0], img_corner_y + MAP_SIZE[1]))

    # Save image to Supabase storage
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    filename = f'map-{math.ceil(north)},{math.ceil(south)},{math.ceil(east)},{math.ceil(west)}.png'
    _, error
