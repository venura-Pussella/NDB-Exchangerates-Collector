from playwright.async_api import async_playwright
from src.configuration.configuration import url, USER_AGENT

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
            await page.goto(url, timeout=40000)
            
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


