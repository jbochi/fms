FMS
===

Simple [FMS API](http://help.adobe.com/en_US/flashmediaserver/adminapi/WSa4cb07693d12388431df580a12a34991ebc-8000.html) client in Python

Example:

	>>> import fms
	>>> f = fms.FMS('server.example.com', port=1111, username='user', password='password')
	>>> f.getServerStats()
	{'timestamp': 'Wed May  2 14:41:44 2012', 'code': 'NetConnection.Call.Success', 'data': {'uptime': '1892397', 'cpu_Usage': '5', 'launchTime': 'Tue Apr 10 17:01:47 2012', 'memory_Usage': '9', 'io': {'working_threads': '0', 'msg_in': '58911366', 'admin_connects': '0', 'rtmfp_lookups_denied': '0', 'rtmfp_remote_forwards': '0', 'msg_dropped': '0', 'bytes_out': '986892', 'swf_verification_matches': '0', 'server_bytes_out': '0', 'bytes_in': '66998508848', 'swf_verification_failures': '0', 'reads': '41433623', 'debug_connects': '0', 'connected': '1', 'service_requests': '0', 'normal_connects': '1', 'swf_verification_unsupported_rejects': '0', 'rtmfp_lookups': '0', 'rtmfp_remote_forward_requests': '0', 'server_bytes_in': '0', 'rtmfp_remote_lookup_requests': '0', 'total_connects': '21', 'swf_verification_exceptions': '0', 'rtmp_connects': '1', 'total_disconnects': '20', 'rtmfp_remote_redirect_requests': '0', 'service_connects': '0', 'writes': '55073', 'bw_in': '50433', 'bw_out': '0', 'rtmfp_forwards': '0', 'total_threads': '611', 'rtmfp_remote_lookups': '0', 'swf_verification_remote_misses': '0', 'rtmfp_remote_redirects': '0', 'swf_verification_attempts': '0', 'group_connects': '0', 'rtmfp_redirects': '0', 'rtmfp_connects': '0', 'virtual_connects': '0', 'msg_out': '168'}, 'num_cores': '1', 'cpus': '24', 'physical_Mem': '1234165760'}, 'level': 'status'}
