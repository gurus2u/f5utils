# Guru Palnisamy
# one liner to trigger and download backup from unix/mac terminal or windows command proxmpt using ssh client

_u=$(ssh <f5_host_or_mgmt_ip> "tmsh save sys ucs \$(echo \$HOSTNAME|cut -d. -f1)-\$(date +%Y%m%d-%H%M)"|tail -1|cut -d' ' -f1) && scp <f5_host_or_mgmt_ip>:$_u ./

## End of Source ##
