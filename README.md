# [mtaa](https://pypi.org/project/mtaa)

[![Downloads](https://pepy.tech/badge/mtaa)](https://pepy.tech/project/mtaa)
[![Downloads](https://pepy.tech/badge/mtaa/month)](https://pepy.tech/project/mtaa)
[![Downloads](https://pepy.tech/badge/mtaa/week)](https://pepy.tech/project/mtaa)

A package consisting of all Tanzania locations from region to streets in a easy accessible way made by [kalebu](https://github.com/kalebu)

[![Become a patron](pictures/become_a_patron_button.png)](https://www.patreon.com/kalebujordan)

## A strory behind

Mtaa package is result of organized **json** of all the locations in Tanzania, As I was looking for data about these locations data I came across repo [tanzania-location-db](https://github.com/HackEAC/tanzania-locations-db), It consists of locations data organized into *regions*, whereby each region has its own csv file. So I wrote a script to transform all the locations from csv into a single **Json** and from there package came.

## Json Transformer

If you wanna give a look at the script or interested about building your Json from a similar kind of raw data here is [Json Transformer script](https://github.com/Kalebu/mtaa/blob/main/json_transformer.py). 

## Installation

Use pip to install it just as shown below;

```bash
pip install mtaa
```

## Usage 

The library is very straight forward, at the very top of the library is country which is tanzania and at the very bottoms are places in a given street, here is a sample;

```python
>>> from mtaa import tanzania

>>> tanzania
['Shinyanga', 'Mara', 'Dar-es-salaam', 'Kilimanjaro', 'Kagera', 'Tanga', 'Mwanza', 'Tabora', 'Kigoma', 'Pwani', 'Ruvuma', 'Mtwara', 'Morogoro', 'Rukwa', 'Katavi', 'Simiyu', 'Geita', 'Arusha', 'Iringa', 'Mbeya', 'Njombe', 'Manyara', 'Lindi', 'Singida', 'Songwe', 'Dodoma']

>>> tanzania.Mbeya.districts
['Mbeya cbd', 'Mbeya', 'Rungwe', 'Mbarali', 'Kyela', 'Chunya]
 
 
>>> tanzania.Mbeya.districts.Rungwe.wards
['ward_post_code', 'Bulyaga', 'Bagamoyo', 'Makandana', 'Msasani', 'Kawetele', 'Itagata', 'Ibigi', 'Kyimo', 'Suma', 'Masoko', 'Mpuguso', 'Malindo', 'Lufingo', 'Kiwira', 'Nkunga', 'Ikuti', 'Kisondela', 'Ilima', 'Bujela', 'Masukulu', 'Kisiba', 'Kabula', 'Lupata', 'Kambasegela', 'Kisegese', 'Itete', 'Lufilyo', 'Lwangwa', 'Mpombo', 'Isange', 'Kandete', 'Luteba', 'Isongole', 'Kinyala', 'Matwebe', 'Masebe', 'Swaya', 'Iponjola', 'Lupepo', 'Ndanto', 'Ntaba', 'Mpata']

```

## How about the Type?

```python
>>> from mtaa import tanzania
>>> type(tanzania)
<class 'mtaa.Tanzania'>
```

As you can see the repr() being shown on of the REPL is of type <mtaa.Tanzania>, you can easily convert it into native python datatypes due to the fact its iteratable, as shown in the example below;

```python
>>> from mtaa import tanzania
>>> list(tanzania)
['Shinyanga', 'Mara', 'Dar-es-salaam', 'Kilimanjaro', 'Kagera', 'Tanga', 'Mwanza', 'Tabora', 'Kigoma', 'Pwani', 'Ruvuma', 'Mtwara', 'Morogoro', 'Rukwa', 'Katavi', 'Simiyu', 'Geita', 'Arusha', 'Iringa', 'Mbeya', 'Njombe', 'Manyara', 'Lindi', 'Singida', 'Songwe', 'Dodoma']
```

Since its Iterable that's means you can loop through it, but as string for  Example;

```python
>>> for district in tanzania.Mbeya.districts:
...     print(district)
... 
Mbeya cbd
Mbeya
Rungwe
Mbarali
Kyela
Chunya
```

## How about Dar-es-salaam ?

In the above example we were able to retreive locations of **Mbeya** region because, Mbeya is a valid python identifier, when you try to access **Dar-es-Salaam** it will ofcourse raise you an error just as shown below;

```python
>>> from mtaa import tanzania
>>> tanzania.Dar-es-salaam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Tanzania' object has no attribute 'Dar'
```

To resolve this at anypoint where you a location name is an invalid identifier, use get_dict() instead of (.) operator to access it as shown in the example below;

```python
>>> from mtaa import tanzania 
>>> tanzania.get('Dar-es-salaam').districts
['Ilala cbd', 'Ilala', 'Kinondoni', 'Temeke', 'Ubungo', 'Kigamboni']
```

## Fetching the whole tree

Lets you want to extract no just names in a ward but the whole ward and its deeper roots, to do this use the tree () at any given instance with exception of places in streets which are just list;

Here an example (Some places in Tanzania)

```python
>>> home = tanzania.Mbeya.districts.Rungwe.wards.Kiwira.tree()
>>> print(home)
{'ward_post_code': '53515', 'streets': {'Mpandapanda': ['Ipoma', 'Kiwira kati', 'Mpandapanda', 'Ilongoboto', 'Isange'], 'Kikota': ['Lukwego', 'Lubwe', "Kang'eng'e", 'Ilamba', 'Kikota', 'Ipande'], 'Ibula': ['Kibumbe', 'Ibula', 'Kanyegele', 'Sanu - salala kalongo', 'Katela'], 'Ilundo': ['Bujinga', 'Ibagha a', 'Buswema', 'Ibagha b', 'Kanyambala', 'Lusungo'], 'Ilolo': ['Ibigi', 'Ilolo', 'Itekele', 'Masebe', 'Masugwa', 'Kisungu']}}

```

## Grouped Locations

You can also access grouped locations such as all districts, wards and street as shown below;

```python
>>> import mtaa
>>> mtaa.wards
......
>>> len(mtaa.wards)
3964
>>> mtaa.districts
......
>>> len(mtaa.districts)
158
>>>mtaa.streets
.....
>>> len(mtaa.streets)
16741
```

## From other languages ?

Incase you're from other languages than Python you might wanna take a look at these general purpose APIS

- [MtaaAPI](https://github.com/HackEAC/mtaaAPI)
- [Location-api](https://github.com/HackEAC/locations-API)

## Give it a star

If you found this repository useful, give it a star so as the whole galaxy of developer can get to know it, you can also keep in touch with me on [twitter](https://twitter.com/j_kalebu).

## Bug bounty?

If you encounter **issue** with the usage of the package, feel free raise an **issue** so as 
we can fix it as soon as possible(ASAP) or just reach me directly through email isaackeinstein(at)gmail.com.

## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible

## Disclaimer

All the location I used to build this repository, I got from an public repository titled [tanzania-locations-db](https://github.com/HackEAC/tanzania-locations-db), I'm not responsible for any kind of misinformation in it, I tried to locate my home with it found its pretty accurate, so use it to your own risk

## Credits

All the credits to ;

- [kalebu](github.com/kalebu)
- [HackEAC](https://github.com/HackEAC/tanzania-locations-db)
- Future contributors

## Related Opensource Projects

- [MtaaAPI](https://github.com/HackEAC/mtaaAPI)
- [Location-API](https://github.com/HackEAC/locations-API)
- [rgeocode](https://github.com/bentesha/rgeocode)
- [Reverse geocoder](https://github.com/Kalebu/reverse-geocoder)
- [tanzaniageodata](https://github.com/Kijacode/tanzaniageodata)
- [location-demographia](https://github.com/dbrax/location-demographia)
