# openSkyNetwork-FlightTracker

[The OpenSky Network](https://opensky-network.org/) is a community-based receiver network which continuously collects air traffic surveillance data. Unlike other systems, OpenSky keeps the collected data forever and makes it available to researchers from different fields. With more than 200 billion ADS-B and Mode S messages collected so far, the OpenSky Network exhibits the largest air traffic surveillance dataset of its kind in the world.
This flight tracker allows you to find the current flights, by country.

## Installation

Dependencies: [OpenSky Network API](https://github.com/openskynetwork/opensky-api)
```
sudo python setup.py install
```

## Usage

From the command line:
```
python flightTracker.py
```
Output: List of all of the countries in which the OpenSky Network can find aircraft.

```
python flightTracker.py -c China
```
Output: Details of every aircraft whose origin country is China


## Contributing
Fork/Submit a pull request

## License
MIT License

Copyright (c) [2016] [Sujit Shivaprasad]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
