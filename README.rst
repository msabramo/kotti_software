==============
kotti_software
==============

This is an extension to the Kotti CMS that adds a system for presenting
software projects on your site.

kotti_software started as a copy of kotti_blog.

`Find out more about Kotti`_

Setting up kotti_software
=========================

This Addon adds two new Content Types to your Kotti site.
To set up the content types add ``kotti_software.kotti_configure``
to the ``kotti.configurators`` setting in your ini file::

    kotti.configurators = kotti_software.kotti_configure

Now you can create a software collection and add software projects.

There are different settings to adjust the behavior of the
software.

You can select if the software projects in the collection overview
should be batched. If you set 
``kotti_software.collection_settings.use_batching`` to ``true``
(the default value) the software projects will be shown on separate
pages. If you set it to ``false`` all software projects are shown
all together on one page::

    kotti_software.collection_settings.use_batching = false

If you use batching you can choose how many software projects are
shown on one page. The default value for 
``kotti_software.collection_settings.pagesize`` is 5::

    kotti_software.collection_settings.pagesize = 10

You can use auto batching where the next page of the software projects
is automatically loaded when scrolling down the overview page instead
of showing links to switch the pages. The default for
``kotti_software.collection_settings.use_auto_batching`` is ``true``::

    kotti_software.collection_settings.use_auto_batching = false

With ``kotti_software.collection_settings.link_headline_overview`` you
can control whether the headline of a software project in the
collection overview is linked to the software project or not. This
setting defaults to ``true``::

    kotti_software.collection_settings.link_headline_overview = false

Parts of kotti_software can be overridden with the setting
``kotti_software.asset_overrides``. Have a look to the 
`Kotti documentation about the asset_overrides setting`_, which is the
same as in ``kotti_software``.

Be warned: This addon is in alpha state. Use it at your own risk.

Using kotti_software
====================

Add a software collection to your site, then to that add software projects.
For software projects, you can provide a date, which you will need to
manually keep up to date. Or, you can provide a json_url instead of a date
and the last-updated date for the project, along with main urls, will be
gathered from a JSON source. Here are ways to enter software projects:

    1) Enter the JSON url only (normal JSON-fetched)

    2) Enter the date and any of: home_page, docs_url,
       package_url, bugtrack_url (Manual entry)

    3) Enter the date only (bare-bones entry, with just date and
       title, and whatever is in body -- useful for defunct
       projects)

For the JSON data, if your project is a Python project and it has been posted
to pypi.python.org, you can enter the JSON url for that, as described below.
Otherwise, make your own JSON file, using the following format, and post it
somewhere, then enter that URL.

::

    {
        "info": {
            "docs_url": "http://packages.python.org/Kotti", 
            "package_url": "http://pypi.python.org/pypi/Kotti", 
            "bugtrack_url": "", 
            "home_page": "http://kotti.pylonsproject.org"
        }, 
        "urls": [ { "upload_time": "2012-08-30T11:59:58", } ]
    }

The urls are key/value pairs within "info", and may be empty, as shown. The
data structure for upload_time looks unnecessarily complicated, but it is
this way because we follow the pypi JSON structure. kotti_software is written
for use on the Kotti website, and thus mainly presents Python projects that
are posted on pypi. Also, kotti_software is used by Kotti developers on their
personal websites, and they tend to have Python projects. However, any type of
project can be posted of course, for javascript, Ruby, etc. Just follow the
format above for creating a custom JSON data structure for each project.

If you need to customize kotti_software itself, the urls are accessed as
json_obj['info']['docs_url'], and the upload_time is accessed as
json_obj['urls'][0]['upload_time'].

**Instructions for common JSON sources:**

pypi
----

Enter the url of the form "http://pypi.python.org/pypi/{project name}/json",
where {project name} is the case-sensitive name of the project on pypi. For
example, for Kotti the url is "http://pypi.python.org/pypi/Kotti/json".

See http://pypi.python.org/pypi/Kotti/json to see the JSON that is parsed.

github
------

As an alternative to pypi, if your project is not posted there, you may put
a JSON file somewhere in your github repo, and access it with the raw url, as:

json_url = "https://raw.github.com/geojeff/kotti_fruits_example/master/json"

As described above, you will need to follow the format of the pypi JSON data.

bitbucket
---------

[TODO] One possibility is to get the tags via the REST API, with something
like:

json_url = https://api.bitbucket.org/1.0/repositories/pypy/pypy/tags"

and in the kotti_software code:

json_raw = urllib2.urlopen(json_url).read()

... code to try for update_time in JSON

if not update_time_found:
    json_obj = json.loads(json_raw)
    json_obj['tip']['utctimestamp']

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _Kotti documentation about the asset_overrides setting: http://kotti.readthedocs.org/en/latest/configuration.html?highlight=asset#adjust-the-look-feel-kotti-asset-overrides
