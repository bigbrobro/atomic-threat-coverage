| Title                | Suspicious Code Page Switch                                                                                                                                                 |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description          | Detects a code page switch in command line or batch scripts to a rare language                                                                                                                                           |
| ATT&amp;CK Tactic    |   This Detection Rule wasn't mapped to ATT&amp;CK Tactic yet  |
| ATT&amp;CK Technique |  This Detection Rule wasn't mapped to ATT&amp;CK Technique yet  |
| Data Needed          | <ul><li>[DN_0002_4688_windows_process_creation_with_commandline](../Data_Needed/DN_0002_4688_windows_process_creation_with_commandline.md)</li><li>[DN_0003_1_windows_sysmon_process_creation](../Data_Needed/DN_0003_1_windows_sysmon_process_creation.md)</li></ul>  |
| Enrichment           |  Data for this Detection Rule doesn't require any Enrichments.  |
| Trigger              |  There is no documented Trigger for this Detection Rule yet  |
| Severity Level       | medium |
| False Positives      | <ul><li>Administrative activity (adjust code pages according to your organisation's region)</li></ul>  |
| Development Status   | experimental |
| References           | <ul><li>[https://docs.microsoft.com/en-us/windows/win32/intl/code-page-identifiers](https://docs.microsoft.com/en-us/windows/win32/intl/code-page-identifiers)</li><li>[https://twitter.com/cglyer/status/1183756892952248325](https://twitter.com/cglyer/status/1183756892952248325)</li></ul>  |
| Author               | Florian Roth |


## Detection Rules

### Sigma rule

```
title: Suspicious Code Page Switch
id: c7942406-33dd-4377-a564-0f62db0593a3
status: experimental
description: Detects a code page switch in command line or batch scripts to a rare language
author: Florian Roth
date: 2019/10/14
references:
    - https://docs.microsoft.com/en-us/windows/win32/intl/code-page-identifiers
    - https://twitter.com/cglyer/status/1183756892952248325
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        CommandLine: 
            - 'chcp* 936'  # Chinese
            # - 'chcp* 1256' # Arabic
            - 'chcp* 1258' # Vietnamese
            # - 'chcp* 855'  # Russian
            # - 'chcp* 866'  # Russian
            # - 'chcp* 864'  # Arabic
    condition: selection
fields:
    - ParentCommandLine
falsepositives:
    - "Administrative activity (adjust code pages according to your organisation's region)"
level: medium

```





### splunk
    
```
(CommandLine="chcp* 936" OR CommandLine="chcp* 1258") | table ParentCommandLine
```






### Saved Search for Splunk

```
Generated with Sigma2SplunkAlert
[Suspicious Code Page Switch]
action.email = 1
action.email.subject.alert = Splunk Alert: $name$
action.email.to = test@test.de
action.email.message.alert = Splunk Alert $name$ triggered \
List of interesting fields:  \
ParentCommandLine: $result.ParentCommandLine$  \
title: Suspicious Code Page Switch status: experimental \
description: Detects a code page switch in command line or batch scripts to a rare language \
references: ['https://docs.microsoft.com/en-us/windows/win32/intl/code-page-identifiers', 'https://twitter.com/cglyer/status/1183756892952248325'] \
tags:  \
author: Florian Roth \
date:  \
falsepositives: ["Administrative activity (adjust code pages according to your organisation's region)"] \
level: medium
action.email.useNSSubject = 1
alert.severity = 1
alert.suppress = 0
alert.track = 1
alert.expires = 24h
counttype = number of events
cron_schedule = */10 * * * *
allow_skew = 50%
schedule_window = auto
description = Detects a code page switch in command line or batch scripts to a rare language
dispatch.earliest_time = -10m
dispatch.latest_time = now
enableSched = 1
quantity = 0
relation = greater than
request.ui_dispatch_app = sigma_hunting_app
request.ui_dispatch_view = search
search = (CommandLine="chcp* 936" OR CommandLine="chcp* 1258") | table ParentCommandLine,host | search NOT [| inputlookup Suspicious_Code_Page_Switch_whitelist.csv]
```