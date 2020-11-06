# ACL
## Presets
### Folder `/shares/cases`
* owner should be root
* other should have no permissions

### created groups
`managers` and `contractors`

### created users
`manager[12]` and `contractors[1-3]`
and users should have corresponding groups as primary group

## Tasks
### modify sharefolder
* set setgid bit onto subfolder `cases`
* set group `managers` permissions on subfolder `cases`
* set acl group `contractors` read, write and executable on `cases`
* user `contractor3` should have read and execute acls on subfolder
* set default acls for group `contractors` read, write and execute
* set default acls for user `contractor3` read and execute
