# Katy OBD
A dialog-based on-board diagnositcs parsing tools.

***Chuan Yang*** (<yangc@sj-hospital.org>)

[![Windows Build status](https://img.shields.io/badge/Windows-passing-brightgreen.svg)](https://github.com/YangChuan80/KatyOBD)
[![MIT license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE)
[![Dowloads](https://img.shields.io/badge/downloads-6M-green.svg)](https://github.com/YangChuan80/WillowbendDICOM/raw/master/Installer/WillowbendDICOM_Installer.exe?raw=true)
[![Medicine Application](https://img.shields.io/badge/application-medicine-red.svg)](README.md)
[![Home](https://img.shields.io/badge/GitHub-home-ff69b4.svg)](https://github.com/YangChuan80)

## Introduction
**Biobanks** are increasingly playing an important role in biotechnology, pharmaceutical and medical research. The ability to manage an ever-increasing number of biosamples (blood, tissue, DNA etc.) and to comply with the regulatory requirements, such as HTA, GCLP, MHRA, FDA 21  CFR Part 11 and other similar requirements, is a high priority for all organisations working in this area.  

**Vehicle On Board Diagnostics Systems** are frequently built from **Laboratory Information Management Systems (LIMS)**, but need to be configured to deliver a solution that meets the specific requirements in a clearly understandable way. Biobanks can handle a wide range of sample types. In addition to the more traditional collections of human tissues biobanks, there are also collections of animal tissues or botanical samples.

***Katy OBD*** is a dialog-based application performing the parser of data from ECU (Electronic Control Unit) installed in cars.

[![Charleston Park's GUI](CharlestonPark_Interface.jpg)](README.md)

## Installation from Binaries
- Download **[CharlestonPark_Installer.exe](https://github.com/YangChuan80/CharlestonPark/blob/master/CharlestonPark_Installer.exe?raw=true)** file from **[here](https://github.com/YangChuan80/CharlestonPark/blob/master/CharlestonPark_Installer.exe?raw=true)**, which is a NSIS installation file only used in Windows platform. 
- After downloading, you can install it directly. When finished, a folder with the same name have been made. Enter the folder CharlestonPark, run the **CharlestonPark.EXE** to go!
- This option is for ordinary users, who are not required to possess any knowledge of Python programming language or to have Python interpreter configured on their computers.
- CharlestonPark can also be run on Mac OSX and Linux.

## Installation from Source
This option is only adopted by Python specialist. 

After you complete the CharlestonPark.py and database files download, run it:
```
python CharlestonPark.py
```
Python interpreter has to be Python 3.4 or later.

- **Setuptools & Pyinstaler**
 - If you'd like to use **PyInstaller**, you should downgrade your **setuptools** module to **19.2**.

To perform frozen binary, do this:
```
pyinstaller CharlestonPark.py -w
```

## Instructions
- Click **Browse** button to browse the information of all samples and patients. 
- When the information lists, you can double click the row, then the detailed information will display in the lower part of the dialog. 
- If you want change the detailed information, after you edit it, you can click the **Update**. After the dialog pop up, your edited changes will update to the database.
- You also can create a new record of sample and/or patient by clicking **New Sample...** and/or **New Patient...**.
- Click **Samples...** or **Patients...** button on the right, you can browse, change and delete the information of sample and patient at one time from the database.
- Besides, the search services are available in main dialogue and **Samples...**/**Patients...** dialogue. ***Charleston Park*** provide patient name search, in-patient ID search and sample ID search options to let you to query the database. 

## License
The MIT License (MIT)

Copyright (c) 2017 Chuan Yang

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
