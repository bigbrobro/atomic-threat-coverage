ta_mapping = {
    "attack.initial_access": [
        "Initial Access",
        "TA0001"
    ],
    "attack.execution": [
        "Execution",
        "TA0002"
    ],
    "attack.persistence": [
        "Persistence",
        "TA0003"
    ],
    "attack.privilege_escalation": [
        "Privilege Escalation",
        "TA0004"
    ],
    "attack.defense_evasion": [
        "Defense Evasion",
        "TA0005"
    ],
    "attack.credential_access": [
        "Credential Access",
        "TA0006"
    ],
    "attack.discovery": [
        "Discovery",
        "TA0007"
    ],
    "attack.lateral_movement": [
        "Lateral Movement",
        "TA0008"
    ],
    "attack.collection": [
        "Collection",
        "TA0009"
    ],
    "attack.exfiltration": [
        "Exfiltration",
        "TA0010"
    ],
    "attack.command_and_control": [
        "Command and Control",
        "TA0011"
    ],
    "attack.impact": [
        "Impact",
        "TA0040"
    ]
}
te_mapping = {
    "T1156": ".bash_profile and .bashrc",
    "T1134": "Access Token Manipulation",
    "T1015": "Accessibility Features",
    "T1531": "Account Access Removal",
    "T1087": "Account Discovery",
    "T1098": "Account Manipulation",
    "T1182": "AppCert DLLs",
    "T1103": "AppInit DLLs",
    "T1155": "AppleScript",
    "T1527": "Application Access Token",
    "T1017": "Application Deployment Software",
    "T1138": "Application Shimming",
    "T1010": "Application Window Discovery",
    "T1123": "Audio Capture",
    "T1131": "Authentication Package",
    "T1119": "Automated Collection",
    "T1020": "Automated Exfiltration",
    "T1197": "BITS Jobs",
    "T1139": "Bash History",
    "T1009": "Binary Padding",
    "T1067": "Bootkit",
    "T1217": "Browser Bookmark Discovery",
    "T1176": "Browser Extensions",
    "T1110": "Brute Force",
    "T1088": "Bypass User Account Control",
    "T1191": "CMSTP",
    "T1042": "Change Default File Association",
    "T1146": "Clear Command History",
    "T1115": "Clipboard Data",
    "T1522": "Cloud Instance Metadata API",
    "T1538": "Cloud Service Dashboard",
    "T1526": "Cloud Service Discovery",
    "T1116": "Code Signing",
    "T1059": "Command-Line Interface",
    "T1043": "Commonly Used Port",
    "T1092": "Communication Through Removable Media",
    "T1500": "Compile After Delivery",
    "T1223": "Compiled HTML File",
    "T1109": "Component Firmware",
    "T1122": "Component Object Model Hijacking",
    "T1175": "Component Object Model and Distributed COM",
    "T1090": "Connection Proxy",
    "T1196": "Control Panel Items",
    "T1136": "Create Account",
    "T1003": "Credential Dumping",
    "T1503": "Credentials from Web Browsers",
    "T1081": "Credentials in Files",
    "T1214": "Credentials in Registry",
    "T1094": "Custom Command and Control Protocol",
    "T1024": "Custom Cryptographic Protocol",
    "T1207": "DCShadow",
    "T1038": "DLL Search Order Hijacking",
    "T1073": "DLL Side-Loading",
    "T1002": "Data Compressed",
    "T1485": "Data Destruction",
    "T1132": "Data Encoding",
    "T1022": "Data Encrypted",
    "T1486": "Data Encrypted for Impact",
    "T1001": "Data Obfuscation",
    "T1074": "Data Staged",
    "T1030": "Data Transfer Size Limits",
    "T1530": "Data from Cloud Storage Object",
    "T1213": "Data from Information Repositories",
    "T1005": "Data from Local System",
    "T1039": "Data from Network Shared Drive",
    "T1025": "Data from Removable Media",
    "T1491": "Defacement",
    "T1140": "Deobfuscate/Decode Files or Information",
    "T1089": "Disabling Security Tools",
    "T1488": "Disk Content Wipe",
    "T1487": "Disk Structure Wipe",
    "T1172": "Domain Fronting",
    "T1483": "Domain Generation Algorithms",
    "T1482": "Domain Trust Discovery",
    "T1189": "Drive-by Compromise",
    "T1157": "Dylib Hijacking",
    "T1173": "Dynamic Data Exchange",
    "T1514": "Elevated Execution with Prompt",
    "T1114": "Email Collection",
    "T1519": "Emond",
    "T1499": "Endpoint Denial of Service",
    "T1480": "Execution Guardrails",
    "T1106": "Execution through API",
    "T1129": "Execution through Module Load",
    "T1048": "Exfiltration Over Alternative Protocol",
    "T1041": "Exfiltration Over Command and Control Channel",
    "T1011": "Exfiltration Over Other Network Medium",
    "T1052": "Exfiltration Over Physical Medium",
    "T1190": "Exploit Public-Facing Application",
    "T1203": "Exploitation for Client Execution",
    "T1212": "Exploitation for Credential Access",
    "T1211": "Exploitation for Defense Evasion",
    "T1068": "Exploitation for Privilege Escalation",
    "T1210": "Exploitation of Remote Services",
    "T1133": "External Remote Services",
    "T1181": "Extra Window Memory Injection",
    "T1008": "Fallback Channels",
    "T1107": "File Deletion",
    "T1006": "File System Logical Offsets",
    "T1044": "File System Permissions Weakness",
    "T1083": "File and Directory Discovery",
    "T1222": "File and Directory Permissions Modification",
    "T1495": "Firmware Corruption",
    "T1187": "Forced Authentication",
    "T1144": "Gatekeeper Bypass",
    "T1061": "Graphical User Interface",
    "T1484": "Group Policy Modification",
    "T1148": "HISTCONTROL",
    "T1200": "Hardware Additions",
    "T1158": "Hidden Files and Directories",
    "T1147": "Hidden Users",
    "T1143": "Hidden Window",
    "T1179": "Hooking",
    "T1062": "Hypervisor",
    "T1183": "Image File Execution Options Injection",
    "T1525": "Implant Container Image",
    "T1054": "Indicator Blocking",
    "T1066": "Indicator Removal from Tools",
    "T1070": "Indicator Removal on Host",
    "T1202": "Indirect Command Execution",
    "T1490": "Inhibit System Recovery",
    "T1056": "Input Capture",
    "T1141": "Input Prompt",
    "T1130": "Install Root Certificate",
    "T1118": "InstallUtil",
    "T1534": "Internal Spearphishing",
    "T1208": "Kerberoasting",
    "T1215": "Kernel Modules and Extensions",
    "T1142": "Keychain",
    "T1161": "LC_LOAD_DYLIB Addition",
    "T1149": "LC_MAIN Hijacking",
    "T1171": "LLMNR/NBT-NS Poisoning and Relay",
    "T1177": "LSASS Driver",
    "T1159": "Launch Agent",
    "T1160": "Launch Daemon",
    "T1152": "Launchctl",
    "T1168": "Local Job Scheduling",
    "T1162": "Login Item",
    "T1037": "Logon Scripts",
    "T1185": "Man in the Browser",
    "T1036": "Masquerading",
    "T1031": "Modify Existing Service",
    "T1112": "Modify Registry",
    "T1170": "Mshta",
    "T1104": "Multi-Stage Channels",
    "T1188": "Multi-hop Proxy",
    "T1026": "Multiband Communication",
    "T1079": "Multilayer Encryption",
    "T1096": "NTFS File Attributes",
    "T1128": "Netsh Helper DLL",
    "T1498": "Network Denial of Service",
    "T1046": "Network Service Scanning",
    "T1126": "Network Share Connection Removal",
    "T1135": "Network Share Discovery",
    "T1040": "Network Sniffing",
    "T1050": "New Service",
    "T1027": "Obfuscated Files or Information",
    "T1137": "Office Application Startup",
    "T1502": "Parent PID Spoofing",
    "T1075": "Pass the Hash",
    "T1097": "Pass the Ticket",
    "T1174": "Password Filter DLL",
    "T1201": "Password Policy Discovery",
    "T1034": "Path Interception",
    "T1120": "Peripheral Device Discovery",
    "T1069": "Permission Groups Discovery",
    "T1150": "Plist Modification",
    "T1205": "Port Knocking",
    "T1013": "Port Monitors",
    "T1086": "PowerShell",
    "T1504": "PowerShell Profile",
    "T1145": "Private Keys",
    "T1057": "Process Discovery",
    "T1186": "Process Doppelg\u00e4nging",
    "T1093": "Process Hollowing",
    "T1055": "Process Injection",
    "T1012": "Query Registry",
    "T1163": "Rc.common",
    "T1164": "Re-opened Applications",
    "T1108": "Redundant Access",
    "T1060": "Registry Run Keys / Startup Folder",
    "T1121": "Regsvcs/Regasm",
    "T1117": "Regsvr32",
    "T1219": "Remote Access Tools",
    "T1076": "Remote Desktop Protocol",
    "T1105": "Remote File Copy",
    "T1021": "Remote Services",
    "T1018": "Remote System Discovery",
    "T1091": "Replication Through Removable Media",
    "T1496": "Resource Hijacking",
    "T1536": "Revert Cloud Instance",
    "T1014": "Rootkit",
    "T1085": "Rundll32",
    "T1494": "Runtime Data Manipulation",
    "T1178": "SID-History Injection",
    "T1198": "SIP and Trust Provider Hijacking",
    "T1184": "SSH Hijacking",
    "T1053": "Scheduled Task",
    "T1029": "Scheduled Transfer",
    "T1113": "Screen Capture",
    "T1180": "Screensaver",
    "T1064": "Scripting",
    "T1063": "Security Software Discovery",
    "T1101": "Security Support Provider",
    "T1167": "Securityd Memory",
    "T1505": "Server Software Component",
    "T1035": "Service Execution",
    "T1058": "Service Registry Permissions Weakness",
    "T1489": "Service Stop",
    "T1166": "Setuid and Setgid",
    "T1051": "Shared Webroot",
    "T1023": "Shortcut Modification",
    "T1218": "Signed Binary Proxy Execution",
    "T1216": "Signed Script Proxy Execution",
    "T1518": "Software Discovery",
    "T1045": "Software Packing",
    "T1153": "Source",
    "T1151": "Space after Filename",
    "T1193": "Spearphishing Attachment",
    "T1192": "Spearphishing Link",
    "T1194": "Spearphishing via Service",
    "T1071": "Standard Application Layer Protocol",
    "T1032": "Standard Cryptographic Protocol",
    "T1095": "Standard Non-Application Layer Protocol",
    "T1165": "Startup Items",
    "T1528": "Steal Application Access Token",
    "T1539": "Steal Web Session Cookie",
    "T1492": "Stored Data Manipulation",
    "T1169": "Sudo",
    "T1206": "Sudo Caching",
    "T1195": "Supply Chain Compromise",
    "T1019": "System Firmware",
    "T1082": "System Information Discovery",
    "T1016": "System Network Configuration Discovery",
    "T1049": "System Network Connections Discovery",
    "T1033": "System Owner/User Discovery",
    "T1007": "System Service Discovery",
    "T1529": "System Shutdown/Reboot",
    "T1124": "System Time Discovery",
    "T1501": "Systemd Service",
    "T1080": "Taint Shared Content",
    "T1221": "Template Injection",
    "T1072": "Third-party Software",
    "T1209": "Time Providers",
    "T1099": "Timestomp",
    "T1537": "Transfer Data to Cloud Account",
    "T1493": "Transmitted Data Manipulation",
    "T1154": "Trap",
    "T1127": "Trusted Developer Utilities",
    "T1199": "Trusted Relationship",
    "T1111": "Two-Factor Authentication Interception",
    "T1065": "Uncommonly Used Port",
    "T1535": "Unused/Unsupported Cloud Regions",
    "T1204": "User Execution",
    "T1078": "Valid Accounts",
    "T1125": "Video Capture",
    "T1497": "Virtualization/Sandbox Evasion",
    "T1102": "Web Service",
    "T1506": "Web Session Cookie",
    "T1100": "Web Shell",
    "T1077": "Windows Admin Shares",
    "T1047": "Windows Management Instrumentation",
    "T1084": "Windows Management Instrumentation Event Subscription",
    "T1028": "Windows Remote Management",
    "T1004": "Winlogon Helper DLL",
    "T1220": "XSL Script Processing"
}
mi_mapping = {
    "M1036": "Account Use Policies",
    "M1015": "Active Directory Configuration",
    "M1049": "Antivirus/Antimalware",
    "M1013": "Application Developer Guidance",
    "M1048": "Application Isolation and Sandboxing",
    "M1047": "Audit",
    "M1040": "Behavior Prevention on Endpoint",
    "M1046": "Boot Integrity",
    "M1045": "Code Signing",
    "M1043": "Credential Access Protection",
    "M1053": "Data Backup",
    "M1042": "Disable or Remove Feature or Program",
    "M1055": "Do Not Mitigate",
    "M1041": "Encrypt Sensitive Information",
    "M1039": "Environment Variable Permissions",
    "M1038": "Execution Prevention",
    "M1050": "Exploit Protection",
    "M1037": "Filter Network Traffic",
    "M1035": "Limit Access to Resource Over Network",
    "M1034": "Limit Hardware Installation",
    "M1033": "Limit Software Installation",
    "M1032": "Multi-factor Authentication",
    "M1031": "Network Intrusion Prevention",
    "M1030": "Network Segmentation",
    "M1028": "Operating System Configuration",
    "M1027": "Password Policies",
    "M1026": "Privileged Account Management",
    "M1025": "Privileged Process Integrity",
    "M1029": "Remote Data Storage",
    "M1022": "Restrict File and Directory Permissions",
    "M1044": "Restrict Library Loading",
    "M1024": "Restrict Registry Permissions",
    "M1021": "Restrict Web-Based Content",
    "M1020": "SSL/TLS Inspection",
    "M1054": "Software Configuration",
    "M1019": "Threat Intelligence Program",
    "M1051": "Update Software",
    "M1052": "User Account Control",
    "M1018": "User Account Management",
    "M1017": "User Training",
    "M1016": "Vulnerability Scanning"
}