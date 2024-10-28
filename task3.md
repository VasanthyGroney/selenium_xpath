# XPath Expressions

## 1. XPath to locate the main h1 element
```xpath
//h1[@id='mainTitle']

##  2. XPath to select the About Us navigational link
```xpath
//a[text()='About Us']
//ul[@class='dropdown']//a[text()='Graphic Design']
//div[@class='service-item'][h3[text()='SEO Services']]/p
//section[@id='services']//div[@class='service-item']
//form[@id='contactForm']//input[@type='email']
//form[@id='contactForm']
//footer//p
//section[@id='services']//div[@class='service-item']
//form[@id='contactForm']
//footer//p
//div[@class='team']//li[1]//h4
//section[@id='contact']//h2
//li[a[@href='#services']]//ul[@class='dropdown']//a
//div[@class='team']//li[1]
//form[@id='contactForm']//input[@type='submit']

