<h1> challenge-collecting-data ImmoEliza</h1>

<h2> Date of project</h2>
<i>26/06/2023-30/06/2023</i>
<h2>Project</h2>
A fictional real estate company "ImmoEliza" wants to create a Machine Learning model to make price predictions on real estate sales in Belgium.
Herein, a dataset would need to be created to gather information about at least 10.000 properties all over Belgium. This dataset will later be used as a training set for the prediction model.

<h2>Data Collection and Scraping</h2>
We focused on scraping the data from ["Immoweb"](https://linkedin.com/in/mythili-palanisamy-492147159), a highly utilised real estate platform in Belgium to list new available property.
We had gathered data concerning:
<li>Price</li>
<li>Address</li>
<li>Building Condition</li>
<li>Construction Year</li>
<li>Bedrooms</li>
<li>Terrace (surface)</li>
<li>Shower rooms</li>
<li>Office</li>
<li>Toilets</li>
<li>Energy Class</li>
<li>Type of Kitchen</li>
<li>Furnished</li>
<li>Parking Space</li>
<li>Garden Area</li>

<h2>Installation</h2>
To run the code, you will need to install/import the following:
<li>Requests</li>
<li>BeautifulSoup</li>   
<li>ThreadPoolexecutor</li>
<li>Regex</li>
<li>Pandas</li>

<h2>How does it work</h2>
<li>when you run get_urls.py, it will return a txt-file which contains a bit over 10,000 urls for houses and apartments from immoweb</li>
<li>data_scrape_challenge.py opens this list, scrapes all the urls and returns them as a csv-file. Any urls which return an error are written to a file called skipped-urls.txt.



<h2>Credits</h2>
This repo was created of an AI Bootcamp organised by BeCode.org by: 
<li>[Mythili Palanisamy](https://linkedin.com/in/mythili-palanisamy-492147159)</li>
<li>[Jonathan Rabbi](https://linkedin.com/in/jonathan-rabbi)</li>
<li>[Fré Van Oers](https://linkedin.com/in/frevanoers/)</li>