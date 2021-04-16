# [mtaa](https://pypi.org/project/mtaa)

[![Downloads](https://pepy.tech/badge/mtaa)](https://pepy.tech/project/mtaa)
[![Downloads](https://pepy.tech/badge/mtaa/month)](https://pepy.tech/project/mtaa)
[![Downloads](https://pepy.tech/badge/mtaa/week)](https://pepy.tech/project/mtaa)

A package consisting of all Tanzania locations from region to streets in a easy accessible way made by [kalebu](https://github.com/kalebu)

[![Become a patron](pictures/become_a_patron_button.png)](https://www.patreon.com/kalebujordan)

Intro
-------
Mtaa package is result of organized **json** of all the locations in Tanzania, As I was looking for data about these locations data I came across repo [tanzania-location-db](https://github.com/HackEAC/tanzania-locations-db), It consists of locations data organized into *regions*, whereby each region has its own csv file. So I wrote a script to transform all the locations from csv into a single **Json** and from there package came.

Json Transformer
------------------

If you wanna give a look at the script or interested about building your Json from a similar kind of raw data here is [Json Transformer script](https://github.com/Kalebu/mtaa/blob/main/json_transformer.py). 


Installation 
------------------

Use pip to install it just as shown below 

```bash

pip install mtaa

```

Usage 
-----------
The library is very straight forward, at the very top of the library is country which is tanzania and at the very bottoms are places in a given street, here is a sample

```python
>>> from mtaa import tanzania

>>> tanzania
['Shinyanga', 'Mara', 'Dar-es-salaam', 'Kilimanjaro', 'Kagera', 'Tanga', 'Mwanza', 'Tabora', 'Kigoma', 'Pwani', 'Ruvuma', 'Mtwara', 'Morogoro', 'Rukwa', 'Katavi', 'Simiyu', 'Geita', 'Arusha', 'Iringa', 'Mbeya', 'Njombe', 'Manyara', 'Lindi', 'Singida', 'Songwe', 'Dodoma']

>>> tanzania.Mbeya.districts
['Mbeya cbd', 'Mbeya', 'Rungwe', 'Mbarali', 'Kyela', 'Chunya]
 
 
>>> tanzania.Mbeya.districts.Rungwe.wards
['ward_post_code', 'Bulyaga', 'Bagamoyo', 'Makandana', 'Msasani', 'Kawetele', 'Itagata', 'Ibigi', 'Kyimo', 'Suma', 'Masoko', 'Mpuguso', 'Malindo', 'Lufingo', 'Kiwira', 'Nkunga', 'Ikuti', 'Kisondela', 'Ilima', 'Bujela', 'Masukulu', 'Kisiba', 'Kabula', 'Lupata', 'Kambasegela', 'Kisegese', 'Itete', 'Lufilyo', 'Lwangwa', 'Mpombo', 'Isange', 'Kandete', 'Luteba', 'Isongole', 'Kinyala', 'Matwebe', 'Masebe', 'Swaya', 'Iponjola', 'Lupepo', 'Ndanto', 'Ntaba', 'Mpata']

```

Fetching the whole tree
-------------------------
Lets you want to extract no just names in a ward but the whole ward and its deeper roots, to do this use the tree method at any given instance with exception of places in streets which are just list 

Here an example (Some places in Tanzania)

```python
>>> home = tanzania.Mbeya.districts.Rungwe.wards.Kiwira.tree()
>>> print(home)
{'ward_post_code': '53515', 'streets': {'Mpandapanda': ['Ipoma', 'Kiwira kati', 'Mpandapanda', 'Ilongoboto', 'Isange'], 'Kikota': ['Lukwego', 'Lubwe', "Kang'eng'e", 'Ilamba', 'Kikota', 'Ipande'], 'Ibula': ['Kibumbe', 'Ibula', 'Kanyegele', 'Sanu - salala kalongo', 'Katela'], 'Ilundo': ['Bujinga', 'Ibagha a', 'Buswema', 'Ibagha b', 'Kanyambala', 'Lusungo'], 'Ilolo': ['Ibigi', 'Ilolo', 'Itekele', 'Masebe', 'Masugwa', 'Kisungu']}}

```

From other languages ?
---------------------

Incase you're from other languages than Python you might wanna take a look at an [MtaaAPI](https://github.com/HackEAC/mtaaAPI) developed by [HackEAC](https://github.com/HackEAC). 



 Give it a star 
 ---------------

If you found this repository useful, give it a star 

You can also keep in touch with me on [Twitter](https://twitter.com/j_kalebu).


Bug bounty?
-----------------

If you encounter **issue** with the usage of the package, feel free raise an **issue** so as 
we can fix it as soon as possible(ASAP) or just reach me directly through my [email](isaackeinstein@gmail.com)


Pull Requests
------------------
If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible


Credits
------------
All the credits to 
- [kalebu](github.com/kalebu)
- [HackEAC](https://github.com/HackEAC/tanzania-locations-db)


Disclaimer !!!
------------
All the location I used to build this repository, I got from an public repository titled [tanzania-locations-db](https://github.com/HackEAC/tanzania-locations-db), 
I'm not responsible for any kind of misinformation in it, I tried to locate my home with it found its pretty accurate, so use it to your own risk
