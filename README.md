<h1> challenge-collecting-data ImmoEliza</h1>

<h2> Date of project</h2>
<i>26/06/2023-30/06/2023</i>
<h2>Project</h2>
A fictional real estate company "ImmoEliza" wants to create a Machine Learning model to make price predictions on real estate sales in Belgium.
Herein, a dataset would need to be created to gather information about at least 10.000 properties all over Belgium. This dataset will later be used as a training set for the prediction model.

<h2>Data Collection and Scraping</h2>
We focused on scraping the data from "Immoweb", a highly utilised real estate platform in Belgium to list new available property.
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
<li>Time</li>

<h2>Criteria</h2>
| Criteria       | Indicator                                  | Yes/No   |
| -------------- | ------------------------------------------ | ------   |
| 1. Is complete | Contains a minimum of 10,000 inputs.       | [yes]    |
|                | Contains data for all of Belgium.          | [yes]    |
|                | No empty row present in the dataset.       | [no]     |
|                | Non-numeric values have been minimized.    | [yes]    |
| 2. Is great    | Used threading to speed up the collection. | [yes]    |

<h2>Personal situation</h2>
- Repository        :   `challenge-collecting-data`
- Type of Challenge :   `Consolidation`
- Team Challenge    :   `Group`
- Team Members      :   `Fré Van Oers`
                        `Jonathan_Rab`
                        `Mythili`