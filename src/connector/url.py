import os
from playwright.async_api import async_playwright
from src.configuration.configuration import url, USER_AGENT
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

connect_str = os.getenv('connect_str')

# Function to upload a file to Azure Blob Storage
def upload_to_blob(file_path, blob_name):
    try:
        # Initialize a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        
        # Get a client to interact with the container
        container_client = blob_service_client.get_container_client("ndb-screenshot-page")
        
        # Create the container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()

        # Upload the file
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        print(f"Uploaded {blob_name} to Azure Blob Storage.")
    
    except Exception as e:
        print(f"Failed to upload to Blob Storage: {e}")

async def fetch_url():
    try:
        async with async_playwright() as p:
            # Launch browser in headless mode
            browser = await p.firefox.launch(headless=True)
            
            # Create a new browser context with user-agent
            context = await browser.new_context(user_agent=USER_AGENT)
            
            # Create a new page within this context
            page = await context.new_page()

            # Navigate to the URL
            await page.goto(url, timeout=100000)

            # Save screenshot locally first
            screenshot_path = "debug_screenshot.png"

            # Upload screenshot to Azure Blob Storage
            blob_name = "screenshots/debug_screenshot.png"  # You can set the name dynamically
            upload_to_blob(screenshot_path, blob_name)
            
            # Get the content of the page
            content = await page.content()

            # Close the browser
            await browser.close()

            return content

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Write the content to a file
# def write_content_to_html_file(content):

#     OUTPUT_HTML ="data/html/NDB_Exchange_Rates.html"

#     with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
#         f.write(content)

# if __name__ == '__main__':
#     try:
#         content = asyncio.run(fetch_url())
#         write_content_to_html_file(content)
#     except Exception as e:
#         print(f"An error occurred: {e}")
