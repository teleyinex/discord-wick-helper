# Helper tool for Discord Wick bot

This tool allows you to get one of the raid reports and transform it into a list of commands that you can only copy and paste to ban accounts.

## How does it work

Just grab the log that Wick generates with the report. At the end of the report you will find a list of all the IDs. Copy them into a file named ids.txt.


Then, just run this command:

```
python chunk.py
```

You will get an output like this:

```
w!b ID1 ID2 ID3 ID4
```

The script tries to generate commands with only 4 IDs, so you can handle them properly.
# discord-wick-helper
