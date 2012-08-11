import naturally, sys, code

catalog = naturally.xml('demo.xml')

code.interact(local = locals(),
        banner=">>> catalog = naturally.xml('demo.xml')")

sys.exit(0)

# Things you may want to try:
print catalog
print catalog.book['id']
print str(catalog.book(id='bk101').author)
print str(catalog.book.price)
