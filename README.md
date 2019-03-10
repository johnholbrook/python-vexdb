# python-vexdb
A thin python wrapper for the VexDB API.

## Installation
NOTE: python-vexdb is only compatible with Python 3!

Install with pip: `pip install vexdb`.

Then, `import vexdb` to get access to the functions in the package.

python-vexdb requires the `urllib` and `json` modules, both of which should have come with your version of python.


## Functions
python-vexdb provides two functions for each of the data types listed at https://vexdb.io/the_data, where `DataType`
is one of `Events`, `Teams`, `Matches`, `Rankings`, `SeasonRankings`, `Awards`, or `Skills`:

- `getDataType` - Returns a list of dictionaries, each corresponding to a single result matching the criteria provided
as function parameters.
- `getNumDataType` - Returns the number of results matching the criteria provided as function parameters.

For each type of data, the `getDataType` and `getNumDataType` functions have a parameter for all of the parameters listed
on the corresponding page at https://vexdb.io/the_data, except for `limit_start`, `limit_number`, and `nodata`.
All parameters are optional, and more information about each parameter can be found on the vexdb API web page for each
data type.

`getDataType` functions also have a boolean parameter `get_all`, which, when set to `True`, will make multiple API calls
to ensure that it returns all matching results, since the API may not return all results for queries with a large number
(more than a few thousand) matches. The default value of `get_all` is `False`, and passing `get_all=True` is only
necessary for queries with a large number of expected results.

## Example Calls
Return a list of all matches played by team 8768A during the 2017-2018 season:
` vexdb.getMatches(team="8768A", season="In The Zone")`

Find all awards given so far in the current season:
`vexdb.getAwards(season="current")`

Find every High School VRC team in the USA: 
`vexdb.getTeams(grade="High School", country="United States", get_all=True)`
(note use of `get_all=True` since this will return a large number of results)

For more in-depth examples, see the example_scripts directory.

## Help Text
To list every included function, run `help(vexdb)`, the output of which is reproduced below:

```
NAME
    vexdb - Thin python wrapper for the VexDB API

FILE
    /Users/john/Library/Python/2.7/lib/python/site-packages/vexdb.py

FUNCTIONS
    getAwards(sku=None, name=None, team=None, season=None, get_all=False)
        Return a list of awards matching the given criteria.

        For sets of criteria that match a large number of awards (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching awards are returned by making
        multiple requests if necessary.

    getEvents(sku=None, program=None, date=None, season=None, city=None, region=None, country=None, team=None, status=None, get_all=False)
        Return a list of events matching the given criteria.

        For sets of criteria that match a large number of events (a few thousand or so),
        a single request to the API will return only a limited number of events.
        Passing get_all=True will ensure that all matching events are returned by making
        multiple requests if necessary.

    getMatches(sku=None, division=None, round=None, instance=None, matchnum=None, scheduled=None, field=None, team=None, scored=None, season=None, get_all=False)
        Return a list of matches matching the given criteria.

        For sets of criteria that match a large number of matches (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching matches are returned by making
        multiple requests if necessary.

    getNumAwards(sku=None, name=None, team=None, season=None)
        Return the number of season rankings matching the given criteria

    getNumEvents(sku=None, program=None, date=None, season=None, city=None, region=None, country=None, team=None, status=None)
        Return the number of events matching the given criteria.

    getNumMatches(sku=None, division=None, round=None, instance=None, matchnum=None, scheduled=None, field=None, team=None, scored=None, season=None)
        Return the number of matches matching the given criteria

    getNumRankings(sku=None, division=None, rank=None, team=None, season=None)
        Return the number of rankings matching the given criteria

    getNumSeasonRankings(program=None, season=None, team=None, vrating_rank=None)
        Return the number of season rankings matching the given criteria

    getNumSkills(sku=None, program=None, type=None, team=None, season=None, season_rank=None, rank=None)
        Return the number of skills records matching the given criteria

    getNumTeams(team=None, program=None, organisation=None, city=None, region=None, country=None, grade=None, is_registered=None, sku=None)
        Return the number of teams matching the given criteria

    getRankings(sku=None, division=None, rank=None, team=None, season=None, get_all=False)
        Return a list of rankings matching the given criteria.

        For sets of criteria that match a large number of rankings (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching rankings are returned by making
        multiple requests if necessary.

    getSeasonRankings(program=None, season=None, team=None, vrating_rank=None, get_all=False)
        Return a list of season rankings matching the given criteria.

        For sets of criteria that match a large number of season rankings (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching season rankings are returned by making
        multiple requests if necessary.

    getSkills(sku=None, program=None, type=None, team=None, season=None, season_rank=None, rank=None, get_all=False)
        Return a list of skills records matching the given criteria.

        For sets of criteria that match a large number of skills records (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching skills records are returned by making
        multiple requests if necessary.

    getTeams(team=None, program=None, organisation=None, city=None, region=None, country=None, grade=None, is_registered=None, sku=None, get_all=False)
        Return a list of teams matching the given criteria.

        For sets of criteria that match a large number of teams (a few thousand or so),
        a single request to the API will return only a limited number of results.
        Passing get_all=True will ensure that all matching teams are returned by making
        multiple requests if necessary.

    urlToJSON(url)
        Makes a request to the specfied URL and returns a list of results.

    urlToSize(url)
        Makes a request to the specfied URL and returns the number of results.

        Useful mostly when making calls with the 'nodata' perameter set to true.
```
