; This has been extracted from
; https://github.com/tldr-pages/tldr/blob/master/pages/common/kcadm.sh.md

% kcadm.sh, common

# Start an authenticated session
kcadm.sh config credentials --server <host> --realm <realm_name> --user <username> --password <password>

# Create a user
kcadm.sh create users -s username=<username> -r <realm_name>

# List all realms
kcadm.sh get realms

# Update a realm with JSON config
kcadm.sh update realms/<realm_name> -f <path_to_file.json>
