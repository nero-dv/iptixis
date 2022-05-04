# iptixis
Simple Apache Log IP Statistics Printed To stdout


<div align="center">
<h3 align="center">iptixis</h3>

  <p align="center">
    Simple Apache log IP statistics printed to <b>stdout</b>
    <br />
    <a href="https://github.com/nero-dv/iptixis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nero-dv/iptixis">View Demo</a>
    ·
    <a href="https://github.com/nero-dv/iptixis/issues">Report Bug</a>
    ·
    <a href="https://github.com/nero-dv/iptixis/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With Python 3.10</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br>
<br>


<!-- ABOUT THE PROJECT -->
## About The Project

This script will parse the apache access log for IPs that have attempted to reach your server. At the time of this commit, the program is rudimentary and exhibits functionality that seems trivial, but can be extended for further dataset gathering. There are a few vectors of information that can be gathered from the apache access log, namely browser header information, and HTTP status codes associated with the request being made. 
<br><br><!--eeeeeeee-->
This script can run on almost any server that runs Python 3.7+. The standard apache access log location is /var/log/apache2/access.log, but this may be different depending on your configuration. This script has been tested with Apache 2.4.53


<!-- GETTING STARTED -->
## Getting Started

### Installation

<!--gh repo clone nero-dv/iptixis && \ <br>
sudo chmod A+X iptixis/main.py && \ <br> 
sudo ./main.py--!>


<!-- ROADMAP -->
## Roadmap

- [ ] Further classification of data
- [ ] Redis/Kafka/MinIO pipeline
- [ ] AbuseIPDB integration
- [ ] Request header classification and CVE cross references for threat level insight
- [ ] GeoIP API Service Integration
- [ ] Visualizations


See the [open issues](https://github.com/nero-dv/iptixis/issues) for a full list of proposed features (and known issues).


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeFeature`)
3. Commit your Changes (`git commit -m 'Add some AwesomeFeature'`)
4. Push to the Branch (`git push origin feature/AwesomeFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@LouLousDen](https://twitter.com/LouLousDen)

Project Link: [https://github.com/nero-dv/iptixis](https://github.com/nero-dv/iptixis)

<p align="right">(<a href="#top">back to top</a>)</p>

