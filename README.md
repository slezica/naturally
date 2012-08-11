# naturally

A 60-line library that makes you feel as if XML documents were just _made of_ Python

## Example 
Let's say we have this rather unoriginal XML document:
```xml
<?xml version="1.0"?>
<catalog version="2.1">
    <book id="1"
          title="The Divine Comedy"
          author="Danti Alighieri">
          
          <edition date="2002-10" language="italian" />
          <edition date="2003-05" language="english" />
          
          <description>
              An epic poem that describes Dante's travels through Hell, Purgatory, and Heaven
          </description>
      </book>
      
    <book id="2"
          title="The Stranger"
          author="Albert Camus"
          date="1942">
          
          <edition date="2007-04" language="french"  />
          <edition date="2010-03" language="spanish" />
          
          <description>
            The story of Meursault, an Algerian who seemingly irrationally kills an Arab man whom he recognises in French Algiers.
          </description>
      </book>
</catalog>
```

## Reading XML
To tinker with `naturally`, you can fire the `demo.py` script.
```
$ python demo.py
```

This will land you into an interactive shell with the first command already ran for you:
```python
>>> catalog = naturally.xml('demo.xml')
>>>
```

Now, XML documents are _naturally_ represented as python objects acting as both a dictionary of their attributes, and a container for their children. 
```python
>>> catalog['version']
'2.1'
>>> catalog.book[0]['id']
'1'
```

In JQuery-style, nodes and sequences of nodes are handled in a mostly transparent manner.
```python
>>> catalog.book['id']
['1', '2']
```

Filtering is _naturally_ easy as well. Using the `()` operator, you can demand presence or specific values of attributes.
```python
>>> catalog.book('date')['title']
'The Stranger'
>>> catalog.book(id='1')['author']
'Danti Alighieri'
```

Since the object's namespace is enterily dedicated to represent the underlying XML document, you can't access some of the data directly. Instead, call the object as if using an empty filter: this will give you the underlying Element nodes, properly represented. 

```python
>>> catalog.book.description()
[<Element 'description' at 0x235e350>, <Element 'description' at 0x235e4d0>]
>>> catalog.book(id='1').description().text.strip()
"An epic poem that describes Dante's travels through Hell, Purgatory, and Heaven"
```

Feels natural, right?

# Writing XML
I have not yet implemented XML creation, but I intend to heavily use [autovivification](http://en.wikipedia.org/wiki/Autovivification) to make it as dead simple as reading.
