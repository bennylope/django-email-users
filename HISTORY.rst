.. :changelog:

History
-------

1.1.0 (2017-07-11)
++++++++++++++++++

* Updated password change form link for User's ModelAdmin class

1.0.0 (2016-04-21)
++++++++++++++++++

* Remove `User.title` field (POTENTIALLY BREAKING). This field should not have
  been added(!). If you're using this field you shouldn't upgrade!
* Squashed migrations (POTENTIALLY BREAKING). If you're using 0.4.0 or an older
  version and want to upgrade, consider faking the migration to 0001 and then
  removing the `title` field. As long as you're using 0.4.0 the `title` field
  is nullable, however.
* Drop support for Django 1.6, 1.7
* Add support for Django 1.9
* Add support for Python 3.5

0.4.0 (2015-04-15)
++++++++++++++++++

* Update Django migrations to reflect field changes for base user model

0.3.0 (2015-04-10)
++++++++++++++++++

* Support Django 1.8

0.1.1 (2014-11-24)
++++++++++++++++++

* Adds a get_username method to User model

0.1.0 (2014-08-15)
++++++++++++++++++

* First release on PyPI.
