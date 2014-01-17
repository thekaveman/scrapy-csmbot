# Scrapy settings for csmbot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'csmbot'

SPIDER_MODULES = ['csmbot.spiders']
NEWSPIDER_MODULE = 'csmbot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'csmbot (+http://www.yourdomain.com)'