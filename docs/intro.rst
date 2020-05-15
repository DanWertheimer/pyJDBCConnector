Introduction
============

``pyJDBCConnector`` is a high level JDBC connection API that was designed to provide a further abstraction for jdbc connections in python.
This package is designed as an introduction to jdbc connections in Python and as such provides much less customizability with a focus on
accessibility.

Motivation
==========
This package came about due to intricacies of dealing with the Denodo JDBC driver with SSL enabled.
The ``jaydebeapi`` package that this package is heavily reliant on doesn't provide the ability to specify
the location of a Trust Store file at JVM start-up. This was a big problem for us and we needed to solve this
for analysts with less engineering experience and enable them to get an introduction to Python programming
with familiar data.

Limitations
===========
- Currently this package has only been tested for the Denodo JDBC driver