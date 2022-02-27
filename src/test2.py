import json
import copy

aa = """
{ "1" : { "19" : { "segment_id" : [ 19 ], "worker_name" : "ci-vre-worker-9df5bbf79-knj45" }, "25" : { "segment_id" : [ 25 ], "worker_name" : "ci-vre-worker-9df5bbf79-qpfbk" }, "14" : { "segment_id" : [ 14 ], "worker_name" : "ci-vre-worker-9df5bbf79-mg5w9" }, "16" : { "segment_id" : [ 16 ], "worker_name" : "ci-vre-worker-9df5bbf79-fmdw9" }, "9" : { "segment_id" : [ 9 ], "worker_name" : "ci-vre-worker-9df5bbf79-697v2" }, "23" : { "segment_id" : [ 23 ], "worker_name" : "ci-vre-worker-9df5bbf79-7r4sn" }, "7" : { "segment_id" : [ 7 ], "worker_name" : "ci-vre-worker-9df5bbf79-2sflw" }, "10" : { "segment_id" : [ 10 ], "worker_name" : "ci-vre-worker-9df5bbf79-64l67" }, "18" : { "segment_id" : [ 18 ], "worker_name" : "ci-vre-worker-9df5bbf79-t2s9r" }, "5" : { "segment_id" : [ 5 ], "worker_name" : "ci-vre-worker-9df5bbf79-v4vw7" }, "20" : { "segment_id" : [ 20 ], "worker_name" : "ci-vre-worker-9df5bbf79-wttt2" }, "12" : { "segment_id" : [ 12 ], "worker_name" : "ci-vre-worker-9df5bbf79-2gtrb" }, "15" : { "segment_id" : [ 15 ], "worker_name" : "ci-vre-worker-9df5bbf79-6k6dd" }, "22" : { "segment_id" : [ 22 ], "worker_name" : "ci-vre-worker-9df5bbf79-db6vl" }, "21" : { "segment_id" : [ 21 ], "worker_name" : "ci-vre-worker-9df5bbf79-r97kk" }, "3" : { "segment_id" : [ 3 ], "worker_name" : "ci-vre-worker-9df5bbf79-5dj65" }, "6" : { "segment_id" : [ 6 ], "worker_name" : "ci-vre-worker-9df5bbf79-82pp7" }, "11" : { "segment_id" : [ 11 ], "worker_name" : "ci-vre-worker-9df5bbf79-9pqpm" }, "2" : { "segment_id" : [ 2 ], "worker_name" : "ci-vre-worker-9df5bbf79-x5mb8" }, "17" : { "segment_id" : [ 17 ], "worker_name" : "ci-vre-worker-9df5bbf79-s6gs2" }, "1" : { "segment_id" : [ 1 ], "worker_name" : "ci-vre-worker-9df5bbf79-nv77z" }, "24" : { "segment_id" : [ 24 ], "worker_name" : "ci-vre-worker-9df5bbf79-h6p85" }, "26" : { "segment_id" : [ 26 ], "worker_name" : "ci-vre-worker-9df5bbf79-sg9q5" }, "28" : { "segment_id" : [ 28 ], "worker_name" : "ci-vre-worker-9df5bbf79-v4qsh" }, "27" : { "segment_id" : [ 27 ], "worker_name" : "ci-vre-worker-9df5bbf79-skkpr" }, "8" : { "segment_id" : [ 8 ], "worker_name" : "ci-vre-worker-9df5bbf79-z6v9f" } } 
, "2" : {}}
"""
groups = json.loads(aa)
print(groups)
for group_id, group_info in groups.items():
    # 遍历副本，在原始列表中删除
    group_info_copy = copy.deepcopy(group_info)
    print("group_id:", group_id)
    for worker_id, worker_info in group_info_copy.items():
        print("worker_id", worker_id)
        if worker_info['worker_name'] == "ci-vre-worker-9df5bbf79-knj45":
            group_info.pop(worker_id)
            # logging.info('before unregister , groups : {}'.format(groups))
            # print(groups)
            # MongoManager().save_service_config('worker_config', 'group_config', groups)