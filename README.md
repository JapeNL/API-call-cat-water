<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JapeNL/API-call-cat-water">
    <img src="images/water_level_perc.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Catalunya water levels download</h3>

  <p align="center">
    Ingest the current water levels of all reservoirs in Catalunya.
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started. To avoid retyping too much info, do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`, `project_license`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Water Quantity in the Dams of Catalonia Internal Basins

This dataset provides the daily historical status of the reservoirs within the Internal Basins of Catalonia. It tracks water levels, stored volumes, and the percentage capacity relative to the maximum capacity of each reservoir.

## Dataset Overview

| Attribute | Details |
| :--- | :--- |
| **Provider** | Catalan Water Agency (ACA) |
| **Category** | Environment |
| **Update Frequency** | Daily |
| **Total Rows** | 88.3K |
| **Total Columns** | 5 |

## Schema Documentation

Below are the details for each API field included in this dataset:

| Column Name | Description | API Field Name | Data Type |
| :--- | :--- | :--- | :--- |
| **Day** | Date the measurement was taken | `day` | Floating timestamp |
| **Station** | Reservoir where the measurement was taken | `station` | Text |
| **Absolute level (msnm)** | Water level (msnm) measured in the reservoir | `absolute_level` | Number |
| **Percentage of volume stored (%)** | Percentage of water volume in relation to the maximum capacity of the reservoir | `reservoir_volume_percentage` | Number |
| **Reservoir volume (hm3)** | Volume of water (hm3) to which the measured level corresponds | `reservoir_volume` | Number |

## Tags
`reservoirs`, `level`, `msnm`, `volume`, `hm3`, `percentage`, `ods6_clean water and sanitation`, `ods13_climate action`, `ods12_responsible production and consumption`

### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
