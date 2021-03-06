Changelog
=========

2.2.8 (unreleased)
------------------

- Nothing changed yet.


2.2.7 (2013-08-29)
------------------

- Bugfix in statistics report view for non-ascii month names #8420
  [pysailor]
- Amended translation for "This OiRA tool was presented to you by"
  in FR #7992 [pysailor]


2.2.6 (2013-08-23)
------------------

- Register a more generic datamanger for survey. #8379 [jcbrand] 

2.2.5 (2013-08-21)
------------------

- Typo in LT translation [pysailor]
- Applied translation updates #7938 and #8190 [pysailor]
- Implement sidebar legend with translations. #7939 [jcbrand]
- Fixed wrong translations for cs and pt [pilz]
- include a script for browser warnings. This fixes OSHA ticket 7368 [pilz]
- spelling fixes in LT #8258

2.2.4 (2013-07-05)
------------------

- Fixed a typo in manual translations: help_header_report, not help_header_reports
  [pysailor]
- Minor translation fixes and updates. #7830, #7766. [jcbrand]
- Updated Flemish and Bulgarian translations #7810 [jcbrand]
- Updated Greek translations #7310, #7704 [jcbrand, pysailor]
- #7555: Czech translation fixes [regebro]
- PT translation fixed 7934 [pysailor]


2.2.3 (2013-06-03)
------------------

- Small style fix start page markup. [jcbrand]


2.2.2 (2013-06-03)
------------------

Upgrade notes
~~~~~~~~~~~~~

This release updates the profile version to *7*. Please use the upgrade feature
in ``portal_setup`` to upgrade the ``osha.oira:default`` profile to this
version.

Bugfixes
~~~~~~~~

- Bugfix. Adding a second measure causes server error.

Feature changes
~~~~~~~~~~~~~~~

- Make XLS headings bold and space columns so that headings don't wrap.
- Add another column in the action plan XLS file for the top-level profile
  question or module #7322 [jcbrand]
- Dropped support for IE8 and enable browser detection to warn users. #7368 [jcbrand]
- New translations for EL, LV #7511 [jcbrand]
- Improvement in dropdown in the survey page #7050 [jcbrand]
- Added IOSHASurvey behavior with externl site link fields, refs #5880 [reinhardt]

2.2.1 (2013-04-23)
------------------

- Added formatting to the help text that explains the use of profile questions.
- Updated Portuguese, Czech and Lithuanian translations.

2.2 (2013-04-15)
----------------

Upgrade notes
~~~~~~~~~~~~~

This release updates the profile version to *7*. Please use the upgrade feature
in ``portal_setup`` to upgrade the ``osha.oira:default`` profile to this
version.

Feature changes
~~~~~~~~~~~~~~~

- Added Hungarian translations #7091 [pysailor]
- Changed title for statistics report to re-use existing translations [pysailor]
- Include the top-level module in the downloadble action plan spreadsheet. [jcbrand]
- allow choosing file format (pdf/xls) in statistics form, refs #7169 [reinhardt]

2.1.1 March 26, 2013
--------------------

Bugfixes
~~~~~~~~

- Added class "Message" on risk_evaluation. This fixes `github ticket #93
  <https://github.com/euphorie/Euphorie/issues/94>`_.  [pysailor]


2.1 (2013-03-22)
----------------

- removed customized version of module_identification to revert back to the
  working tno version
- Fixed survey statistics to not show previews as published surveys.

2.0b9 - Match 19, 2013
----------------------

- Translation updates


2.0b8 - Match 19, 2013
----------------------

- Translation updates


2.0b7 - March 19, 2013
----------------------

Feature changes
~~~~~~~~~~~~~~~

- Added combination of action plan, prevention plan and resources into
  one cell
- Shortened translation for fr, fixes #7073

Bugfixes
~~~~~~~~

- Actions menu couldn't load when user is anonymous
- UnicodeDecodeError on statistics views


2.0b5 - March 15, 2013
----------------------

Feature changes
~~~~~~~~~~~~~~~

- Restrict statistics views to users with edit permission in the relevant
  context.


2.0b4 - March 13, 2013
----------------------


Feature changes
~~~~~~~~~~~~~~~

- Add new Spanish translation.

- Update French and Greek translation.

- deactivated legend temporarily until wording is final. This fixes #7007

- reactivated main navigation heading so that you can click back.
  This fixes #6076.

Bugfixes
~~~~~~~~

- Fix grammar for field labels in the company information form.

- Correct the navigation tree legend: the description for answered risks was
  not correct.

- Fixed IE9 navtree rendering bug.


2.0b3 - March 5, 2013
---------------------

Upgrade notes
~~~~~~~~~~~~~

This release updates the profile version to *6*. Please use the upgrade feature
in ``portal_setup`` to upgrade the ``osha.oira:default`` profile to this
version.

The minimum required Euphorie version is now *6.0b2*.

Feature changes
~~~~~~~~~~~~~~~

- Change ordering for the action plan timeline to sort on risk priority
  instead of measure start date. This fixes `ticket 87
  <https://github.com/euphorie/Euphorie/issues/87>`_.

- Add action and expertise information for measures to the timeline report.
  This fixes `ticket 85 <https://github.com/euphorie/Euphorie/issues/85>`_.

Bugfixes
~~~~~~~~

- Correct display of error messages on the risk action plan form.
- Add upgrade step to set default value for ``time`` column used for statistics.
  Fixes error upon client login under certain circumstances.
- Update HELP trnaslations for FR and EL. #5648
- Fix unicode error when adding profiles in client. #4403


2.0b2 - February 19, 2013
-------------------------

Feature changes
~~~~~~~~~~~~~~~

- Improve styling of report landing page.

Bugfixes
~~~~~~~~

- Include nuplone directory in MANIFEST.in.
- Fixed rendering of the custom homepage..


2.0b1 - February 15, 2013
-------------------------

Upgrade notes
~~~~~~~~~~~~~

osha.oira now requires Euphorie 6. Please see the `Euphorie upgrade notes
<http://euphorie.readthedocs.org/en/latest/changes.html#upgrade-notes>`_
for important upgrade information.

This release updates the profile version to *5*. Please use the upgrade feature
in ``portal_setup`` to upgrade the ``osha.oira:default`` profile to this
version.

The Euphorie configuration file (``etc/euphorie.ini`` in the standard buildout)
no longer needs to include the complete configuration. You now only need to
specify details that are specific to your deployment such as the Google Analytics
accounts and client URL.

Feature changes
~~~~~~~~~~~~~~~

- This package is now automatically tested using `Travis
  <travis-ci.org/euphorie/osha.oira>`_.

- Allow developers to use `make pot` to update the POT-file for translations.

- CSS and JavaScript is now maintained in the Euphorie package to make
  maintenance easier.

- Use a modal panel to change the title of an existing session.

- Override the action plan timeline download from Euphorie to use a subset
  of columns with a different ordering and add a new comment column.

- Replace the online view of the action plan report with a new landing page
  from where the full report can be downloaded in RTF format or a XLSX file
  with all defined measures.

- Change the user interface for profile questions: use separate questions to
  ask if a section is relevant for a user and if it can occur multiple times.


Bugfixes
~~~~~~~~

- Correct logging of client logins.
- Improve display of error messages in the client.
- Fix accidental double loading of javascript in client pages.


1.2.37 (2013-02-06)
-------------------

- Nothing changed yet.


1.2.36 (2013-02-01)
-------------------

- Nothing changed yet.


1.2.35 (2013-01-29)
-------------------

- Update report markup with changes from Prototype (add .message class)
  [jcbrand]



1.2.34 (2013-01-29)
-------------------

- Show/hide link for legal refs was white on white. [jcbrand]


1.2.33 (2013-01-22)
-------------------

- Remove "(in Euro)" for budget field #6208 [jcbrand]


1.2.32 (2013-01-22)
-------------------

- Nothing changed yet.


1.2.31 (2013-01-21)
-------------------

- Fixed LT unicode error [thomas_w]


1.2.30 (2013-01-21)
-------------------

- Fix ZCML loading in tests so we can support Plone 4.2. [wiggy]
- Shorten buttons in Greek translation #6286 [jcbrand]
- Override Survey edit form to hide "Evaluation optional" field #6175 [jcbrand]
- Integrate changes from Prototype. Fixes #6285 [jcbrand]
- Fixed homepage for mobile view on android #6342 [jcbrand]
- Reverse the order in which measures are shown #6287 [jcbrand]
- French updates on the identification page #6428 [jcbrand]
- Added FI translations #6410 [thomasw]
- Added LT translations #6257 [thomasw]

1.2.29 (2012-12-17)
-------------------

- Fixed RST error. [jcbrand]


1.2.28 (2012-12-17)
-------------------

- Comments don't appear in the report #5985 [jcbrand]
- Hide help tab #6071 [jcbrand]
- Bump jquery to 1.8.2 [jcbrand]

1.2.27. (2012-11-26)
--------------------

- Regenerate en po file. [jcbrand]
- Re-add fuzzy entries and just remove the top ones (before doc metadata) which cause unicode errors. [jcbrand]


1.2.26 (2012-11-09)
-------------------

- Removed #fuzzy marker in all po files [thomasw]


1.2.25 (2012-11-01)
-------------------

- Hide the standard solutions button when there aren't any [jcbrand]


1.2.24 (2012-11-01)
-------------------

- Include datepicker.min.css when not in debug mode [jcbrand]


1.2.23 (2012-11-01)
-------------------

- Added multilingual support to the datepicker [jcbrand]
- Datepicker CSS and images now moved to the Euphorie Prototype [jcbrand]


1.2.22 (2012-10-29)
-------------------

- fixed 2 fatal typos (for translation) in risk_actionplan :-( [thomasw]


1.2.21 (2012-10-29)
-------------------

- Added missing i18n:translate statments in risk_actionplan (copied from the
  Euphorie version) [thomasw]

1.2.20 (2012-10-29)
-------------------

- Nothing changed yet.


1.2.19 (2012-10-29)
-------------------

- Changed name for language nl-be #5978 [thomasw]

1.2.18 (2012-10-01)
-------------------

- Update webhelpers.pt from Euphorie. Load Modernizr separately. [jcbrand]


1.2.17 (2012-09-28)
-------------------

- Remove country view override. [jcbrand]


1.2.16 (2012-09-28)
-------------------

- Translation fix for "list of risks" report in FR. [jcbrand]


1.2.15 (2012-09-27)
-------------------

- Remove special char from changes.rst (breaks uploading to pypi). [jcbrand]


1.2.14 (2012-09-27)
-------------------

- Description content gets lost in report if risk not evaluated. #5660. [jcbrand]
- Translation issues on action plan page #5809. [jcbrand]
- Translations of "skip" button. #4436  [jcbrand]
- UnicodeDecodeError for sectors. #5174 [jcbrand]


1.2.13 (2012-09-04)
-------------------

- Action plan page bugfixes. [jcbrand]


1.2.12 (2012-09-04)
-------------------

- Action plan page bugfixes. [jcbrand]


1.2.11 (2012-09-03)
-------------------

- Use jquery.placeholder.js instead of superimpose. [jcbrand]

1.2.10 (2012-09-03)
-------------------

- Add modernizr.js and some markup changes from Prototype. [jcbrand]

1.2.9 (2012-08-31)
------------------

- Implemented new design for adding measure in the action plan stage. [jcbrand]


1.2.8 (2012-08-30)
------------------

- Remove header and carousel on custom homepage. #5055 [jcbrand]

1.2.7 (2012-08-28)
------------------

- Hide company form after skipped or filled in. #4436 [jcrband]
- Added Catalan (ca) translations #5463 [thomasw]
- Added Latvian (lv) translations #5075 [thomasw]

1.2.6 (2012-07-23)
------------------

- Updated Czech translations. [jcbrand]
- Only show link to custom homepage when on the English docs folder. [jcbrand]

1.2.5 (2012-07-23)
------------------

- Renabled links on questions in the sidebar. For #5187. [jcbrand]
- Implement custom homepage functionality. For #5055. [jcbrand]

1.2.4 (2012-06-28)
------------------

- Bugfix. Revert method name from unreleased htmllaundry. [jcbrand]

1.2.3 (2012-06-28)
------------------

- IE7 fixes related to the datepicker #3495. [jcbrand]

1.2.2 (2012-06-27)
------------------

- Added Czech translations. Ticket #4036. [jcbrand]
- Updated Greek translations. #4405. [jcbrand]
- Unescape HTML codes when creating RTF docs. Fixes #4395. [jcbrand]
- Hide/Move legal and policy text on evaluation and action plan steps. For #5351. [jcbrand]
- Added Flemish (Vlaams nl_BE) translation #5150 [thomasw]
- Added datepicker to the risk action plan view #3495. [jcbrand]

1.2.1
-----

- Added Bulgarian translations [thomasw]
- change devbox to client.oiraproject.eu fixes #4304 [pilz]

1.2 (2012-02-27)
----------------

- #4249: Restrict the @@contact form and hide links to it. [jcbrand]

1.1 (2012-12-17)
----------------
- #3813: Also show children of optional modules in the downloadable report. [jcbrand]
- #3536: Updated the en translations file. [jcbrand]
- AttributeError bugfix on the report.pt view. [jcbrand]

1.0 (2012-12-13)
----------------

- #3813 Adjust the Content of tools feature to display ALL risks [jcbrand]
- #3811 "Measure" text on accordion not translated. [jcbrand]
- #3792 Provide route back to Identification phase from the identification report. [jcbrand]
- #3779 Privacy not working on client and community sites [jcbrand]
- #3892 Exchange the OiRA logo in the admin part [jcbrand]
- #4071 Integrate Wichert's changes in to osha.oira [jcbrand]

0.24 (2011-10-07)
-----------------
- 3805: Added Slovenian translations. [thomas_w]

0.23 (2011-09-27)
-----------------

- 3520: Add upgrade step to renew the 'published' date of all client surveys. [jcbrand]
- 3797: Renamed travailleurs to salaries and statut to avancement. [jcbrand]
- Removed the bugfix for 2583, since a more proper bugfix is now in Euphorie [jcbrand]
- Language changes for 3414 and 3515 [jcbrand]
- Czech translations [thomas_w]

0.22 (2011-09-05)
-----------------

- 3414: Bugfix on _actionplan_ landing page. Add i18n var. [jcbrand]
- Add DE, EL, SK translations [thomas_w]
- Add title attrs on clicktips for IE6/7 [jcbrand]
- Changed headers for mobile compatibility [jcbrand]
- Lots of browser fixes [jcbrand]

0.21 (2011-08-26)
-----------------

- NB: Depends on Euphorie 3.0syslab19 or higher

- Refactored @@delete on sector view back to Euphorie. [jcbrand]
- Depend on zrtresource screen-ie6. [jcbrand]
- More tests and bugfixes [jcbrand]
- Move the surveypopup code to survey_popup.js (disabled for now) [jcbrand]

0.20 (2011-08-23)
-----------------

- Updated Spanish translations [thomas_w]
- IE 6 fix. Remove the tooltips in AJAX add measure form. [jcbrand]
- Stop using minified css for IE6. [jcbrand]

0.19 (2011-08-16)
-----------------

- Updated French translations [jcbrand]

0.18 (2011-08-15)
-----------------

- #3044 Last wave of English changes [jcbrand]
- #3049 Design fixes [jcbrand]
- #3343 Customize InfoBubble description according to calculation method [jcbrand]
- #3361 Correct position of an info bubble [jcbrand]
- #3365 Add favicon [jcbrand]
- #3386: Rename "Next" and "Continue" buttons to "Save and continue" when on forms. [jcbrand]

0.17 (2011-07-02)
-----------------

- Bugfix, when populating Prevention Plan with standard solution [jcbrand]

0.16 (2011-07-01)
-----------------

- #1537 Merged changes from Euphorie.
        Use radio buttons instead of dropdown
        Add a new InfoBubble on the OiRA tool add page.
        Make fields required to remove "No Value" option. [jcbrand]
- #2510 Merged changes from Euphorie into osha.oira [jcbrand]
- #3002 Found and fixed some more instances where survey is being used [jcbrand]
- #3048 Updated the translations [jcbrand]
- #3323 Add custom start page with new text and merge old patch into this template [jcbrand]
- #2510 Add js to animate the measures button/link


0.15 (2011-05-31)
-----------------

- #2223 Add the FancyBox to the module evaluation page [jcbrand]


0.14 (2011-05-30)
-----------------

- #3044 New English copy [jcbrand]
- #3281 Fix is_region AttributeError when copying countries to the client [jcbrand]
- #3048 More translation updates

0.13 (2011-05-26)
-----------------

- #2223 Add FancyBox image zoom to module images [jcbrand]
- #3260 Make European Flag visible on the client homepage. [jcbrand]
- #3277 Stale quote [pilz]
- #3221 Priority gone for FR [jcbrand]
- #3048 Add more translations [jcbrand]
- #3265 Hide empty modules on final report [jcbrand]
- #2560 Info bubbles for statistics fields [jcbrand]


0.12 (2011-05-05)
-----------------

- Restructure package to faciliate automated tested.
- #2556 Backported the frontpage fixes from Cornelis. [jcbrand]
- #2754 Modules should be movable before profile questions. [jcbrand]
- #2611 Changed headings in the final report [jcbrand]
- #2885 Risks that are not evaluated but do have action plans must be shown as
  finalised. [jcbrand]


0.11 (2011-04-12)
-----------------

- #2611 The identification report should also have page numbers in the bottom
        right and the download date in the top right of each page. [jcbrand]
- #2885 Parked risks must also be shown affirmatively [jcbrand]


0.10 (2011-04-11)
-----------------

- #2560 Added a new schema field on the Sector obj, statistics_level.
- #2699 Headers of the Legal boxes and also the risk headings in the evaluation
        and identification reports must be in lower case for Greek.
- #2924 OiRA tools with policy risks that have been actioned, should not
        appear in the "Risks that have NOT been evaluated and do NOT have action
        plans", but instead in the top section.
- #2964 Make sure that the logo is visible on the last report page
- #2611 Lots of changes to the final download report
- #3002 the word "survey" should not be used anymore
- #2989 Final HTML report headers were dodgy in IE7
- #2914 The Hairdressers in Cyprus tool must be shown when viewing the Swedish sector in English
- #2885 String at the bottom of the final report changed.
        Risks that have been identified as not present should be stated affirmatively.
        Risks must have their priorities indicated (if set)
- #2560 Added admin-edit form and statistics level field on sectors
- #2752 Fixed default color for published surveys
- #2623 Empty legal boxes should not be displayed.

0.9 (2011-03-10)
----------------

- Two bugfixes (for which there aren't any ticket numbers).
  Both are related to the same problem of bullets sometimes being deeper than 4
  levels in the download forms.
  [jcbrand]


0.8 (2011-03-10)
----------------

- Just a version bump. [jcbrand]


0.7 (2011-03-10)
----------------

- #2367 and #2752: Fixed various color picker problems.
- #2750: OiRA client - Change text [jcbrand]
- #2591: Change text on the company form page [jcbrand]
- #2707: OiRA, client - change text above profile questions [jcbrand]


0.6 (2011-03-04)
----------------

- Merged new translation strings and default values to the .po files. [jcbrand]
- Bugfix in touch_surveys.py external-method. [jcbrand]
- #2649: Use portal_properties to store the survey urls. Fallback to English if
  none found. [jcbrand]


0.5 (2011-03-03)
----------------

- Just a version bump. [jcbrand]


0.4 (2011-03-03)
----------------

- #2649: We will now follow the convention that the different SurveyMonkey language
  URLs will be the base url (English version) plus _de, _nl, etc.
  [jcbrand]
- #2681: Remove header capitalization for Greek language. [jcbrand]
- #2555: The footer for the "contents of tool" .rtf document was changed. Also
  removed the "this risk must still be inventorised statement". [jcbrand]
- #2583: Problem in the sessions after updating and republishing [jcbrand]


0.3 (2011-02-23)
----------------

- during the xml import, langauge values might still include trailing and leading spaces.
  For the frontpage langauge detection, we need to strip them.
  [pilz]
- Bugfix for identification download report generation. [jcbrand]


0.2 (2011-02-23)
----------------

- (Hopefully) Resolves: #1433 #2231 #2293 #2555 #2556 #2621 #2623 #2649
  [jcbrand]


0.1 (2011-01-26)
----------------

* Initial release


