---
title: "Orgzly"
tags:
    - outil
---

Gestionnaire de notes pour agenda, listes diverses...

## Recherches

- Agenda  
  `s.1y .b.annivs (it.none or I.conf) .it.done .i.call .i.buy o.sched .b.frise .b.chantiers`
- Auj et demain
  `s.1d .i.past o.sched .b.frise .b.chantiers`
- Chantiers
  `b.chantiers (s.lt.1d OR s.none) o.prio o.sched`

## Official documentation

(as of 2024-01-01: could be out of date)

- [[Orgzly#Syncing Notebooks]]
    - [[Orgzly#Repository Types]]
        - [[Orgzly#Dropbox]]
        - [[Orgzly#WebDAV]]
        - [[Orgzly#Directory (local storage)]]
    - [[Orgzly#Status Messages]]
        - [[Orgzly#No change]]
        - [[Orgzly#Saved to URL]]
        - [[Orgzly#Loaded from URL]]
        - [[Orgzly#Notebook has no link and one or more remote notebooks with the same name exist]]
        - [[Orgzly#Notebook has no link and multiple repositories exist]]
        - [[Orgzly#Both local and remote notebook have been modified]]
            - [[Orgzly#Manually merging the two, conflicting files when using Dropbox]]
    - [[Orgzly#Notes for Org mode users]]
        - [[Orgzly#Generated Org files]]
- [[Orgzly#Links]]
    - [[Orgzly#Web page]]
    - [[Orgzly#Email]]
    - [[Orgzly#Telephone number]]
    - [[Orgzly#Location]]
    - [[Orgzly#File]]
    - [[Orgzly#Note]]
    - [[Orgzly#Notebook]]
- [[Orgzly#Search]]
    - [[Orgzly#Search expressions]]
    - [[Orgzly#Sorting]]
    - [[Orgzly#Agenda]]
    - [[Orgzly#Examples]]
    - [[Orgzly#Search Results]]
- [[Orgzly#FAQ]]
    - [[Orgzly#How much does it cost?]]
    - [[Orgzly#Is the source code available?]]
    - [[Orgzly#I don't use Google Play, any alternatives?]]
    - [[Orgzly#Dropbox sync option is missing]]
    - [[Orgzly#Is there an iOS version?]]
- [[Orgzly#Privacy Policy]]
- [[Orgzly#Contact]]

## Syncing Notebooks

You can store your notebooks on Dropbox or sync them with a directory on your device.

Notebooks are written as plain text files in [Org mode](https://orgmode.org) file format.

Synchronization is currently manual – you have to initiate it yourself by clicking the `Sync` button. Button is located in the navigation drawer.

Note that Orgzly doesn't yet detect deletion of remote notebooks. If you delete a notebook in the repository it will be restored after sync (unless you deleted it in the app as well).

### Repository Types

#### Dropbox

The Dropbox app is not required for syncing, instead you will allow Orgzly to contact Dropbox on your behalf using the browser.

- Go to `Settings`
- Click on `Sync`
- Click on `Repositories`
- Click on `Dropbox` (if you already have some repositories, click the plus icon first)
- Enter the directory inside Dropbox (without "Dropbox" part)

#### WebDAV

You can sync your notebooks over WebDAV with any service that supports it, such as [Nextcloud](https://nextcloud.com/), for example.

- Go to `Settings`
- Click on `Sync`
- Click on `Repositories`
- Click on `WebDAV` (if you already have some repositories, click the plus icon first)
- Enter the URL, username and password

Optionally, if the server is using a self-signed certificate for example, you could add it here.

#### Directory (local storage)

Notebooks can be synced with one or more directories on your device.

- Go to `Settings`
- Click on `Sync`
- Click on `Repositories`
- Click on `Directory` (if you already have some repositories, click the plus icon first)
- Click `Browse` and select (or create new) directory

### Status Messages

After syncing is done, every notebook will have its sync status message updated.

#### No change

Notebook is already synced. Nothing to do.

#### Saved to URL

Notebook has been successfully synced by being saved to the repository represented by URL.

#### Loaded from URL

Notebook has been successfully synced by being loaded from the notebook represented by URL.

#### Notebook has no link and one or more remote notebooks with the same name exist

Orgzly doesn't know which remote notebook to use for syncing.

Each notebook must have a link to a remote notebook. Link is usually set automatically after the first sync. However, there are cases when this is not possible, or when the link is removed.

Link cannot be created after the first sync if:

- Notebook was created in Orgzly, but there is already a remote notebook with the same name in one of the repositories
- Multiple repositories are used and there is a notebook with the same name in them

Link is removed when:

- Repository is renamed or deleted

Link can be set manually:

- Open the list of notebooks ("Notebooks")
- Long-click on a notebook
- Click on `Set Link`
- Choose a repository
- Click `Set`

Link is set if you can see the URL next to the small link icon in notebook's details.

#### Notebook has no link and multiple repositories exist

See [[Orgzly#Notebook has no link and one or more remote notebooks with the same name exist]]

#### Both local and remote notebook have been modified

If you modify a notebook in Orgzly and at the same time (before performing a sync) you modify its linked remote notebook, next sync will leave the notebook in a conflicted state.

When notebook is not synced due to conflict, you have two options:

- `Force Load` to import remote notebook and overwrite the local version
- `Force Save` to export local notebook and overwrite the remote version

These actions are available in notebook's contextual menu:

- Open the list of notebooks ("Notebooks")
- Long-click on a notebook to open the menu

There is currently no other way to resolve a conflict within Orgzly itself.

##### Manually merging the two, conflicting files when using Dropbox

When the local and remote notebooks have been modified in a Dropbox repository you can take advantage of the facts that Orgzly stores information in text files (in the Org file format) and that Orgzly will create a new copy of the file if you remove it from Dropbox.

For example, you might move the original, underlying .org file in Dropbox to a different directory, then tell Orgzly to sync the files again (which will cause Orgzly to create a new file (with the same file name)). You can then use an external tool (such as a diff program) to compare your original file and the file that Orgzly created. You can then determine what changes were made, and which ones you wish to keep.

Be sure to remember that the new file (the one created by Orgzly) is where you want to put your final, merged version of the file.

### Notes for Org mode users

Notebooks are encoded in [Org mode](https://orgmode.org) file format.

#### Generated Org files

When compared to your original Org files, files generated by Orgzly might differ in the amount of white space, outlined below. Any other difference would be considered a serious bug.

- _By default, tags are separated from the title with a single space character._ You will lose your tags' indentation as if you had `org-tags-column` set to `0`.
    - You can set `Tags column` in the app's preferences (under `Settings / Sync / Org file format / Tags indentation`), which should behave just like `org-tags-column`.
    - There is also a preference to make `Tags column` output compatible with `org-indent-mode`.
- _Unsupported metadata below header is part of note's content._ As soon as any unsupported metadata is encountered, lines from that point until the next heading are considered part of note's content. You might find an unexpected new line between supported and unsupported metadata, because note's content is normally separated from heading by a new line.

If any of this is not working for you, please [[Orgzly#contact]]

## Links

Links can be used in note's title or content. Links can be enclosed in brackets (e.g. `[[link]]`). You can specify a name which will be displayed instead of the link (e.g. `[[link][name]]`).

### Web page

`https://www.orgzly.com`

### Email

`mailto:support@orgzly.com`

### Telephone number

You can dial a phone number, compose SMS or MMS.

- `tel:1-800-555-0199`
- `voicemail:1-800-555-0199`
- `sms:1-800-555-0199`
- `sms:1-800-555-0199?body=omw%20brt`
- `smsto:1-800-555-0199`
- `mms:1-800-555-0199`
- `mmsto:1-800-555-0199`

### Location

To open a map you can specify the exact location or a search query.

- `geo:40.7128,-74.0060`
- `geo:0,0?q=new+york+city`
- `geo:40.7128,-74.0060?z=11`

### File

Links to external files are supported.

Files are **relative to the main storage directory** (e.g. `/sdcard`).

- `file:Download/document.txt`
- `file:Music/song.mp3`

In Settings, you can change the relative root to point to any directory on your device. There is one setting to set the root for absolute links (e.g. `file:/readme.txt`), and another setting to set the root for relative links (e.g. `file:readme.txt`).

### Note

Linking to notes is done using properties. Two properties are supported – `ID` and `CUSTOM_ID`.

If you set note's property `ID` to `123e4567-e89b-12d3-a456-426655440000` you can link to the note using:

`id:123e4567-e89b-12d3-a456-426655440000`

Value can be anything, but [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) is recommended.

If you prefer a more user-friendly value, use `CUSTOM_ID` property. This type of link starts with `#` character, followed by the property value. It must be enclosed in brackets. If you set `CUSTOM_ID` to `Meeting checklist`, linking to that note is done using:

`[[#Meeting checklist]]`

### Notebook

Link to a notebook within the app looks like a link to an external file:

`file:gtd.org`

Only the name matters and it has to be the same as the notebook you are linking to.

## Search

Search expressions are separated with space.

They are implicitly joined by logical `AND`. `OR` operator is also supported. Both operators are case insensitive. `AND` has higher precedence than `OR`.

### Search expressions

Following search expressions are supported.

Some of them support `.` (NOT) operator (see the last column).

```plain
| Expression      | Finds notes              | Example           | .   |
| --------------- | ------------------------ | ----------------- | --- |
| `s.PERIOD`      | Scheduled within period  | `s.today`         | N   |
| `d.PERIOD`      | Deadline within period   | `d.le.2d`         | N   |
| `e.PERIOD`      | Event within period      | `e.ge.now`        | N   |
| `c.PERIOD`      | Closed within period     | `c.yesterday`     | N   |
| `cr.PERIOD`     | Created within period    | `cr.ge.yesterday` | N   |
| `i.STATE`       | With state               | `i.todo`          | Y   |
| `it.STATE-TYPE` | With state type          | `.it.done`        | Y   |
| `b.NOTEBOOK`    | From notebook            | `.b.Work`         | Y   |
| `t.TAG`         | With tag (inherited too) | `t.errand`        | Y   |
| `tn.TAG`        | With tag (note's only)   | `tn.toRead`       | Y   |
| `p.PRIORITY`    | Having priority          | `.p.c`            | Y   |
| `ps.PRIORITY`   | Having set priority      | `ps.b`            | Y   |
```

`PERIOD` can be:

- `OP.TIME` – matches time
- `none` (or `no`) – matches notes without the property

`OP` can be:

- `eq` – equal to `TIME`
- `ne` – not equal to `TIME`
- `lt` – less than `TIME`
- `le` – less than or equal to `TIME`
- `gt` – greater than `TIME`
- `ge` – greater than or equal to `TIME`

If `OP` is not specified:

- Default value for `s`, `d` and `cr` is `le`
- Default value for `c` is `eq`

`TIME` can be:

- `Nh` – `N` hours from now
- `Nd` – `N` days from now
- `Nw` – `N` weeks from now
- `Nm` – `N` months from now
- `Ny` – `N` years from now

`N` can be negative.

For example:

- `-2h` – two hours ago
- `5d` – five days from today
- `-2w` – two weeks ago
- `3m` – three months from today
- `1y` – one year from today

Few aliases for `TIME` are available:

- `tomorrow`, `tmrw` or `tom`
- `today` or `tod`
- `now`
- `yesterday`

`STATE` is a keyword like `TODO`, `DONE`, `NEW`, etc. Keywords are case insensitive. Only states specified in Settings can be searched by. Any keywords not included in the settings are not treated as states - they become part of note's title.

`STATE-TYPE` can be `todo`, `done` or `none`.

`NOTEBOOK` is the name of notebook. It must be surrounded with double quotes if it contains spaces.

`TAG` is searched as a substring. For example `t.bee` will find notes which are tagged with `beeblebrox`.

`PRIORITY` is a priority starting from `A`.

### Sorting

Default ordering of notes is by notebook name then priority. If `s` or `d` are used in the query, they are also sorted by scheduled or deadline time. They are always sorted by position in the notebook last.

You can change this behavior by using `o` operator.

Using `o.PROPERTY` will sort notes by property. `.o.PROPERTY` is also supported which sorts notes by property in reverse order. You can specify multiple operators and they will be used in order.

Following properties are supported:

```plain
|Property|Order by|
|---|---|
|`b` `book` `notebook`|Notebook name|
|`t` `title`|Title|
|`s` `sched` `scheduled`|Scheduled time|
|`d` `dead` `deadline`|Deadline time|
|`e` `event`|Event time|
|`c` `close` `closed`|Closed time|
|`cr` `created`|Created-at time|
|`p` `pri` `prio` `priority`|Priority|
|`st` `state`|States as defined in Settings|
```

When a note contains multiple events, only one of those events is considered when sorting. With `o.event` the oldest event is used. With `.o.event` most recent event is used.

### Agenda

You can add `ad.DAYS` to any query to display search results grouped by day.

`DAYS` is a number of days you want to display.

For example, `(t.gym or t.class) ad.3` will display notes tagged with `gym` or `class` with any type of time set within next 3 days.

### Examples

- `i.todo t.john` - Search for `TODO` notes which are tagged with `john`
- `b.Work .i.done` - Search in notebook `Work` for notes without `DONE` state
- `(b.Home or b.Work) phone` - Search in notebooks `Home` and `Work` for notes which contain the string `phone` in their title, content or any of the tags
- `s.1d p.a` - Search for priority `A` notes scheduled for tomorrow or earlier (same as `p.a s.tom`)
- `s.ge.today o.book o.pri` - Search for notes scheduled for today or later, sorting them by notebook name then priority
- `o.book o.pri o.s` - Sort by notebook name then priority then scheduled time
- `p.b` - Search for notes with priority `B` (includes notes with no priority if default priority is `B`)
- `ps.b` - Search for notes with priority set to `B`

### Search Results

For each note you can tap on it to edit the note immediately. For each note you can also swipe right to display a menu of options that allow you to assign a starting time, cycle through the `TODO` and `DONE` states, or to simply mark the note as `DONE`. If you swipe left you'll be given a single option: displaying the note in the notebook that contains it.

## FAQ

### How much does it cost?

Orgzly is free.

### Is the source code available?

Yes, source code is available on [GitHub](https://github.com/orgzly/orgzly-android).

### I don't use Google Play, any alternatives?

Orgzly is also available on [F-Droid](https://f-droid.org/app/com.orgzly). Or you can download APK files directly from [GitHub releases](https://github.com/orgzly/orgzly-android/releases) page.

### Dropbox sync option is missing

Are you using F-Droid version? Dropbox is only available in Google Play's version of the app.

### Is there an iOS version?

No, only Android version is available at the moment.

After implementing some of the important features which are still missing in the current Android version, there is an idea to start working on either iOS version or a Web application.

## Privacy Policy

See [Privacy Policy](https://www.orgzly.com/privacy).

## Contact

Email us at [support@orgzly.com](mailto:support@orgzly.com) and visit [Orgzly.com](https://www.orgzly.com).

Follow us on [Twitter](https://twitter.com/Orgzly) and [Facebook](https://www.facebook.com/Orgzly).

Help us localize Orgzly by joining our [Crowdin project](https://crowdin.com/project/orgzly).

[Email](mailto:support@orgzly.com) [GitHub](https://github.com/orgzly) [Twitter](https://twitter.com/Orgzly) [Facebook](https://www.facebook.com/Orgzly)

[Privacy Policy](https://www.orgzly.com/privacy)
