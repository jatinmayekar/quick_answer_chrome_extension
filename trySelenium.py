from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to run in headless mode (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the article
url = 'https://www.inc.com/nick-hobson/25-years-ago-steve-jobs-saved-apple-from-collapse-its-a-lesson-for-every-tech-ceo-today.html'

# Open the URL
driver.get(url)

# Wait for the page to load completely (you may need to adjust the time)
driver.implicitly_wait(20)

# Locate the main article text (you need to inspect the webpage to find the correct element)
# Example using a common class name for article text
#article_element = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div > div.ArticleGrid__feedContainer__tXvv8 > div.Article__articleContent__RJnz7.np-content > article > article')  # Adjust the selector as needed
#article_element = driver.find_element(By.CSS_SELECTOR, '#mainArticleWrapper > div:nth-child(1) > div > div.ArticleGrid__feedContainer__tXvv8 > div.Article__articleContent__RJnz7.np-content > article > article > div.ModernArticleBody__cleanBodyText__m-7G0.article-body > div:nth-child(3)')  # Adjust the selector as needed
article_element = driver.find_elements(By.XPATH, '//*[@id="mainArticleWrapper"]/div[1]/div/div[3]/div[2]/article/article/div[2]/div[1]/p')  # Adjust the selector as needed

# Extract the text
#article_text = article_element

for value in article_element:
    print(value.text)

# Print the article text
#print(article_text.getText())

# Close the WebDriver
driver.quit()

# #mainArticleWrapper > div:nth-child(1) > div > div.ArticleGrid__feedContainer__tXvv8 > div.Article__articleContent__RJnz7.np-content > article > article > div.ModernArticleBody__cleanBodyText__m-7G0.article-body
#<div class="ModernArticleBody__cleanBodyText__m-7G0 article-body"><div class="standardText"><p dir="ltr">When Steve Jobs resigned from Apple in 1985, no one would have guessed he would eventually be known as a as once-in-a-lifetime business magnate.</p></div><div class="d-md-none mobile_insert mobile_insert_2"><div><div id="in_content_6597130525" class="adElement AdContainer__adContainer__LBZiO  " data-ad_slot_type="in_content" data-page="1" data-instance="1" data-slot_base_id="in_content_1_1" data-refresh_count="1"></div></div></div><div class="standardText"><p dir="ltr">Following Jobs' departure, Apple's 55 percent&nbsp;profit margin on its desktop publishing products came crashing down when&nbsp;IBM began offering PC computers with similar functionality at a much lower price point, and with Microsoft dominating the market share.&nbsp;</p></div><div class="standardText"><p dir="ltr">When Jobs came back as interim CEO, in 1997,&nbsp;he was faced with the task of making Apple profitable again. What he did is nothing short of amazing: the company went from losing $1.04 billion to turning a $309 million profit a year later. Jobs saved the company and set the course for decades of innovation.&nbsp;This is how he did it.</p></div><div id="native_mid_article"><div id="native_mid_article_5579105960" class="adElement AdContainer__adContainer__LBZiO AdContainer__native_mid_article__R3mjx " data-ad_slot_type="native_mid_article" data-page="1" data-instance="1" data-slot_base_id="native_mid_article_1_1" data-refresh_count="1"></div></div><div class="standardText"><h2>Focus on core products</h2></div><div><div id="outstream_5372620749" class="adElement AdContainer__adContainer__LBZiO AdContainer__outstream__vvu7p " data-ad_slot_type="outstream" data-page="1" data-instance="1" data-slot_base_id="outstream_1_1" data-refresh_count="1"></div></div><div class="standardText"><p>Jobs realized Apple had strayed too far from its core mission of offering personal computers. He streamlined the product line and focused on producing just four total products, two desktop computers and two portable devices, with one set marketed for professionals and the other for consumers. During a recession, companies should similarly focus&nbsp;on their core competencies and the products or services that are most essential to their customers.</p></div><div class="standardText"><h2 dir="ltr">Be courageous in your stance</h2></div><div class="standardText"><p dir="ltr">Jobs was not afraid to make difficult decisions, such as canceling 70 percent&nbsp;of the company's product line and downsizing the management team. During a recession, companies may need to make tough decisions about layoffs, budget cuts, or other cost-saving measures. While these decisions can be painful, they may ultimately be necessary for the long-term health of the company.</p></div><div class="d-md-none mobile_insert mobile_insert_8"><div><div id="break_1253987539" class="adElement AdContainer__adContainer__LBZiO  " data-ad_slot_type="break" data-page="1" data-instance="2" data-slot_base_id="break_1_2" data-refresh_count="1"></div></div></div><div class="standardText"><p dir="ltr">Importantly, you need to ensure that you're explaining how and why the difficult decisions are tied to the&nbsp;success of the company and brand long-term.&nbsp;</p></div><div class="standardText"><h2 dir="ltr">Collaborate with rivals</h2></div><div class="standardText"><p dir="ltr">Jobs formed a partnership with Microsoft, a longtime rival of Apple, to secure a cash flow injection and solidify Microsoft's commitment to developing software for the Macintosh computer. During a recession, companies may benefit from seeking out unlikely partnerships or collaborations with competitors or other industry players to find new sources of revenue or support.</p></div><div class="standardText"><p dir="ltr">This is more true today than it was 25 years ago. The ecosystem approach to business opens doors for companies to collaborate with one another.</p></div><div class="standardText"><h2 dir="ltr">Prioritize the customer experience</h2></div><div class="standardText"><p>Jobs understood that Apple's commitment to offering the best products would be undercut if short-term profit and cost targets were the sole criteria for success. He helped to free up leaders' precious time and orient everyone toward the same shared success: building something the customer would love.</p></div><div class="d-md-none mobile_insert mobile_insert_14"><div><div id="break_8756300187" class="adElement AdContainer__adContainer__LBZiO  " data-ad_slot_type="break" data-page="1" data-instance="3" data-slot_base_id="break_1_3" data-refresh_count="1"></div></div></div><div class="standardText"><p dir="ltr">By creating one P&amp;L statement for the entire company and eliminating in-fighting among divisions, Jobs ensured that Apple's leaders could focus on what was best for the products and the consumers. During a recession, companies should prioritize the customer experience and seek to meet their needs and expectations, even if it means making short-term sacrifices for long-term gains.</p></div><div class="standardText"><h2 dir="ltr">Rally the troops</h2></div><div class="standardText"><p>When Jobs came in, there were multiple business lines at Apple, each with its own P&amp;L statement and strategy. By having every business unit report to one P&amp;L statement, Jobs eliminated the need for managers to compete with one another for resources and profitability.&nbsp;</p></div><div class="standardText lastItem"><p>This allowed Apple's leaders to focus on the overall financial health of the company, rather than being bogged down by infighting among divisions. With each manager concerned only with their own respective units showing a profit, regardless of the overall health of the company, Jobs' approach eliminated the silos that had been created, and encouraged cross-functional collaboration. This created a more cohesive company culture, ultimately leading to better decision&nbsp;making and a stronger focus on the company's core values and goals.</p></div></div>
